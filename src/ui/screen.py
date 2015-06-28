__author__ = 'Fernando'

import pygame


class Screen:

    def __init__(self, title, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.title = title

    def draw(self):
        pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.title)
