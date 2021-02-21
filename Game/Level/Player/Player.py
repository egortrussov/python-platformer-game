import pygame 
import math

from config.Constants import *

class Player:

    def __init__(self, window, x, y, camera_position):
        self.window = window
        self.x = x 
        self.y = y 
        self.height = PLAYER_HEIGHT 
        self.width = PLAYER_WIDTH
        self.camera_position = camera_position

        self.acceleration_y = 0
        self.acceleration_x = 0
        self.is_moving = False
        self.dir = 'right'
    
    def perform(self):

        new_x = self.x + self.acceleration_x 
        if (self.acceleration_x):
            res, limit = self.obstacles.check_collision(new_x, self.y, self.dir)
            if (res):
                self.x = new_x
            else:
                self.acceleration_x = 0 
                self.x = limit

        dir_y = 'up'
        if (self.acceleration_y > 0):
            dir_y = 'down'
        if (self.acceleration_y):
            new_y = self.acceleration_y + self.y 
            res, limit = self.obstacles.check_collision(self.x, new_y, dir_y)
            if (res):
                self.y = new_y
            else:
                self.y = limit
                self.acceleration_y = 0
        
        self.check_camera_movement()

        if (self.acceleration_x and not self.is_moving):
            if (self.acceleration_x > 0):
                self.acceleration_x = max(0, self.acceleration_x - 1)
            else:
                self.acceleration_x = min(0, self.acceleration_x + 1)

        self.draw()
    
    def draw(self):
        self.window.draw_rect(self.x - self.camera_position, self.y, self.width, self.height, [0, 255, 0])
    
    def check_camera_movement(self):
        x = self.x 
        if (x > CAMERA_OFFSET and x <= self.camera_position + CAMERA_OFFSET):
            new_position = self.move_camera(self.acceleration_x)
            self.camera_position = new_position 
        if (x >= self.camera_position + WIN_WIDTH - CAMERA_OFFSET):
            new_position = self.move_camera(self.acceleration_x)
            self.camera_position = new_position 
    
    def is_falling(self):
        y, height = self.y, self.height 

        res, limit = self.obstacles.check_collision(self.x, self.y, 'down')

        return res
    
    def check_falling(self):
        if (self.is_falling()):
            self.acceleration_y = min(10, self.acceleration_y + .5)
        else:
            if (self.acceleration_y > 0):
                self.acceleration_y = 0
    
    def jump(self):
        if (not self.is_falling()):
            self.acceleration_y = -10 
    
    def move(self, dir):
        if (dir == 'left'):
            self.acceleration_x = max(self.acceleration_x - 1, -10)
        if (dir == 'right'):
            self.acceleration_x = min(self.acceleration_x + 1, 10)
        self.dir = dir