#Import all the nessesary libraries
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import caffe
import os
from os import listdir
import time
import sys 

#Set caffe to cpu or gpu mode, either is caffe.set_mode_cpu() or caffe.set_mode_gpu()
caffe.set_mode_cpu()

#Define variable for location of required files
MODEL_FILE = '../models/bvlc_reference_caffenet_jessedits/deploy.prototxt'
PRETRAINED = '../models/bvlc_reference_caffenet_jessedits/caffenet_train_iter_2150.caffemodel'
MEAN_FILE = './caffe/imagenet/imagenet_mean1.npy'
LABEL_FILE = '../data/neutrinodata1/synset_words.txt'

#Load the BVLC Reference Caffenet models
net = caffe.Classifier(MODEL_FILE, PRETRAINED,
                       mean=np.load(MEAN_FILE),
                       channel_swap=None,
                       raw_scale=255,
                       image_dims=(224, 224))

'''net = caffe.Classifier(MODEL_FILE, PRETRAINED)
net.set_channel_swap('data',(2,1,0))
net.set_raw_scale('data',255)
net.set_mean('data',np.load(MEAN_FILE))'''

pred_features = []

input_image = caffe.io.load_image(sys.argv[1])

'''
#Let plot out the image
plt.imshow(input_image)
plt.savefig('../examples/images/cat.jpg')
plt.close()
'''

#Predict class
start = time.time()
prediction = net.predict([input_image])
print("Done in %.2f s." % (time.time() - start))
print 'prediction shape:', prediction[0].shape[0]
print 'predicted class:', prediction[0].argmax()

#Predict label
fi = open(LABEL_FILE)
labels = fi.readlines()
print 'predicted name:', labels[prediction[0].argmax()],



#Plot the polygon frequency
plt.plot(prediction[0])
#plt.savefig(sys.argv[1])
plt.close()

