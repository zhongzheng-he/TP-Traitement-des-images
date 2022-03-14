# -*- coding: utf-8 -*-
"""
Image LUTs functions : 
- createLinearGrayscaleLUT : compute a linear ramp function (LUT) and return a tuple with x and y
- applyLUT : Apply lut to image I (permanently : modify original image)

@author: emilien
"""
import matplotlib
import numpy

def createLinearGrayscaleLUT(bins=256, vmin=-1, vmax=-1, inv=False):
    """
    compute a linear ramp function (LUT) and return a tuple with x array and y array
    (only for integer type image)
    - arg 1 : "bins" => int : number of values/samples (256 by default)
    - arg 2 (optional) : "vmin" => int : minimum input value (x axes) (0 by default)
    - arg 3 (optional) : "vmax" => int : maximum input value (x axes) (bins - 1 by default)
    - arg 4 (optional) : "inv" => bool : True to inverse LUT ramp function (False by default)
    """

    if vmin<0:
        vmin=0
        
    if vmax<0 :
        vmax = bins-1
    
    result = numpy.zeros(bins,dtype="uint16")
    for i in range(vmin,vmax+1):
        newvalue = round( (i-vmin)*(bins-1)/(vmax-vmin) )
        result[i] = newvalue
    
    if (inv):
        result = vmax - result
        
    return numpy.arange(bins),result

def LUT2Colormap(lut):
    """
    convert a LUT to a colormap (to display with matplotlib)
    (do not use)
    - arg 1 : "lut" => array : LUT y values array 
    """
    result = []    
    bins =len(lut) 
    maximum = bins-1
    for i in lut:
        grayvalue = i/maximum
        result.append( (grayvalue,grayvalue,grayvalue,1) )
    
    return matplotlib.colors.ListedColormap(result)
    
def applyLUT(I,lut):
    """
    Apply lut to image I (permanently : modify original image)
    - arg 1 : "I" =>  : image array
    - arg 2 : "lut" => array : LUT y values array 
    """
    I2 = I.copy()
    for i in range(len(lut)):
        I[I2==i]=lut[i]

if __name__ == '__main__':
    import scipy
    import matplotlib.pyplot as plt
    import numpy as np

    img = scipy.misc.face(gray=True)
    maximumvalue = np.iinfo('uint8').max
    lut1,x1 = createLinearGrayscaleLUT(maximumvalue+1)
    cmap1 = LUT2Colormap(lut1)
    colors = [cmap1(i) for i in range(cmap1.N)]
    
    plt.figure()
    plt.imshow(img,cmap1,vmin=0,vmax=1000)

    lut2 = lut1[::-1]   
    cmap2 = LUT2Colormap(lut2)
    
    
    plt.figure()
    plt.imshow(img,cmap2)
    
    #pts = plt.ginput(3) # it will wait for three clicks
    
    
