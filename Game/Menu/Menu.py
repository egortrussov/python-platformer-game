import pygame 

from Window.Window import *

class Menu:
    def __init__(self, window):
        self.window = window 
    
    def draw(self):
        self.window.draw_rect(100, 150, 50, 50, [255, 0, 0])
    
    def click(self, pos):
        x, y = pos 
        if (x < 300):
            return 0 
        return 1