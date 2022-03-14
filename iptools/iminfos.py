# -*- coding: utf-8 -*-
"""
Image infos functions :
- imtype : return image array type string
- imtypemax : return maximum value of image type
- imsize : return image size tuple 

@author: emilien
"""
import numpy as np

def imtype(I):
    """
    return image array type string
    arg 1 : "I" => 2D array : Image 
    """
    return (I.dtype).name
    
def imtypemax(I):
    """
    return maximum value of image type
    arg 1 : "I" => 2D array : Image 
    """
    return (np.iinfo((I.dtype).name)).max
    
def imsize(I):
    """
    return image size tuple (2 values for grayscale image, 3 value for color image)
    arg 1 : "I" => 2D array : Image 
    """
    return I.shape

