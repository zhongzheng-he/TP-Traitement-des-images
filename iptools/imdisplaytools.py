# -*- coding: utf-8 -*-
"""
Image display functions :
- imshow : display image

@author: emilien
"""
import numpy as np 
import matplotlib.pyplot as pl
import iptools.luttools as lt
import matplotlib
def imshow(I,lut=None, cmap=None, autorescale=None, interpolation='none', overlaymaskorlabel=None, overlayalpha=0.5) :
    """
    display image
    arg 1 : "I" => 2D array : Image or fft2 image
    arg 2 (optional) : "lut" => 1D array : y values
    arg 3 (optional) : "cmap" => string : custom colormap (see matplotlib.pyplot for cmap details)
    arg 4 (optional) : "autorescale" => bool : if True automatically adjust image display between min & max (like a ramp lut)
    arg 5 (optional) : "interpolation" => string : specify interpolation type
    arg 6 (optional) : "overlaymaskorlabel" => binary mask or int labeled image : to overlay mask or labeled image over displayed image
    arg 7 (optional) : "overlayalpha" ==> float between 0. and 1. : alpha value (1 - transparency) of the overlayed mask or labeled image
    """
    isinteger = "int" in (I.dtype).name
    if "complex" in str(I.dtype):
        tmp = abs(I)
        tmp[tmp==0]=1
        tmp = np.log10(tmp)
        imshow(tmp,autorescale=True) 
    elif len(I.shape)==2:
        if (autorescale is None) or (autorescale == False) :
            if isinteger:
                minval=0;maxval=np.iinfo((I.dtype).name).max
            else:
                minval=0;maxval=1
        else :
            minval = np.amin(I);maxval = np.amax(I)
        
        if lut is not None :
            maxval=len(lut)
            pl.imshow(I,cmap=lt.LUT2Colormap(lut),vmin=minval,vmax=maxval, interpolation=interpolation)
            pl.axis('off')
        else:
            if (cmap is not None):
                pl.imshow(I,cmap=cmap,vmin=minval,vmax=maxval, interpolation=interpolation)
                pl.axis('off')
            else:
                pl.imshow(I,cmap="gray",vmin=minval,vmax=maxval, interpolation=interpolation)
                pl.axis('off')
        
        if overlaymaskorlabel is not None :
            colors = [(0,0,0,0)] + [(pl.cm.jet(i)) for i in range(1,256)] 
            new_map = matplotlib.colors.LinearSegmentedColormap.from_list('new_map', colors, N=256)
            '''pl.hold(True)  '''          
            pl.imshow(overlaymaskorlabel, cmap=new_map, alpha=overlayalpha, interpolation='none')
            '''pl.hold(False)  '''          
    elif len(I.shape)==3:
        pl.imshow(I,interpolation=interpolation)
        pl.axis('off')
    else:
        raise Exception("Error : Image dimension >3")
        
def labelcolorshow(labelIm) :
    """
    display labelized image into color
    arg 1 : "labelIm" => 2D array : labelized image 
    """
    if len(labelIm.shape)==2:
        
        pl.imshow(labelIm, interpolation='none')
        pl.axis('off')
    
    else:
        raise Exception("Error : Image dimension >2")

if __name__ == '__main__':
    import scipy.misc as imload
    import luttools
    import iminfos
    
    E = imload.imread("./images/enhance-me.gif");
    L1,X1 = luttools.createLinearGrayscaleLUT(256,iminfos.immin(E),iminfos.immax(E))
    imshow(E,L1)
    
