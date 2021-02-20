import pygame 
from config.Constants import *

from Game.Menu.Menu import *
from Game.Level.Level import *

class Game: 
    def __init__(self, window):
        self.window = window

        self.is_menu = True 
        self.level = None 
        self.scene = Menu(window)
    
    def draw_scene(self):

        if (self.is_menu):
            self.scene.draw()
            return True
        else:
            self.scene.perform()
    
    def check_events(self, events):

        if (self.is_menu):
            for e in events:
                if (e.type == pygame.MOUSEBUTTONDOWN):
                    pos = pygame.mouse.get_pos()

                    level = self.scene.click(pos)

                    self.level = level
                    self.is_menu = False 
                    self.scene = Level(self.window, level)

    def check_keys(self, keys):

        if (self.level != None):
            self.scene.check_keys(keys)
        pass
