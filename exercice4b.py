# -*- coding: utf-8 -*-
"""
TP TNI Python : Resolution VS Definition

@author: emilien
"""
from skimage.transform import resize
import matplotlib.pyplot as plt
import iptools.imdisplaytools as imdisp
import numpy as np
import imageio as iio

lenaIm = iio.imread("lena.png") #chargement de Lena
[rows,cols] = lenaIm.shape # retourne la taille (512x512)


lenaIm2 = resize(lenaIm, [rows//2, cols//2]) # retaille copie de lenaIm de taille /2
lenaIm3 = resize(lenaIm, [rows//4, cols//4]) # retaille copie de lenaIm de taille /4
lenaIm4 = resize(lenaIm, [rows//8, cols//8]) # retaille copie de lenaIm de taille /8
lenaIm5 = lenaIm.copy() # copie simplement lenaIm dans lenaIm5

plt.figure()

# affiche les différentes versions de lena sur une grille 
plt.subplot2grid((4,4), (0, 0)).set_title("a : 512x512")
imdisp.imshow(lenaIm)

plt.subplot2grid((4,4), (0, 1)).set_title("b : 256x256")
imdisp.imshow(lenaIm2)

plt.subplot2grid((4,4), (1, 0)).set_title("c : 128x128")
imdisp.imshow(lenaIm3)

plt.subplot2grid((4,4), (1, 1)).set_title("d : 64x64")
imdisp.imshow(lenaIm4)

plt.subplot2grid((4,4), (0, 2), colspan=2, rowspan=2).set_title("e : 512x512 \n taille vignette x 2")
imdisp.imshow(lenaIm5)
