__author__ = 'Fernando'

import sys

from pygame.locals import *
from ui.screen import *

def main():
    pygame.init()
    screen = Screen('Territory', 800, 600)
    screen.draw()

    pygame.display.flip()

    # Initialize clock
    clock = pygame.time.Clock()

    # run the game loop
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                pass
            if event.type == KEYUP:
                pass
            pygame.display.flip()

main()
