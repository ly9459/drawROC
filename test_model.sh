#!/bin/sh
TOOLS = ./build/tools

#save ./probs.txt
$sudo TOOLS/test test -model ./examples/mnist/lenet_test.prototxt  -weights ./examples/mnist/lenet_iter_10000.caffemodel
#draw roc
$sudo python ./python/draw_roc.py

