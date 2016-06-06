import sys
import cv2

print sys.argv[1] 
img = cv2.imread(sys.argv[1])

crop_img = cv2.resize(img, (224,224)) # Crop from x, y, w, h -> 100, 200, 300, 400
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
#cv2.imshow("cropped", crop_img)
cv2.imwrite(sys.argv[1],crop_img)
cv2.waitKey(0)
