
class Tile:

    def __init__(self, x, y, type):
        self.x = x
        self.y = y 
        self.type = type

def get_obstacles(level):

    if level == 0:
        return [
            Tile(18, 17, 'solid'),
            Tile(18, 16, 'solid'),
            Tile(17, 17, 'solid'),
            Tile(16, 17, 'solid'),
        ]