#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 23:04:00 2020

@author: luke
"""

import pyglet
import physicalobject
from pyglet.window import key
import resources
import math
import bullet
import pymunk

class PlayerTank(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super().__init__(img=resources.tank_body, *args, **kwargs)
        #basic init
        self.key_handler = key.KeyStateHandler()
        self.new_objects = []
        #turret handlers
        self.tank_turret = pyglet.sprite.Sprite(img=resources.tank_turret, *args, **kwargs)
        self.turret_angle = 0
        self.mousex = 0
        self.mousey = 0
        self.bullet_speed = 500
        #stats
        self.accel_speed = 0
        self.turnspeed = 0
        self.decel_speed = 3
        self.turn_decel_speed = 0.8
        self.mass = 1
        #tankbody init
        self.dynamic = True
        self.image = resources.tank_body
        self.id = "playertank"
        self.angle = 0
        self.shape = pymunk.Poly.create_box(None, size=(self.image.width, self.image.height))
        self.moment = pymunk.moment_for_box(self.mass, (self.image.width, self.image.height))
        self.body = pymunk.Body(self.mass, self.moment)
        self.shape.elasticity = 0
        self.shape.body = self.body
        self.shape.body.position = 500, 500
        self.shape.body.angle = math.pi*3/2
        self.shape.body.friction = 1000
        #useful new stuff for collisions
        self.shape.id = "bullet"
        self.shape.dead = False
        
        
    def update(self, dt):
        super(PlayerTank, self).update(dt)
        #driving handles
        self.turret_angle = physicalobject.direction(self.mousex-self.x, self.mousey-self.y, self.tank_turret)
        if self.key_handler[key.W]:
            self.shape.body.apply_force_at_world_point((math.cos(self.body.angle)*self.accel_speed, math.sin(self.body.angle)*self.accel_speed), (self.body.position.x, self.body.position.y)) 
        elif self.key_handler[key.S]:
            self.shape.body.apply_force_at_world_point((-1*math.cos(self.body.angle)*self.accel_speed, -1*math.sin(self.body.angle)*self.accel_speed), (self.body.position.x, self.body.position.y)) 
        if self.key_handler[key.A]:
            self.body.angle += math.radians(self.turnspeed*physicalobject.determine_speed(self.body.velocity.x, self.body.velocity.y))
        if self.key_handler[key.D]:
            self.body.angle -= math.radians(self.turnspeed*physicalobject.determine_speed(self.body.velocity.x, self.body.velocity.y))
        #decel
        self.shape.body.apply_force_at_world_point((math.cos(physicalobject.direction(self.body.velocity.x, self.body.velocity.y, self))*self.decel_speed*physicalobject.determine_speed(self.body.velocity.x, self.body.velocity.y)*-1, math.sin(physicalobject.direction(self.body.velocity.x, self.body.velocity.y, self))*self.decel_speed*physicalobject.determine_speed(self.body.velocity.x, self.body.velocity.y)*-1), (self.body.position.x, self.body.position.y)) 
        #angular momentum decel
        self.shape.body.angular_velocity *= self.turn_decel_speed
        #turret image control
        self.tank_turret.rotation = resources.degrees(self.turret_angle)*-1
        self.tank_turret.x = self.x
        self.tank_turret.y = self.y
        
        
        
    def fire(self, mousex, mousey):
        bullet_x = self.body.position.x + math.cos(self.turret_angle)*59
        bullet_y = self.body.position.y + math.sin(self.turret_angle)*59
        velo_x = math.cos(self.turret_angle)*self.bullet_speed+self.body.velocity.x
        velo_y = math.sin(self.turret_angle)*self.bullet_speed+self.body.velocity.y
        angle = physicalobject.direction(velo_x, velo_y, self)
        new_bullet = bullet.Bullet(x=bullet_x, y=bullet_y, velo_x = velo_x, velo_y = velo_y, angle = angle, batch=self.batch)
        self.new_objects.append(new_bullet)
        
    def die(self):
        pass
        
        
    
            
            
            
            