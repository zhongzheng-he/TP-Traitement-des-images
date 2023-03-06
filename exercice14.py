# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 21:06:10 2016

@author: emilien

region growing exemple exercice

"""

import scipy.misc as misc
import iptools.luttools as luttools
import matplotlib.pyplot as plt
import iptools.imdisplaytools as imdisp
import numpy as np
import imageio as iio

def neighbours(pixelcoordinates, connexity):
    """
    get a list of neighbours coordinates [row column]
    arg1 : pixelcoordinates ==> [row column] : center pixel coordinates
    arg2 : connexity ==> int : 4 or 8 for 2D, 6 ou 26 for 3D
    """
    result = []
    
    dim = len(pixelcoordinates)
    
    if dim==2:
        if connexity==4 :
            for r in [-1, 0, 0, 1]:
                for c in [0, -1, 1, 0]:
                    newPixel = [pixelcoordinates[0]+r , pixelcoordinates[1]+c]
                    result.append(newPixel)
        elif connexity==8:
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    newPixel = [pixelcoordinates[0]+i, pixelcoordinates[1]+j]
                    result.append(newPixel)
            
    elif dim==3:
        raise NotImplementedError("3D neighbours not implemented yet !")
        
    return result
    

def regionGrowing(img, startpixel, delta):
    """
    TODO: describe this function
    """
    list = []
    list.append(startpixel)
    mask = np.zeros(img.shape, dtype="bool")
    rows,cols = img.shape
    
    refValue = img[startpixel[0],startpixel[1]]
    
    while len(list) > 0:
        
        for pixel in list:
            print(len(list))
            if (abs(int(img[pixel[0],pixel[1]])-refValue)<=delta):
                mask[pixel[0],pixel[1]]=True
                
                # check neighbours
                for newPixel in neighbours(pixel, 4):
                    if newPixel[0] >=0 and newPixel[0] < rows and newPixel[1] >=0 and newPixel[1] < cols:
                        if (not mask[newPixel[0],newPixel[1]]) and (newPixel not in list):
                            list.append(newPixel)
                    
            list.remove(pixel)        
    return mask

def pickImagePixelCoordinates(im):
    """
    Wait user click on image and return clicked pixel position [row column]
    arg1 : im ==> 2d array : image
    """
    imdisp.imshow(brainIm)
    #pickedPixelCoordinates = np.around(plt.ginput(1)) # il ne marche pas avec google colab
    pickedPixelCoordinates = np.around([102,102])# (102,102) est le centre de la tumeur
    pickedPixelCoordinates = np.reshape(pickedPixelCoordinates,[2,-1])
    pickedPixelCoordinates = pickedPixelCoordinates.astype("uint16")
    pickedPixelCoordinates = [pickedPixelCoordinates[1],pickedPixelCoordinates[0]] 
    
    return pickedPixelCoordinates
        

# load image
brainIm = iio.imread("brain2.png")

# get start pixel coordinates on image
pickedPixel =[102,102]

# apply region growing
mask = regionGrowing(brainIm,pickedPixel, 30)

# display segmented mask region over the original image
imdisp.imshow(brainIm, overlaymaskorlabel=mask, overlayalpha=0.5)

