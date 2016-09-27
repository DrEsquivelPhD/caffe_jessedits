#!/usr/bin/env python

import sys
import numpy as np
import cv2
print sys.argv[1]
img = cv2.imread(sys.argv[1],0)
img1 = cv2.imread(sys.argv[1],0)

numnonzerorows = (img !=0).sum(1)
zeroindexvec   = np.where(numnonzerorows == 0)[0]
img = np.delete(img,zeroindexvec, axis=0)

img = img.transpose()
numnonzerorows = (img !=0).sum(1)
zeroindexvec   = np.where(numnonzerorows == 0)[0]
img = np.delete(img,zeroindexvec, axis=0)

img = img.transpose()

print 'Before:' 
print img1.shape
print 'After:' 
print img.shape

img = cv2.resize(img, (224,224)) # Crop from x, y, w, h -> 100, 200, 300, 400
print 'Image resize'
print img.shape

cv2.imwrite(sys.argv[1],img)

