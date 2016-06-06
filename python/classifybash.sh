#!/bin/bash

# bash for loop
for f in $( ls ../data/neutrinodata2/train  ); do
#for f in $( ls test  ); do
	python classify_test.py $f $f.npy 
done 
