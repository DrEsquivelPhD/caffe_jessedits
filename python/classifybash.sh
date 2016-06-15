#!/bin/bash

# bash for loop
for f in $( ls ../data/neutrinodata/val  ); do
#for f in $( ls test  ); do
	python2.7 classify_test.py --print_results ../data/neutrinodata/val/$f $f.npy 
done 
