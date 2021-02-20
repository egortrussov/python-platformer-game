import pygame

class Window: 
    def __init__(self, WIN):
        self.WIN = WIN
    
    def draw_rect(self, x, y):
        pygame.draw.rect(self.WIN, [255, 0, 0], [x, y, 60, 60])