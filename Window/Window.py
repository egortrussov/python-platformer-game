import pygame

class Window: 
    def __init__(self, WIN):
        self.WIN = WIN
    
    def draw_rect(self, x, y, wid, hei, color):
        pygame.draw.rect(self.WIN, color, [x, y, wid, hei])
    
    def draw_image(self, path, x, y, size_x, size_y):

        raw_sprite = pygame.image.load(path)
        sprite = pygame.transform.scale(raw_sprite, (size_x, size_y))

        self.WIN.blit(sprite, (x, y))