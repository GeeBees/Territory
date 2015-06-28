__author__ = 'Fernando'


class ElementList(object):

    def __init__(self):
        self.__elements = []

    def add_element(self, e):
        self.__elements.append(e)

    def __len__(self):
        return len(self.__elements)

    def __iter__(self):
        for e in self.__elements:
            yield e
