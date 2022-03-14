# -*- coding: utf-8 -*-
"""
FFT tools functions : 
- imfft : return fft2 transform of the image
- imifft : return inv fft2 (fft transform to image)

@author: emilien
"""

import numpy as np

def imfft(I):
    """
    return fft2 transform of the image
    arg 1 : "I" => 2D array : Image 
    """
    fftim = np.fft.fft2(I)
    fftim = np.fft.fftshift(fftim)
    return fftim

def imifft(Ifft, dtype="uint8"):
    """
    return inv fft2 (fft transform to image)
    arg 1 : "Ifft" => 2D array : FFT image 
    arg 2 (optional) : dtype ==> string : orginal image type
    """
    Ifft = np.fft.fftshift(Ifft)
    imfiltered = (abs(np.fft.ifft2(Ifft))).astype(dtype)
    
    return imfiltered
    