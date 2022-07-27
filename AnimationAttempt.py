#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 10:32:24 2022

@author: benchenevert
"""

import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np


#Initial Empty Plot

fig = plt.figure()
ax = plt.axes(xlim=(-50, 50),ylim=(-50, 50))
line, = ax.plot([],[], lw=2)

#xlim(-50, 50)
#ylim(-50, 50)

#Function to create empty line

def func():
    line = ax.set_data([],[])
    return line,

    #ln, plt.plot([],[])
    #ln.set_data
    
#Parametric Equation to Plot

xarray = []
yarray = []

def animate(i):
    t = 0.1*i
    
    x = t*np.sin(t)
    y = t*np.cos(t)
    
    xarray.append(x)
    yarray.append(y)
    
    line.set_data(xarray,yarray)
    
    return line,

#Plot Animation

anim = animation.FuncAnimation(fig,animate,frames = 500,interval = 20)

#anim = animation.FuncAnimation(fig,animate,frames = 500,interval = 20)

plt.show()
    
    
    
    
    
    
    
    

