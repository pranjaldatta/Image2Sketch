# Image2Sketch
Translate self-potraits to sketchs using pix2pix

### About

Image translation from one domain to another domain is one of the most interesting applications of computer vision. 
The paper [Image translation using Conditional GANs](https://arxiv.org/pdf/1611.07004.pdf) demonstrated the use of cGANs for 
Image Translation.

In this project, a pix2pix PyTorch Implementation was trained on a custom generated dataset to translate potraits of people into their corresponding sketches. It was deployed as a simple web app using flask. 

### Get Started

* *STEP 1: Clone the Repository*
   
   Paste the following command in your terminal
```
$ git clone https://github.com/pranjaldatta/Image2Sketch.git
```

* *STEP 2: Create a conda environment* 

   From the cloned repository root, run the following command
```
$ conda env create -f env.yaml
```

* *STEP 3: Get the pre-trained weights*
   
   Download the pretrained weights from [here](https://drive.google.com/drive/folders/1fkHJesOOYjYWR9NH97iywD6TTuSJ7vDVusp=sharing), extract and place it in the /src/pytorch-CycleGAN-and-pix2pix/checkpoints/sketch_pix2pix

* *STEP 4: Run local server*
```
$ ./run_server.sh
```

* *STEP 5: Visit http://localhost:5000/*
    
   Visit http://localhost:5000/ and select an image and hit submit. 
   Check out the demo video!

### Demo

<a href="http://www.youtube.com/watch?feature=player_embedded&v=dLvr5bdT36s" target="_blank"><img src="http://img.youtube.com/vi/dLvr5bdT36s/0.jpg" alt="IMAGE ALT TEXT HERE" width="300" height="300"  /></a>


### Examples


* *Example 1*:

<img src="https://github.com/pranjaldatta/Image2Sketch/blob/master/examples/example1.jpeg" height=200 width=200></img> 
<img src="https://github.com/pranjaldatta/Image2Sketch/blob/master/examples/example1_result.jpeg" height=200 width=200></img> 

* *Example 2*:

<img src="https://github.com/pranjaldatta/Image2Sketch/blob/master/examples/example2.jpeg" height=200 width=200></img> 
<img src="https://github.com/pranjaldatta/Image2Sketch/blob/master/examples/example2_result.jpeg" height=200 width=200></img> 

* *Example 3*:

<img src="https://github.com/pranjaldatta/Image2Sketch/blob/master/examples/example3.jpg" height=200 width=200></img> 
<img src="https://github.com/pranjaldatta/Image2Sketch/blob/master/examples/example3_result.jpeg" height=200 width=200></img> 

* *Example 4*:

<img src="https://github.com/pranjaldatta/Image2Sketch/blob/master/examples/example4.jpg" height=200 width=200></img> 
<img src="https://github.com/pranjaldatta/Image2Sketch/blob/master/examples/example4_result.jpeg" height=200 width=200></img>


### Training
    
For training check out the [doc](https://github.com/pranjaldatta/Image2Sketch/blob/master/docs/TRAINING.md)
   

### Credits: 

* [LFW Dataset](http://vis-www.cs.umass.edu/lfw/)
* [This](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) brilliant implementation in PyTorch

