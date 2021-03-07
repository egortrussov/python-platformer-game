import random

from Game.levels.level_1.level_1_layout import *
from Game.Level.Obstacles.Tile.Tile import *
from Game.Level.Obstacles.tiles_data import tiles_data

from Game.Bonuses.Weed import *

from config.Constants import *

def get_obstacles(window, level):

    
    obstacles = []
    decoration = []
    bonuses = []
    level_data = None

    if level == 0:

        level_data = layout_1
    
    dirt_sprites = ['sprites/tiles/dirt.png', 'sprites/tiles/grass.png']

    for row in range(len(level_data)):
        for col in range(len(level_data[row])):
            tile = level_data[row][col]
            if (tile == '#'):
                choice = 'grass_block'
                if (row and level_data[row - 1][col] == '#'):
                    choice = 'dirt_block'
                elif (row and level_data[row - 1][col] == ' '):
                    if (random.randint(0, 3) <= 2):
                        data = tiles_data['grass']
                        decoration.append( Tile(col, row - 1, data.type, data.sprite, 0, data.is_animated, data.max_animation_frames) )
                    else:
                        bonuses.append(Weed(window, col, row - 1))
                        data = tiles_data['grass']
                        decoration.append( Tile(col, row - 1, data.type, data.sprite, 0, data.is_animated, data.max_animation_frames) )
                 
                if (row < TILES_VER - 1 and level_data[row + 1][col] == ' '):
                    if (random.randint(0, 3) <= 2):
                        data = tiles_data['dirt_stalagmites']
                        decoration.append( Tile(col, row + 1, data.type, data.sprite, 0, data.is_animated, data.max_animation_frames) )
                data = tiles_data[choice]
                obstacles.append( Tile(col, row, data.type, data.sprite, 0, data.is_animated, data.max_animation_frames) )
    
    return obstacles, decoration, bonuses
