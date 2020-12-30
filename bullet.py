#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 14:22:08 2020

@author: luke
"""

import pyglet
import pymunk
import math
import resources
import physicalobject
import playertank

class Bullet(physicalobject.PhysicalObject):

    def __init__(self, x, y, velo_x, velo_y, angle, *args, **kwargs):
        super(Bullet, self).__init__(resources.bullet, *args, **kwargs)
        self.new_objects = []
        self.id = "bullet"
        self.dynamic = True
        self.mass = 0.1
        #bulletbody init
        self.image = resources.bullet
        self.id = "bullet"
        self.shape = pymunk.Poly.create_box(None, size=(self.image.width, self.image.height))
        self.moment = pymunk.moment_for_box(self.mass, (self.image.width, self.image.height))
        self.body = pymunk.Body(self.mass, self.moment)
        self.shape.body = self.body
        self.body.position = (x, y)
        self.body.velocity = (velo_x, velo_y)
        self.shape.body.angle = angle
        self.shape.id = "bullet"
        self.shape.dead = False
    
    def update(self, dt):
        super(Bullet, self).update(dt)
        #print(self.body.position.x, self.body.position.y)
        self.body.position.angle = physicalobject.direction(self.body.velocity.x, self.body.velocity.y, self)
        self.rotation = resources.degrees(self.shape.body.angle)*-1
        
        
    def die(self):
        self.dead = False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        