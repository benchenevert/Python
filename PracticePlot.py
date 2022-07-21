#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 15:07:14 2022

@author: benchenevert
"""

import math
import matplotlib.pyplot as plt

def sum2(N, x = []):
    
    x_totals = []
    for i in range(len(x)):
        total = 0
        for n in range(N+1):
            total += ((-1)**N)*(x[i]**(2*n))/(math.factorial(2*n))
            
        x_totals.append(total)
        
    #return x_totals
    plt.plot(x,x_totals)       
           