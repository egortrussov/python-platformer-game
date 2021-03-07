
from config.Constants import *

class Weed:
    
    def __init__(self, window, x, y):
        self.window = window 
        self.sprite = 'sprites/bonuses/weed_1.png' 
        self.x = x
        self.y = y

        self.collected = False 
        self.width = self.height = TILE_SIZE + 10  
        self.max_animation_frames = 2 
        self.frame = 1
        self.render_num = 1

    def draw(self, camera_position):
        if (not self.collected):
            self.window.draw_image(self.sprite, self.x * TILE_SIZE - 5 - camera_position, self.y * TILE_SIZE - 10, self.width, self.height)

            self.render_num += 1 

            if (self.render_num >= 30):
                self.frame += 1 
                if (self.frame > self.max_animation_frames):
                    self.frame = 1 
                path_1 = list(self.sprite) 
                path_1[-5] = str(self.frame)
                self.sprite = "".join(path_1)
                self.render_num = 0
        
        