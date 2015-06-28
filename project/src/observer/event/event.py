__author__ = 'Fernando'

from src.observer.observable import *


class Event(Observable):

    def __init__(self):
        super(Event, self).__init__()
