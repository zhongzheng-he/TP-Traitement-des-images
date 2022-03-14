# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 18:12:24 2016

First image manipulations : To complete

@author: emilien
"""
import numpy as np
import scipy.misc as misc
import iptools.imdisplaytools as imdisp
from iptools.tictoc import *


# image loading => create an array im
im = misc.face(gray=True)

# display image
imdisp.imshow(im)

# display pixel value at position (row=42, column=1023)
print(im[42,1023])

# display image size
print(im.shape)
print("np pixels : ",im.shape[0]*im.shape[1])

# display image pixels type
print(im.dtype)

# display pixels sum
print(np.sum(im))

  
 
# display pixels average value
print(np.mean(im))
 
# copy im into im2 and multiply im2 pixels by 2; then display it
im2 = im[:]
im2 = im2 *2
imdisp.imshow(im2)



# display subimage of im [120 - 512][360-820]
imdisp.imshow(im[120:512,360:820])

# using loops, print every image's pixels
# TODO
#for r in range(im.shape[0]):
#    for c in range(im.shape[1]):
#        #print(im[r,c])

tic()
# copy im into im3 and, using loops, erase (draw in black) the region [120 - 512][360-820]
im3 = im[:]
for r in range(120,512):
    for c in range(360,820):
            im[r,c]=0

print("elapsed time 1 : ",toc())
imdisp.imshow(im3)

# display it
# TODO

tic()
# copy im into im4 and, using slicing, erase (draw in black) the region [120 - 512][360-820]
im4 = im[:]
im4[120:512,360:820] = 0
print("elapsed time 2 : ",toc())

imdisp.imshow(im3)

# display it
