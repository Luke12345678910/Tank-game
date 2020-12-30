#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 12:23:10 2020

@author: luke
"""

import pyglet
import pymunk
import math
import resources
import physicalobject

class WallBlock(physicalobject.PhysicalObject):

    def __init__(self, x, y, *args, **kwargs):
        super().__init__(img=resources.bigbluewall, *args, **kwargs)
        #basic init
        self.new_objects = []
        self.image = resources.wallblock
        self.dynamic = False
        self.id = "wall"
        #stats
        self.mass = -1 #infinite
        #wallbody init
        self.shape = pymunk.Poly.create_box(None, size=(self.image.width, self.image.height))
        self.body = pymunk.Body(body_type = pymunk.Body.STATIC)
        self.shape.body = self.body
        self.shape.body.position = x, y
        self.shape.body.angle = 0
        self.shape.elasticity = 0
        self.shape.friction = 1000
        #sprite binding
        self.x = self.body.position.x
        self.y = self.body.position.y
        self.rotation = math.degrees(self.body.angle*-1)
        self.shape.id = "wall"
        self.shape.dead = False
        
    def update(self, dt):
        super(WallBlock, self).update(dt)
        
    def die(self):
        pass