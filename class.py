#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 11:14:12 2022

@author: benchenevert
"""
import random
import math

class person():
    def __init__(self,x,y):
        self.name
        self.height
        self.infection
        self.x = x
        self.y = y
        
        def move(self):
            
            a = random.random(1,4)
            
            if a == 1:
                self.x += 1
            elif a == 2:
                self.y += 1
            elif a == 3:
                self.x -= 1
            elif a == 4:
                self.y -= 1
        
class infected(person):
    pass

    def infect(self,person):
        
        distance = math.sqrt((self.x - person.x)**2 + (self.y - person.y)**2)
        
        if distance < 1:
            person.hitpoints -= 10