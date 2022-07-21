#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 17:30:36 2022

@author: benchenevert
"""
from IPython.display import display

import sympy as sp
sp.init_printing()

x,a,b,c = sp.symbols('x,a,b,c')

display(sp.solve((a * x**2 + b * x + c),x))