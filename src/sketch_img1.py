import os
import sys
import importlib
import base64
import argparse
from PIL import Image
import io
import numpy as np
import cv2


def infer(b64):
    
    #we handle the options first. hardcode some params  
    opts = options.TestOptions()
    opts.num_threads = 0
    opts.batch_size = 1
    opts.serial_batches = True
    opts.no_flip = True
    opts.display_id = -1
    opts.checkpoints_dir = "./pytorch-CycleGAN-and-pix2pix/checkpoints"
    opts.name = "sketch_pix2pix"
    opts.model = "test"
    opts.netG = "unet_256"
    opts.direction = "BtoA"
    opts.dataset_mode = "single"    
    opts.norm = "batch"
    opts = opts.parse()

    model = models.create_model(opts)
    model.setup(opts)

    if opts.eval:
        model.eval()

    cv2.namedWindow("Frame")
    img = Image.open(io.BytesIO(base64.decodebytes(b64)))
    img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

    cv2.imshow("Frame", img)



if __name__ == "__main__":
    try:
        sys.path.index(os.path.dirname(os.path.abspath(__file__))+"/pytorch-CycleGAN-and-pix2pix")
    except ValueError:  
        
        print("Appending...")  
        sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/pytorch-CycleGAN-and-pix2pix")    
    
    
    options = importlib.import_module("pytorch-CycleGAN-and-pix2pix.options.test_options")
    models = importlib.import_module("pytorch-CycleGAN-and-pix2pix.models")
    create_dataset = importlib.import_module("pytorch-CycleGAN-and-pix2pix.data", "create_dataset")
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--base64", action="store", help="base64 string of the image")
    parser.add_argument("-i", "--img", action="store", help="Address of the image")
    args = parser.parse_args()

    with open(args.img, "rb") as f:
        string = base64.b64encode(f.read())
    infer(string)
"""
with open("img.jpg", "wb") as fs:
    fs.write(base64.decodebytes(string))

img = Image.open(io.BytesIO(base64.decodebytes(string)))
img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
print(type(img))
"""