#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 10:51:30 2022

@author: benchenevert
"""
import random
import Animal
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def animate(frame_number):
    for an in pop:
        an.move(x_min,x_max,y_min,y_max)


    d.set_data([animal.x for animal in pop if 
animal.__class__ is Animal.prey],[animal.y for animal in
pop if animal.__class__ is Animal.prey])
    c.set_data([animal.x for animal in pop if 
animal.__class__ is Animal.predator],[animal.y for animal
in pop if animal.__class__ is Animal.predator])
    e.set_data([animal.x for animal in pop_dead],[animal.y
for animal in pop_dead])













x_max = 25
x_min = 0
y_max = 25
y_min = 0




num_prey = 25
num_predator = 5

pop = [Animal.prey(x_max*np.random.uniform(0,1),
y_max*np.random.uniform(0,1)) for i in range(num_prey)] \
    + [Animal.predator(x_max*np.random.uniform(0,1),
y_max*np.random.uniform(0,1)) for i in range(num_predator)]
    
pop_dead = []



ax = plt.axes(xlim=(x_min,x_max), ylim=(y_min, y_max))
fig = plt.gcf()


d, = plt.plot([animal.x for animal in pop if 
animal.__class__ is Animal.prey],[animal.y for animal in
pop if animal.__class__ is Animal.prey], 'bo', markersize = 
5)
c, = plt.plot([animal.x for animal in pop if 
animal.__class__ is Animal.predator],[animal.y for animal
in pop if animal.__class__ is Animal.predator], 'ro', 
markersize = 5)
e, = plt.plot([animal.x for animal in pop_dead],[animal.y
for animal in pop_dead], 'o', color = 'black', markersize =
5)


anim = animation.FuncAnimation(fig, animate, frames = 500,
interval=1, repeat=False)












