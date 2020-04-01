## Training Procedure for Pix2Pix on Image2Sketch Custom Dataset

#### Prepare the Data
   
   All the commands listed here are executed from within the src directory
   
* *STEP 1: Download the Labeled faces in the Wild dataset (lfw)*
   
   Run the following command in the terminal
   ```
   $ download_lfw.sh
   ```
   
* *STEP 2: Generate the Original and Sketch pairs*
    
    We process each image in the lfw dataset and generate a sketch equivalent using standard opencv techniques. We put the original
    non-processed lfw images in <Dataset folder path>/originals directory and their sketch equivalents in <Dataset folder path>/sketch
    Enter the following code in your terminal. Replace <Datast folder path> with the directory address in which you want the 
    original and sketch folders. It will create a directory if it doesnt exist. If it exists, ensure that the following structure exists   
   * directory name/original
   * directory name/sketch
        
  
  
 
    ```
    $ python dataset_gen.py -p path/to/original/downloaded/lfw -t path/where/to/store/fw
    ```
    
*  *STEP 3: Prepare for pix2pix specific training*
    
    pix2pix demands that data for training be structured in a specific format.To ensure that run the following command in 
    ther terminal
    
    ```
    $ pix2pix_data.py -p path/to/processed/dataset -t path/to/final/dataset/location/
    ```
    
    Delete the other datasets to save space!
    
 * *STEP 4: Fold the data*
 
    Run the following command to prep the dataroot for the model.
    
    ```
    python pytorch-CycleGAN-and-pix2pix/datasets/combine_A_and_B.py --fold_A /path/to/data/A --fold_B /path/to/data/B --fold_AB /path/to/data
    ```
    
* *STEP 5: Train!*

    Follow this [doc](https://github.com/pranjaldatta/Image2Sketch/blob/master/src/pytorch-CycleGAN-and-pix2pix/scripts/train_pix2pix.sh) here.
    Name of model is **sketch_pix2pix** and direction is **AtoB**
    Some more [docs](https://github.com/pranjaldatta/Image2Sketch/tree/master/src/pytorch-CycleGAN-and-pix2pix/docs) to help you out!
