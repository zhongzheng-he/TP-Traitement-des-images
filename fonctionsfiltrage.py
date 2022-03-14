#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:49:51 2017

@author: emilien
"""

import numpy as np


def convolution(im, filter):
    """
    apply convolution filter to image 
    im : image
    filter : filter array
    """
    
    # init some variables depending on filter and image sizes    
    filterrows,filtercols = filter.shape
    imrows,imcols = im.shape
    xpadding = filtercols//2
    ypadding = filterrows//2

    #init output image
    imfiltered = np.zeros(im.shape)   
    
    # scan image
    for r in range(ypadding,imrows-ypadding):
        for c in range(xpadding, imcols-xpadding):
            sum=0
            # apply conv for the current position
            for rf in range(filterrows):
                for cf in range(filtercols):
                    sum += filter[rf,cf] * im[r+rf-ypadding, c+cf-xpadding]
            imfiltered[r,c] = sum
    
    return imfiltered     
    
def median(im, size):
    """
    apply convolution filter to image 
    im : image
    size : filter size
    """
    # init some variables depending on filter and image size s   
    imrows,imcols = im.shape
    xpadding = size//2
    ypadding = size//2
    
    #init output image
    imfiltered = np.zeros(im.shape)   
    
    # scan image
    for r in range(ypadding,imrows-ypadding):
        for c in range(xpadding, imcols-xpadding):
            pixels=[]
            cpt=0
            # apply median algo for the current position
            for rf in range(size):
                for cf in range(size):
                    pixels.append(im[r+rf-ypadding, c+cf-xpadding])
                    cpt+=1
                    
            pixels.sort() # pixels sort
            imfiltered[r,c] = pixels[len(pixels)//2] # take median value and apply
    
    return imfiltered     