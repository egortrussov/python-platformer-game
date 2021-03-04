import pygame

class Window: 
    def __init__(self, WIN):
        self.WIN = WIN
    
    def draw_rect(self, x, y, wid, hei, color):
        pygame.draw.rect(self.WIN, color, [x, y, wid, hei])
    
    def draw_image(self, path, x, y, size_x, size_y, flip_hor = False):

        raw_sprite = pygame.image.load(path)
        sprite = pygame.transform.scale(raw_sprite, (size_x, size_y))

        if (flip_hor):
            sprite = pygame.transform.flip(sprite, True, False)

        self.WIN.blit(sprite, (x, y))
    
    def draw_text(self, x, y, text, font, color):
        text_to_display = font.render(text, 1, color) 
        self.WIN.blit(text_to_display, (x, y))