import os
import sys
import importlib
import base64
import argparse
from PIL import Image
import io
import numpy as np
import cv2
import matplotlib.pyplot as plt



try:
    sys.path.index(os.path.dirname(os.path.abspath(__file__))+"/pytorch-CycleGAN-and-pix2pix")
except ValueError:          
    sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/pytorch-CycleGAN-and-pix2pix")  

import torch
from torchvision import transforms
from options import test_options
from models import create_model

def infer(b64):
    
    #we handle the options first. hardcode some params  
    opts = test_options.TestOptions().parse()
    opts.num_threads = 0
    opts.batch_size = 1
    opts.serial_batches = True
    opts.no_flip = True
    opts.display_id = -1
    opts.checkpoints_dir = "./src/pytorch-CycleGAN-and-pix2pix/checkpoints"
    #opts.checkpoints_dir = "./pytorch-CycleGAN-and-pix2pix/checkpoints"
    opts.name = "sketch_pix2pix"
    opts.model = "test"
    opts.netG = "unet_256"
    opts.direction = "BtoA"
    opts.dataset_mode = "single"    
    opts.norm = "batch"   
    

    model = create_model(opts)
    #print(opts)
    model.setup(opts)

    if opts.eval:
        model.eval()
    
    if isinstance(b64, bytes):
        img = Image.open(io.BytesIO(base64.decodebytes(b64)))
    else:    
        img = Image.open(io.BytesIO(base64.decodebytes(bytes(b64, 'utf-8'))))
    

    tsfms = transforms.Compose([
        transforms.Resize((256,256), Image.BICUBIC),
        transforms.ToTensor(),
        transforms.Normalize((.5,.5,.5),(.5,.5,.5))
    ])

    img = tsfms(img)

    img = torch.unsqueeze(img, 0)

    data = {
        "A": img,
        "A_paths": __file__
    }

    model.set_input(data)
    model.test()

    visuals = model.get_current_visuals()

    fake = list(visuals.items())[1][1]
    fake = fake.data
    fake = torch.squeeze(fake, 0).float().numpy()
    fake = (np.transpose(fake, (1,2,0)) + 1)/ 2.0 * 255.0
    fake = fake.astype(np.uint8)

    buff = io.BytesIO()
    fake = Image.fromarray(fake)
    fake.save("fake4.jpeg")
    fake.save(buff, "JPEG")
    return base64.b64encode(buff.getvalue())

if __name__ == "__main__":

    
    sys.stdout = open(os.devnull, 'w')
    
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--base64", action="store", help="base64 string of the image")
    parser.add_argument("-i", "--img", action="store", help="Address of the image")
    args = parser.parse_args()
    if args.base64:
        fake_b64 = infer(args.base64)
        sys.stdout = sys.__stdout__
        resp_obj = {
            "encoding" : fake_b64
        }
        print(resp_obj)


    else:
        with open(args.img, "rb") as f:
            string = base64.b64encode(f.read())
            res = infer(string)
            resp_obj = {
                'encoding': res
            }
            print(resp_obj)



