import pygame 
import math

from config.Constants import *

class Player:

    def __init__(self, window, x, y):
        self.window = window
        self.x = x 
        self.y = y 
        self.height = PLAYER_HEIGHT 
        self.width = PLAYER_WIDTH

        self.acceleration_y = 0
        self.acceleration_x = 0
        self.is_moving = False
    
    def perform(self):
        self.x += self.acceleration_x 
        self.y += self.acceleration_y 

        if (self.acceleration_x and not self.is_moving):
            if (self.acceleration_x > 0):
                self.acceleration_x = max(0, self.acceleration_x - 1)
            else:
                self.acceleration_x = min(0, self.acceleration_x + 1)

        self.draw()
    
    def draw(self):
        self.window.draw_rect(self.x, self.y, self.width, self.height, [0, 255, 0])
    
    def is_falling(self):
        y, height = self.y, self.height 
        bottom_pos = y + height  

        return bottom_pos < WIN_HEIGHT
    
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
        print(dir)
        if (dir == 'left'):
            self.acceleration_x = max(self.acceleration_x - 1, -10)
        if (dir == 'right'):
            self.acceleration_x = min(self.acceleration_x + 1, 10)
        print(self.acceleration_x)