# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 12:21:44 2016

@author: emilien

kmean exemple exercice
"""

import numpy as np
import scipy.misc as misc
import skimage as ski
import sklearn.cluster as skclus
import matplotlib.pyplot as plt
import iptools.imdisplaytools as imdisp

def myKmeans(im, k, k_init=None):
    """
    kmean clustering
    arg 1 : "im" => 2D array : Image 
    arg 2 : k => int : number of classes for output
    arg 3 (optional) : classes centers initialisation (by default, classes centers are evenly-distributed between min and max of the image)
    """
    
    #if k_init not specified : init an array with centers evenly ditributed between min and max of image
    if not k_init:
        k_init = np.array(list(range(np.amin(im),np.amax(im),(np.amax(im)-np.amin(im))//k)))
    
    # create observations variable which is image flatten (2D==>1D array)
    obs = im.flatten()
    isContinue=True;
    # initialise centers (classes avg) and obs classes
    centers = k_init.copy()
    obsClass = np.zeros(obs.shape)
    
  
    # while isContinue is true
    while (isContinue): 
        # inside loop, initialization stuff...
        previousCenters = centers.copy()
        sumCenters = np.zeros(k_init.shape)
        nbSamplesByCenters = np.zeros(k_init.shape)
        
        # for each pixel in image, choose the best classe (which had the best distance between intensity value and center value)
        for i in range(len(obs)):
            o = obs[i]
            classindex = np.argmin(abs(centers-o))
            
            sumCenters[classindex] += o
            nbSamplesByCenters[classindex] +=1
            obsClass[i] = classindex
          
        # update classes centers with the news distribution
        centers = sumCenters / nbSamplesByCenters
        
        
        # compute convergence value (difference between new centers and the previous one)
        conv = np.sum(abs(centers-previousCenters))
    
        
       
        # if conv value is small ==> stop the loop
        if (conv < 0.01):
            isContinue=False
            
    
    # at the end, create an classified image by reshaping obsClass 1D to 2D array    
    imClass = obsClass.reshape(im.shape)
    
    # return classes centers and classified image
    return (centers, imClass)

# TODO : load "brain2.png" image

# TODO : apply myKmeans on it

# TODO : display the new classified image using imdisp.labelcolorshow
# (considering each class number as a different label)
