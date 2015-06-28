__author__ = 'Fernando'

from observer.observable import *


class Event(Observable):

    def __init__(self):
        super(Event, self).__init__()
