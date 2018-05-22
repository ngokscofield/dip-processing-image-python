import cv2
import numpy as np
from sys import argv
filename = argv[1]
image = cv2.imread(filename,0)
image1=cv2.equalizeHist(image)
cv2.imshow('image',image)
cv2.imshow('image1',image1)
cv2.imwrite('grayImageUseLibrary.png',image)
cv2.imwrite('equalizeImageUseLibrary.png',image1)
cv2.waitKey(0)
cv2.destroyAllWindows()
