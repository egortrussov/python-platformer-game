
import pygame
from config.Constants import *

class HintText:

    def __init__(self, window, text, font_size):
        self.text = text
        self.window = window
        self.font_size = font_size

        self.font = pygame.font.Font('fonts/joystix.ttf', font_size)
        self.padding = 10
    
    def display(self):
        mx_len = 0
        for line in self.text:
            mx_len = max(mx_len, len(line)) 
        
        rect_width = mx_len * (self.font_size ) + 20 
        rect_height = len(self.text) * (self.font_size + 3) + 20
        x = WIN_WIDTH - 10 - rect_width + self.padding 
        y = 10 + self.padding

        self.window.draw_rect(x - 10 - 5, y - self.padding - 5, rect_width + 6, rect_height + 6, [0, 0, 255])
        self.window.draw_rect(x - 10, y - self.padding, rect_width, rect_height, [0, 0, 0])

        for line in self.text:
            self.window.draw_text(x, y, line, self.font, [255, 255, 255])
            y += self.font_size + 3