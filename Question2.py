#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 19:03:21 2022

@author: benchenevert
"""
    


import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

n = sp.Symbol('n')

def sum1(n):
    
    n_totals = []
    total = 0
    for n in range(1000):
        
            
        total += (((-1)**(n + 1) * 1/n))
        
        n_totals.append(total)

        display(n_totals)
    
    
    # I have destroyed and retried this code more times than I have blinked and I don't know what to do.
    # The closest I have gotten has been an array with 10000 entries but they are all '-1'.
    # I believe that this version of my code is the closest to what is being asked but I keep getting 
    # getting the error "division by zero".
    
  




















     