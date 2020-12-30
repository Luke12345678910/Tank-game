#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 17:59:03 2020

@author: luke
"""
import pyglet
import math

import resources

class PhysicalObject(pyglet.sprite.Sprite):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.dead = False
        self.shape = 0
        
    def update(self, dt):
        #check if shape is dead
        if (self.shape.dead == True):
            self.die()
        #binding sprites to shapes
        if self.dynamic:
            self.x = self.body.position.x
            self.y = self.body.position.y
            self.rotation = math.degrees(self.body.angle*-1)
        
        
#extra functions        
def determine_speed(velo_x, velo_y):
    return ((velo_x**2 + velo_y**2)**0.5)

def direction(velo_x, velo_y, obj):
    if (velo_x == 0 and velo_y > 0):
        return(math.pi/2)
    elif (velo_x == 0 and velo_y < 0):
        return(3*math.pi/2)
    elif (velo_x > 0 and velo_y == 0):
        return(0)
    elif (velo_x < 0 and velo_y == 0):
        return(math.pi)
    elif (velo_x>0 and velo_y > 0):
        return math.atan(velo_y/velo_x)
    elif (velo_x<0 and velo_y > 0):
        return (math.atan(velo_y/velo_x) + math.pi)
    elif (velo_x<0 and velo_y < 0):
        return (math.atan(velo_y/velo_x) + math.pi)
    elif (velo_x>0 and velo_y < 0):
        return (math.atan(velo_y/velo_x))
    #no movement base case
    else:
        if (obj == None):
            return 0
        return (obj.shape.body.angle)
    
    

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        