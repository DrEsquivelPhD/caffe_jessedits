#!/usr/bin/env python
"""
classify.py is an out-of-the-box image classifer callable from the command line.
By default it configures and runs the Caffe reference ImageNet model.
"""
import numpy as np
import pandas as pd
import os
import sys
import argparse
import glob
import time
import cv2
from skimage.color import rgb2gray

import caffe


def main(argv):
    pycaffe_dir = os.path.dirname(__file__)

    parser = argparse.ArgumentParser()
    # Required arguments: input and output files.
    parser.add_argument(
        "input_file",
        help="Input image, directory, or npy."
    )
    parser.add_argument(
        "--print_results",
        action='store_true',
        help="Write output text to stdout rather than serializing to a file."
    )
    parser.add_argument(
        "--labels_file",
        default=os.path.join(pycaffe_dir,
                "../data/neutrinodata1/synset_words.txt"),
        help="Readable label definition file."
    )    
    parser.add_argument(
        "output_file",
        help="Output npy filename."
    )
    # Optional arguments.
    parser.add_argument(
        "--model_def",
        default=os.path.join(pycaffe_dir,
                "../models/bvlc_reference_caffenet_jessedits/deploy.prototxt"),
        help="Model definition file."
    )
    parser.add_argument(
        "--pretrained_model",
        default=os.path.join(pycaffe_dir,
                "../models/bvlc_reference_caffenet_jessedits/caffenet_train_iter_2000.caffemodel"),
        help="Trained model weights file."
    )
    parser.add_argument(
        "--gpu",
        action='store_true',
        help="Switch for gpu computation."
    )
    parser.add_argument(
        "--center_only",
        action='store_true',
        help="Switch for prediction from center crop alone instead of " +
             "averaging predictions across crops (default)."
    )
    parser.add_argument(
        "--images_dim",
        default='224,224,1',
        help="Canonical 'height,width' dimensions of input images."
    )
    parser.add_argument(
        "--mean_file",
        default=os.path.join(pycaffe_dir,
                             'caffe/imagenet/imagenet_mean1.npy'),
        help="Data set image mean of [Channels x Height x Width] dimensions " +
             "(numpy array). Set to '' for no mean subtraction."
    )
    parser.add_argument(
        "--input_scale",
        type=float,
        help="Multiply input features by this scale to finish preprocessing."
    )
    parser.add_argument(
        "--raw_scale",
        type=float,
        default=255.0,
        help="Multiply raw input by this scale before preprocessing."
    )
    parser.add_argument(
        "--channel_swap",
        default= None,
        help="Order to permute input channels. The default converts " +
             "RGB -> BGR since BGR is the Caffe default by way of OpenCV."
    )
    parser.add_argument(
        "--ext",
        default='bmp',
        help="Image file extension to take as input when a directory " +
             "is given as the input file."
    )
    parser.add_argument(
        "--force_grayscale",
        action='store_true',
        help="Converts RGB images down to single-channel grayscale versions," +
             "useful for single-channel networks like MNIST."
    )
    args = parser.parse_args()
    

    image_dims = [int(s) for s in args.images_dim.split(',')]
    if args.force_grayscale:
       channel_swap = None 
       mean = np.load(args.mean_file)
    else:
        mean = np.load(args.mean_file)
        #channel_swap = [int(s) for s in args.channel_swap.split(',')]
        channel_swap = None 

    if args.gpu:
        caffe.set_mode_gpu()
        print("GPU mode")
    else:
        caffe.set_mode_cpu()
        print("CPU mode")


    # Load numpy array (.npy), directory glob (*.jpg), or image file.
    args.input_file = os.path.expanduser(args.input_file)
    if args.input_file.endswith('npy'):
        print("Loading file: %s" % args.input_file)
        inputs = np.load(args.input_file)
    elif os.path.isdir(args.input_file):
        print("Loading folder: %s" % args.input_file)
        inputs =[caffe.io.load_image(im_f)
                 for im_f in glob.glob(args.input_file + '/*.' + args.ext)]
    else:
        print("Loading file: %s" % args.input_file)
        img = cv2.imread(args.input_file)
        #img_gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY ); 
        inputs = [caffe.io.load_image(args.input_file)]
        #inputs = [img_gray]
        #print img_gray.shape
        print img.shape
    
    if args.force_grayscale:
       print("Checking that it is grayscaling")
       inputs = [rgb2gray(input) for input in inputs];
    

    print("Classifying %d inputs." % len(inputs))
    
    # Make classifier.
    classifier = caffe.Classifier(args.model_def, args.pretrained_model,
            image_dims=image_dims, mean=mean,
            input_scale=1.0, raw_scale=args.raw_scale,
            channel_swap=channel_swap)

    # Classify.
    start = time.time()
    scores = classifier.predict(inputs, not args.center_only).flatten()
    print("Done in %.2f s." % (time.time() - start))
    
    if args.print_results:
        with open(args.labels_file) as f:
          labels_df = pd.DataFrame([
               {
                   'synset_id': l.strip().split(' ')[0],
                   'name': ' '.join(l.strip().split(' ')[1:]).split(',')[0]
               }
               for l in f.readlines()
            ])
        labels = labels_df.sort('synset_id')['name'].values

        indices = (-scores).argsort()[:1]
        print indices
        print scores 
        predictions = labels[indices]
        print labels 

        meta = [
                   (p, '%.5f' % scores[i])
                   for i, p in zip(indices, predictions)
               ]

        print meta
    # Save
    print("Saving results into %s" % args.output_file)
    np.save(args.output_file, scores)


if __name__ == '__main__':
    main(sys.argv)
