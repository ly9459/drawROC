#!/bin/sh
TOOLS = ./build/tools

#save ./probs.txt
#$sudo ./build/tools/test test -model ./examples/mnist/lenet_test.prototxt  -weights ./examples/mnist/lenet_iter_10000.caffemodel
$sudo ./build/tools/test test -model ./examples/cifar10/cifar_test.prototxt  -weights ./examples/cifar10/cifar10_quick_iter_10000.caffemodel.h5
#draw roc
$sudo python ./python/draw_roc.py

