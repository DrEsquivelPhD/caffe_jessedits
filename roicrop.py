#!/usr/bin/env python

import numpy as np
import cv2

img = cv2.imread('Muminus_Plane3_bmpfile1.bmp',0)
print img.shape
numnonzerorows = (img !=0).sum(1)
zeroindexvec   = np.where(numnonzerorows == 0)[0]
img = np.delete(img,zeroindexvec, axis=0)
print img.shape

img = img.transpose()
print img.shape
numnonzerorows = (img !=0).sum(1)
zeroindexvec   = np.where(numnonzerorows == 0)[0]
img = np.delete(img,zeroindexvec, axis=0)
print img.shape

img = img.transpose()

img = cv2.resize(img, (224,224)) # Crop from x, y, w, h -> 100, 200, 300, 400
cv2.imwrite('Muminus_Plane3_bmpfile1_mod.png',img)
img1 = cv2.imread('Muminus_Plane3_bmpfile1.bmp',0)
print 'Before:' 
print img1.shape
print 'After:' 
print img.shape

