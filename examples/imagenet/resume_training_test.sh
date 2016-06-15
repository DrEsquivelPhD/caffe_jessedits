#!/usr/bin/env sh

./../../build/tools/caffe train \
    --solver=/home/jessi12/CNN_local/caffe/models/bvlc_reference_caffenet_jessedits/solver.prototxt \
   # --weights=/home/jessi12/CNN_local/caffe/models/bvlc_reference_caffenet_jessedits/neutrino_v2/stoppingpnts/caffenet_train_iter_1161.caffemodel \
    --snapshot=/home/jessi12/CNN_local/caffe/models/bvlc_reference_caffenet_jessedits/neutrino_v2/caffenet_train_iter_2000.solverstate
