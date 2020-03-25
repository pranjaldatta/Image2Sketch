import numpy as np 
from PIL import Image
import cv2
import matplotlib.pyplot as plt
from src import sketch_img

import subprocess
from src import sketch_img
from io import BytesIO
import base64
import json

def action(file):

    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(type(img))
    pil_img = Image.fromarray(img.astype("uint8"))
    pil_img.save('real4.jpeg')
    print(type(pil_img))
    buff = BytesIO()
    pil_img.save(buff, "JPEG")
    buff.seek(0)

    img_base64 = base64.b64encode(buff.read())

    

    resp_obj = subprocess.check_output(["python", "./src/sketch_img.py", "-b", img_base64])
    return resp_obj