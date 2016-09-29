#!/bin/bash

# bash for loop
for f in $( ls  ); do
        python roicrop_mcc7.py $f
done 
~    
