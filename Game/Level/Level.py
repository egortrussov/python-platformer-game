import pygame 

class Level:
    def __init__(self, window, number):
        self.window = window 
        self.number = number
    
    def draw(self):
        self.window.draw_rect(320, 120)