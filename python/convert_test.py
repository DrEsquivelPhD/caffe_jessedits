
#!/usr/bin/env python
# Make sure that caffe is on the python path:
caffe_root = '/home/jessica/caffe/'  # this file is expected to be in {caffe_root}/examples
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe
import numpy as np

#Convert mean file produced by Caffe to numpy array, assume 3 chanels
#python bin_to_npy.py dim_image_mean path_to_mean_caffe name_output

channels = 1

a = caffe.io.caffe_pb2.BlobProto()
with open(sys.argv[2],'rb') as f:
  a.ParseFromString(f.read())

means=a.data
means=np.asarray(means)
print means.shape
s = int(sys.argv[1])
means=means.reshape(channels,s,s)
np.save(sys.argv[3],means)
