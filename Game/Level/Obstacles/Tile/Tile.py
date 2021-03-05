
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
