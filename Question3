#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 20:36:05 2022

@author: benchenevert
"""

import math
import matplotlib.pyplot as plt

def sum2(N, x = []):
  
    x_totals = []
    for i in range(len(x)):
        total = 0
        for n in range(N):
            total += (x[i]**(n+1) * (1/(n+1)))
            
        x_totals.append(total)
        
    #return x_totals
    plt.plot(x,x_totals)
    