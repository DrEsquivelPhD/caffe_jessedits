#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=/home/jessi12/CNN_local/caffe/examples/imagenet
DATA=/home/jessi12/CNN_local/caffe/data/mupi_mcc7
TOOLS=/home/jessi12/CNN_local/caffe/tools

$TOOLS/compute_image_mean $EXAMPLE/mupi_mcc7_train_lmdb \
  $DATA/imagenet_mean.binaryproto

echo "Done."
