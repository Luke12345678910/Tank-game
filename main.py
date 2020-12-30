#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:01:22 2020

@author: luke
"""

import pyglet
import pymunk
from pymunk.pyglet_util import DrawOptions
import math
import physicalobject
import playertank
import resources
import wall
import bullet
import room

#pymunk init
space = pymunk.Space()
space.gravity = 0, 0
options = DrawOptions()

#pyglet init
rooms = []
game_window = pyglet.window.Window(1400, 1000)
main_batch = pyglet.graphics.Batch()
resources.center_image(resources.tank_body)
resources.center_image(resources.bullet)
resources.center_image(resources.wallblock)
#roomsyikes

#startroom/////////////////////////////////////////////////////////////////////////////////////////////////////////////
start_room = room.Room()
rooms.append(start_room)
#playertank init
player_tank = playertank.PlayerTank(x=500, y=500, batch=main_batch)
player_tank.scale = 1
start_room.objects.append(player_tank)
player_tank.accel_speed = 300
player_tank.max_speed = 200
player_tank.turnspeed = .01
player_tank.rotation = math.pi*3/2
start_room.space.add(player_tank.shape, player_tank.body)
game_window.push_handlers(player_tank)
game_window.push_handlers(player_tank.key_handler)
#testwallinits
for i in range(57):
    test_wall = wall.WallBlock(x=25*i, y=0, batch=main_batch)
    start_room.space.add(test_wall.shape, test_wall.body)
    start_room.objects.append(test_wall)
for i in range(57):
    test_wall = wall.WallBlock(x=25*i, y=1000, batch=main_batch)
    start_room.space.add(test_wall.shape, test_wall.body)
    start_room.objects.append(test_wall)
for i in range(41):
    test_wall = wall.WallBlock(x=0, y=25*i, batch=main_batch)
    start_room.space.add(test_wall.shape, test_wall.body)
    start_room.objects.append(test_wall)
for i in range(41):
    test_wall = wall.WallBlock(x=1400, y=25*i, batch=main_batch)
    start_room.space.add(test_wall.shape, test_wall.body)
    start_room.objects.append(test_wall)

#collision response
def coll_begin(arbiter, space, data):
    return True

def coll_pre(arbiter, space, data):
    #bullet-wall
    if ((arbiter.shapes[0].id == "bullet" and arbiter.shapes[1].id == "wall") or (arbiter.shapes[1].id == "bullet" and arbiter.shapes[0].id == "wall")):
        if (arbiter.shapes[0].id == "bullet"):
            arbiter.shapes[0].dead = True
        if (arbiter.shapes[1].id == "bullet"):
            arbiter.shapes[1].dead = True
    return True

def coll_post(arbiter, space, data):
    pass



current_room = start_room
def update(dt):
    current_room.update(dt)
    handler = current_room.space.add_default_collision_handler()
    handler.begin = coll_begin
    handler.pre_solve = coll_pre
    handler.post_solve = coll_post
        
@game_window.event    
def on_mouse_motion(x, y, dx, dy):
    player_tank.mousex = x
    player_tank.mousey = y
    player_tank.turret_angle = physicalobject.direction(x-player_tank.x, y-player_tank.y, None)
    

@game_window.event
def on_mouse_press(x, y, button, modifiers):
    player_tank.fire(x, y)

@game_window.event
def on_draw():
    game_window.clear()
    #space.debug_draw(options)
    main_batch.draw()
    
if __name__ == '__main__':
    pyglet.clock.schedule_interval(update, 1/120.0)
    pyglet.app.run()
    
    