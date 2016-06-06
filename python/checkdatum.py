#!/usr/bin/env python

caffe_root = '/home/jessica/caffe/'  # this file is expected to be in {caffe_root}/examples
import numpy as np
import lmdb
import caffe

env = lmdb.open('/home/jessica/caffe/examples/imagenet/neutrinodata3_train_lmdb/', readonly=True)
with env.begin() as txn:
    raw_datum = txn.get(b'00000000')

datum = caffe.proto.caffe_pb2.Datum()
#datum.ParseFromString(raw_datum)

flat_x = np.fromstring(datum.data, dtype=np.uint8)
x = flat_x.reshape(datum.channels, datum.height, datum.width)
print datum.channels 
print datum.height 
print datum.width 
y = datum.label
print y
'''
with env.begin() as txn:
    cursor = txn.cursor()
    for key, value in cursor:
        print(key, value)
'''
