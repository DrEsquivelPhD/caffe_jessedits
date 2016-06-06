#!/bin/bash

# bash for loop
for f in $( ls  ); do
	python crop.py $f
done 
