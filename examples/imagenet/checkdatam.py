#!/usr/bin/env python

caffe_root = '/home/jessi12/CNN_local/caffe/'  # this file is expected to be in {caffe_root}/examples
import numpy as np
import lmdb
import caffe

env = lmdb.open('/home/jessi12/CNN_local/caffe/examples/imagenet/neutrinodata_train_lmdb/', readonly=True)
with env.begin() as txn:
    raw_datum = txn.get(b'00000000')

datum = caffe.proto.caffe_pb2.Datum()
#datum.ParseFromString(datum)

flat_x = np.fromstring(datum.data, dtype=np.uint8)
x = flat_x.reshape(datum.channels, datum.height, datum.width)
print datum.channels
print datum.height
print datum.width
y = datum.label
print y

