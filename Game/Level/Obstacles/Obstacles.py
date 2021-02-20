import pygame 

from Game.Level.Obstacles.get_obstacles import get_obstacles
from config.Constants import *

def intersect(l, r, l1, r1):
    return (min(r, r1) > max(l, l1))

class Obstacles:

    def __init__(self, window, level):
        self.window = window
        self.level = level 

        self.load_obstacles()
    
    def load_obstacles(self):
        self.obstacles = get_obstacles(self.level) 
    
    def perform(self):
        self.draw_obstacles()
    
    def draw_obstacles(self):
        for tile in self.obstacles:
            self.window.draw_rect(tile.x * TILE_SIZE, tile.y * TILE_SIZE, TILE_SIZE, TILE_SIZE, [0, 125, 25])
    
    def check_collision(self, x, y, dir):
        res = True

        if dir == 'right':
            xx = x + PLAYER_WIDTH 
            yy = y + PLAYER_HEIGHT 

            for tile in self.obstacles:
                tile_x = tile.x * TILE_SIZE 
                tile_y = tile.y * TILE_SIZE 
                if (tile_x < xx and tile_x + TILE_SIZE > xx) and intersect(y, yy, tile_y, tile_y + TILE_SIZE):
                    res = False
        
        if dir == 'left':
            xx = x + PLAYER_WIDTH 
            yy = y + PLAYER_HEIGHT 

            for tile in self.obstacles:
                tile_x = tile.x * TILE_SIZE 
                tile_y = tile.y * TILE_SIZE 
                if (tile_x + TILE_SIZE > x and tile_x < x) and intersect(y, yy, tile_y, tile_y + TILE_SIZE):
                    res = False

        if dir == 'down':
            xx = x + PLAYER_WIDTH 
            yy = y + PLAYER_HEIGHT 

            for tile in self.obstacles:
                tile_x = tile.x * TILE_SIZE 
                tile_y = tile.y * TILE_SIZE 
                if (tile_y < yy and tile_y + TILE_SIZE > yy) and intersect(x, xx, tile_x, tile_x + TILE_SIZE):
                    res = False
        
        if dir == 'up':
            xx = x + PLAYER_WIDTH 
            yy = y + PLAYER_HEIGHT 

            for tile in self.obstacles:
                tile_x = tile.x * TILE_SIZE 
                tile_y = tile.y * TILE_SIZE 
                if (tile_y + TILE_SIZE > y and tile_y < y) and intersect(x, xx, tile_x, tile_x + TILE_SIZE):
                    res = False
        

        return res