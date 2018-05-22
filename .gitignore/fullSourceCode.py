import cv2
import numpy as np
from sys import argv

g = [ ]  #the list in which we will stuff single grayscale pixel value inplace of 3 RBG values
#this function converts each RGB pixel value into single Grayscale pixel value and appends that value to list 'g'
def rgb2gray(img):
    global g
    row,col,CHANNEL = img.shape
    for i in range(row) :
        for j in range(col):
            a = (img[i,j,0]*0.299 + img[i,j,1]*0.587 + img[i,j,2]*0.114)
            g.append(a)
    return 

def histogram(image):
    row = image.shape[0]
    col = image.shape[1]
    htg = [0] * 256
    for i in range(0, row):
	for j in range(0, col):
            htg[image[i, j]] += 1
    return htg

def equalize(image):
    hist = histogram(image)
    for i in range(1, 256):
	hist[i] += hist[i-1]
	
    eql = []
    for i in range(0, 256):
	eql.append(round(255 * hist[i]/hist[255]))
	
    row = image.shape[0]
    col = image.shape[1]

    for i in range(0, row):
	for j in range(0, col):
	    image[i, j] = eql[image[i, j]]

    return image
if __name__ == '__main__':
    filename = argv[1]
    image = cv2.imread(filename)
    row,col,ch = image.shape
    rgb2gray(image)  #convert the img1 into grayscale
    gr = np.array(g)  #convert the list 'g' containing grayscale pixel values into numpy array
    cv2.imwrite("grayImage.png" , gr.reshape(row,col)) #save the image file as grayImage.png

    image = cv2.imread('grayImage.png',-1)
    img = equalize(image)
    cv2.imwrite('equalizeImage.png',img)
    cv2.destroyAllWindows()
