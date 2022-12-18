import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "img.jpg"

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140]) # 2 dimensional array formula to convert image to gray scale

def dodge(front,back):                  # function to dodge image
    result=front*255/(255-back)          # to get the image in the range of 0-255
    result[result>255]=255               # to get the image in the range of 0-255
    result[back==255]=255               
    return result.astype('uint8')           # to get the image in the range of 0-255


ss = imageio.imread(img)  # read image
gray = rgb2gray(ss)  # convert to grayscale

i = 255-gray  # invert image
blur = scipy.ndimage.filters.gaussian_filter(i,sigma=15)  # blur image
r = dodge(blur,gray)  # dodge image to get pencil sketch


cv2.imwrite('sketch.jpg',r)  # save image