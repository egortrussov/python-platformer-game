import pygame 

from Game.Game import *
 
from config.Constants import * 
from Window.Window import * 
 

pygame.init()

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption('Super trash bros')

window = Window(WIN)

def main():
    run = True 
    clock = pygame.time.Clock() 

    game = Game(window)

    while (run):
        pygame.time.delay(10)
        WIN.fill([0, 0, 0])

        events = pygame.event.get()
        keys = pygame.key.get_pressed()

        clock.tick(FPS)

        for e in events:
            if (e.type == pygame.QUIT):
                exit()
        
        game.check_events(events)
        game.check_keys(keys)

        game.draw_scene()

        pygame.display.flip()

        pygame.display.update()

        pass 

main()