#!/usr/bin/env sh

./../../build/tools/caffe train \
    --solver=/home/jessica/caffe/models/bvlc_reference_caffenet_jessedits/solver.prototxt \
    --snapshot=/home/jessica/caffe/models/bvlc_reference_caffenet_jessedits/caffenet_train_iter_1939.solverstate
