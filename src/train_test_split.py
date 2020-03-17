import os
import argparse
import random
import shutil

def train_test_split(path, ratio):
    if not os.path.exists(path + "/train"):
        os.mkdir(path + "/train")
        os.mkdir(path + "/train/sketch")
        os.mkdir(path + "/train/original")
    if not os.path.exists(path + "/test"):
        os.mkdir(path + "/test")
        os.mkdir(path + "/test/sketch")
        os.mkdir(path + "/test/original")    

    original_dir = path + "/original"
    sketch_dir = path + "/sketch"

    img_list = os.listdir(original_dir)
    max_train = int(ratio * len(img_list))

    #we shift the train images
    count = 0
    while count <= max_train:
        if count % 5 == 0:
            print("Processing image #{}".format(count+1))
        try:    
            idx = random.randint(0, len(img_list) - 1)
            img = img_list[idx]
        except IndexError:
            print("Index Error: Index: {}, length: {}".format(idx, len(img_list)))  
            exit
        del img_list[idx]
        shutil.copyfile(original_dir+"/"+img, path+"/train/original/"+img)
        shutil.copyfile(sketch_dir+"/"+img, path+"/train/sketch/"+img)
        count += 1
    print("{} images in train".format(count))
    
    count = 0
    #now we shift the test images
    for img in img_list:
        print("Processing img #", count+1)
        shutil.copyfile(original_dir+"/"+img, path+"/test/original/"+img)
        shutil.copyfile(original_dir+"/"+img, path+"/test/sketch/"+img)
        count += 1
    print("{} images in test".format(count))     

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="path to dataset", required=True, action='store')
    parser.add_argument("-r", "--ratio", help="ratio of train test split", required=True, action="store")
    args = parser.parse_args()

    train_test_split(args.path, float(args.ratio))
    