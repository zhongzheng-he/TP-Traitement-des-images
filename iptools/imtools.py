# -*- coding: utf-8 -*-
"""
Image tools functions : 
- imconvert : return converted image as a new type (numpy array type). Do not modify original image

@author: emilien
"""

def imconvert(I,dtype):
    """
    return converted image as a new type (numpy array type). Do not modify original image
    arg 1 : "I" => 2D array : Image 
    arg 1 : "dtype" => string : new type (see numpy array type for more details)
    """
    return I.astype(dtype)