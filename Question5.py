#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 2022

@author: benchenevert
"""



import sympy as sp
import numpy as np

from sympy import diff

sp.init_printing()

x,y = sp.symbols('x,y')
pi = sp.symbols('pi')

expr = (x**3 - ((sp.cos(pi * x))**2) / (2 * x**2 + 1) + ((11/3) * x**2) - 1)


display(diff(expr, x))

#display(expr.expand())