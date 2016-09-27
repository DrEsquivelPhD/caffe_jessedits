#!/usr/bin/env python

import sys
import numpy as np
import cv2

print sys.argv[1]
#img = cv2.imread('Muminus_Plane3_bmpfile1.bmp',0)
img = cv2.imread(sys.argv[1],0)
img1 = cv2.imread(sys.argv[1],0)

#print img.shape
numnonzerorows = (img).sum(1)
#print numnonzerorows.shape
zeroindexvec=[]
for x in xrange(len(numnonzerorows)):
	if numnonzerorows[x]==0:
	 	zeroindexvec.append(x)	
	if numnonzerorows[x]!=0: 	
		#print "in first else loop"
		#print x 
		#print numnonzerorows[x]
		break

print img.shape
for y in xrange(len(numnonzerorows)):
	if numnonzerorows[-y -1]==0:
	 	zeroindexvec.append(len(numnonzerorows)-y-1)
	if numnonzerorows[-y -1]!=0:
		#print "in second else loop"
		#print numnonzerorows[-y-1] 
		break
img = np.delete(img,zeroindexvec, axis=0)

#print img.shape


#print img.shape
img = img.transpose()
#print img.shape
numnonzerocols = (img).sum(1)
#print numnonzerocols.shape
zeroindexvec1=[]

for x in xrange(len(numnonzerocols)):
	if numnonzerocols[x]==0:
	 	zeroindexvec1.append(x)	
	if numnonzerocols[x]!=0: 	
		#print "in first else loop"
		#print x 
		#print numnonzerocols[x]
		break

#print img.shape
for y in xrange(len(numnonzerocols)):
	if numnonzerocols[-y -1]==0:
	 	zeroindexvec1.append(len(numnonzerocols)-y-1)
	if numnonzerocols[-y -1]!=0:
		#print "in second else loop"
		#print numnonzerocols[-y-1] 
		break
img = np.delete(img,zeroindexvec1, axis=0)

#print img.shape

img = img.transpose()
#print img.shape

def padzero(vector, pad_width, iaxis, kwargs):
	vector[:pad_width[0]] = 0
	vector[-pad_width[1]:] = 0
	return vector

img = np.lib.pad(img,(5,),padzero)
#print img.shape[0]
#print img.shape[1]
if img.shape[0] <224 and img.shape[1]<224:
	if img.shape[0]<img.shape[1]:
		img = np.lib.pad(img,(224-img.shape[0]),padzero)	
	if img.shape[1]<img.shape[0]:
		img = np.lib.pad(img,(224-img.shape[1]),padzero)	

#img = img.transpose()
img = cv2.resize(img, (224,224)) # Crop from x, y, w, h -> 100, 200, 300, 400
cv2.imwrite(sys.argv[1],img)
print 'Before:' 
print img1.shape
print 'After:' 
print img.shape

