#!/usr/bin/env python

import caffe
import numpy as np
import sys

if len(sys.argv) != 3:
   print "Usage: python convert_protomean.py proto.mean out.npy"
sys.exit()
print "About to start!"
blob = caffe.proto.caffe_pb2.BlobProto()
print "finished setting blob"
data = open( sys.argv[1] , 'rb' ).read()
print "finished setting data"
blob.ParseFromString(data)
print "finished parsing data"
arr = np.array( caffe.io.blobproto_to_array(blob) )
print "finished creating array"
out = arr[0]
np.save( sys.argv[2] , out )
print "Finished converting"
                            
