import pygame

class Window: 
    def __init__(self, WIN):
        self.WIN = WIN
    
    def draw_rect(self, x, y, wid, hei, color):
        pygame.draw.rect(self.WIN, color, [x, y, wid, hei])