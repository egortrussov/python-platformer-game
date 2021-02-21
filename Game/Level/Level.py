import pygame 

from Game.Level.Player.Player import *
from Game.Level.Obstacles.Obstacles import *

class Level:
    def __init__(self, window, number):
        self.window = window 
        self.number = number
        self.player = Player(window, 50, 200, 0)

        self.obstacles = Obstacles(window, number, 0) 
        self.player.obstacles = self.obstacles
        self.camera_position = 0

        self.player.move_camera = self.move_camera
    
    def perform(self):

        self.player.check_falling()

        self.obstacles.perform()

        self.draw()
    
    def draw(self):
        self.player.perform()
    
    def check_keys(self, keys):
        if (keys[pygame.K_UP]):
            self.player.jump()
        if (keys[pygame.K_LEFT]):
            self.player.is_moving = True
            self.player.move('left')
        elif (keys[pygame.K_RIGHT]):
            self.player.is_moving = True 
            self.player.move('right')
        else:
            self.player.is_moving = False
    
    def move_camera(self, delta):
        self.camera_position = max(0, self.camera_position + delta) 

        self.obstacles.camera_position = self.camera_position

        return self.camera_position 