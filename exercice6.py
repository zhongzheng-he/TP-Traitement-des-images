# -*- coding: utf-8 -*-
"""
TP TNI Python. Secret code :)

@author: emilien
"""

import scipy.misc as misc 
import matplotlib.pyplot as plt
import iptools.imdisplaytools as imdisp
import numpy as np
import imageio as iio

imHeart = iio.imread("heart-gray.png")


plt.figure()
# Affichage de l'image originale
plt.subplot(1,2,1).set_title("image originale")
imdisp.imshow(imHeart)

print("Niveaux de gris dans l'image originale : \n",np.unique(imHeart))

imHeart2 = imHeart//100 * 100 # opération sur l'image ???

# Affichage de l'image modifiée
plt.subplot(1,2,2).set_title("image modifiée")
imdisp.imshow(imHeart2)

print("\n\nNiveaux de gris dans l'image modifiée : \n",np.unique(imHeart2))
