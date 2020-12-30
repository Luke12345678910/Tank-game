#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 18:43:08 2020

@author: luke
"""

import pyglet
import pymunk
import math
import resources

class Room():
    
    def __init__(self):
        self.objects = []
        self.space = pymunk.Space()
        self.space.gravity = 0, 0
        
    def update(self, dt):
        self.space.step(dt)
        for obj in self.objects:
            obj.update(dt)
            self.objects.extend(obj.new_objects)
            for obj2 in obj.new_objects:
                self.space.add(obj2.body, obj2.shape)
            obj.new_objects = []
                    
        for to_remove in [obj for obj in self.objects if obj.dead]:
            to_remove.delete()
            self.objects.remove(to_remove)
            self.space.remove(to_remove.body, to_remove.shape)