import os
import argparse
import random
import shutil
import time

def shift_train(originals, fake, max_train, targpath):

    img_list = os.listdir(originals)
    count = 0
    
    start_time = time.time()
    while count <= max_train:        
        try:
            idx = random.randint(0, len(img_list)-1)    
            img = img_list[idx]
        except IndexError:
            print("IndexError: Index: {}, Length: {}".format(idx, len(img_list)))
            exit
        del img_list[idx]
        
        if count % 5 == 0:
            print("Processing image #{}: img_name: {}".format(count, img))        
        
        shutil.copyfile(originals+"/"+img, targpath+"/A/train/"+img)
        shutil.copyfile(fake+"/"+img, targpath+"/B/train/"+img) 

        count += 1

    train_time = time.time() - start_time
    print("-"*50)
    print("Moving test images ...") 

    count = 1
    start_time = time.time()
    for img in img_list:
        print("Processing test image #{}: Img Name: {}".format(count, img))
        shutil.copyfile(originals+"/"+img, targpath+"/A/test/"+img)
        shutil.copyfile(fake+"/"+img, targpath+"/B/test/"+img)
        count += 1
    test_time = time.time() - start_time

    print("-"*50)
    print("Train Images: {}, Time Taken: {}".format(max_train, train_time))
    print("Test Images: {}, Time Taken: {}".format(count, test_time))    


def train_test_split(path, targpath, ratio):

    try:
        if not os.path.exists(path):
            raise NotADirectoryError
        if not os.path.exists(targpath):
            print("Target dataset folder doesnt exist. Making one ...")
            os.mkdir(targpath)
            os.mkdir(targpath+"A")
            os.mkdir(targpath+"B")
            os.mkdir(targpath+"A/"+"train")
            os.mkdir(targpath+"A/"+"test")
            os.mkdir(targpath+"B/"+"train")
            os.mkdir(targpath+"B/"+"test")
    except NotADirectoryError:
        print("Source dataset directory not found") 
    except FileNotFoundError:
        print("Error in target directory address")    
    except:
        print("Error occured!")

    originals = path + "/original"
    fakes = path + "/sketch"

  
    max_train = int(ratio*len(os.listdir(originals)))

    #we shift the train 
    shift_train(originals, fakes, max_train, targpath)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path", help="path to dataset", required=True, action='store')
    parser.add_argument("-t", "--targ", help="path to target dataset dir", required=True, action="store")
    parser.add_argument("-r", "--ratio", help="ratio of train test split", required=True, action="store")
    args = parser.parse_args()

    train_test_split(args.path, args.targ, float(args.ratio))