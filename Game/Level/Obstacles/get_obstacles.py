import random

from Game.Level.Obstacles.levels_layouts.level_1 import layout_1

from config.Constants import *

class Tile:

    def __init__(self, x, y, type, path, rot_angle, is_animated, max_animation_frames):
        self.x = x
        self.y = y 
        self.type = type
        self.path = path 
        self.rot_angle = rot_angle
        self.is_animated = is_animated
        self.max_animation_frames = max_animation_frames

        self.animation_step = 1
        self.display_number = 0
    
    def draw(self, window, camera_position):

        if (self.is_animated):
            path_1 = list(self.path) 
            path_1[-5] = str(self.animation_step)
            self.path = "".join(path_1)

        window.draw_image(self.path, self.x * TILE_SIZE - camera_position, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

        if (self.is_animated):
            self.display_number += 1 
            if (self.display_number >= 10):
                self.animation_step += 1 
                if (self.animation_step > self.max_animation_frames):
                    self.animation_step = 1
                self.display_number = 0 


def get_obstacles(level):

    
    obstacles = []
    level_data = None

    if level == 0:

        level_data = layout_1
    
    dirt_sprites = ['sprites/tiles/dirt.png', 'sprites/tiles/grass.png']

    for row in range(len(level_data)):
        for col in range(len(level_data[row])):
            tile = level_data[row][col]
            if (tile == '#'):
                inx = 1
                if (row and level_data[row - 1][col] == '#'):
                    inx = 0
                elif (row and level_data[row - 1][col] == ' '):
                    if (random.randint(0, 3) <= 2):
                        obstacles.append( Tile(col, row - 1, 'decoration', 'sprites/decoration/grass_1.png', 0, True, 2) )
                 
                if (row < TILES_VER - 1 and level_data[row + 1][col] == ' '):
                    if (random.randint(0, 3) <= 2):
                        obstacles.append( Tile(col, row + 1, 'decoration', 'sprites/decoration/dirt_stalagmite.png', 0, False, 0) )
                
                obstacles.append( Tile(col, row, 'solid', dirt_sprites[inx], 0, False, 0) )
    
    return obstacles
