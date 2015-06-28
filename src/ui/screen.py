__author__ = 'Fernando'

import pygame


class Screen:

    def __init__(self, title, screen_width, screen_height):
        self.__screen_width = screen_width
        self.__screen_height = screen_height
        self.__title = title

    def draw(self):
        pygame.display.set_mode((self.__screen_width, self.__screen_height))
        pygame.display.set_caption(self.__title)
