
from Game.Level.Obstacles.levels_layouts.level_1 import layout_1

class Tile:

    def __init__(self, x, y, type):
        self.x = x
        self.y = y 
        self.type = type

def get_obstacles(level):

    
    obstacles = []
    level_data = None

    if level == 0:

        level_data = layout_1

    for row in range(len(level_data)):
        for col in range(len(level_data[row])):
            tile = level_data[row][col]
            if (tile == '#'):
                obstacles.append(Tile(col, row, 'solid'))
    
    return obstacles
