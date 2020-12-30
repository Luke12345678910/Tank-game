#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 00:03:20 2020

@author: luke
"""

import pyglet
import math

#image inits
tank_body = pyglet.resource.image("tank_body.png")
tank_turret = pyglet.resource.image("tank_turret.png")
bullet = pyglet.resource.image("bullet.png")
bigbluewall = pyglet.resource.image("bigbluewall.png")
wallblock = pyglet.resource.image("wallblock.png")
tank_turret.anchor_x = 17
tank_turret.anchor_y = tank_turret.height/2
def center_image(image):
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2
    
    
#random functions
def degrees(rad):
    return (rad*180/math.pi)

def radians(deg):
    return (deg*math.pi/180)

#vectors(not used?)
class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def normalize(self):
        magnitude = self.magnitude()
        self.x = self.x/magnitude
        self.y = self.y/magnitude
        return 1
    
    def dot(self, vect2):
        return (self.x*vect2.x + self.y*vect2.y)
    
    def __str__(self):
        return ("(" + str(self.x) + "," + str(self.y) + ")")
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    