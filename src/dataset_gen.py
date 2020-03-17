import cv2
import os
from opencv_sketching import sketch
import argparse
from glob import glob
import time
import shutil

def gen_dataset(path, targpath):
    
    try:
        if not os.path.exists(path):
            raise NotADirectoryError
        if not os.path.exists(targpath):
            print("Target dataset folder doesnt exist. Making one ...")
            os.mkdir(targpath)
            os.mkdir(targpath+"/sketch")
            os.mkdir(targpath+"/original")
    except NotADirectoryError:
        print("Source dataset directory not found") 
    except FileNotFoundError:
        print("Error in target directory address")

    start_time = time.time()
    for idx, item in enumerate(os.walk(path)):        
        if idx == 0:
            continue
        if idx % 10 == 0:
            print("Processing Image #", idx+1)        
        for i in item[2]:
            img = cv2.imread(os.path.join(item[0], i))
            sketch(img, os.path.join(targpath, "sketch/img_{}.jpg".format(idx+1)))
            shutil.copyfile(os.path.join(item[0], i), os.path.join(targpath, "original/img_{}.jpg".format(idx+1)))

    print("total time taken: ", time.time() - start_time)
 




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", required=True, action="store", help="Original dataset location")
    parser.add_argument("-t", "--target", required=True, action="store", help="target directory of new dataset")
    parser.add_argument("-v", "--validation", action="store", help="store valdiation fraction")
    args = parser.parse_args()
    
    gen_dataset(args.path, args.target)
    
