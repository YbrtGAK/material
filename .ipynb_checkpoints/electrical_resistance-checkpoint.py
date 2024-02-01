# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 13:14:44 2023

@author: yberton
"""

"""Electrical resistivity"""

#imports
import numpy as np
from numpy import pi,log

#Dimensions
L = 300e-3 # Length [m]
De = 6e-3 # External diameter [m]
Di = 2e-3 # Internal diameter [m]
e = De - Di # Thickness [m]
Se = pi*De*L ; Si = pi*Di*L # [m²]

Ae = pi*De**2/4 ; Ai = pi*Di**2/4 # [m²]
A = Ae - Ai # Solid section of the tube [m²]


S = Se + Si + 2*A # [m²]
V = A*L 

#Physical ppties
Re = lambda e,rhoe : rhoe*A/L

#Aluminium 


#Inox
Re_inox = Re(e,60e-6)

