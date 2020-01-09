# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim.Geography import *


class Map:
    """
    Map of the islands biography
    Makes a dictionary with coordinate tuples as key and instance classes
    as values
    """

    def __init__(self, area_type):
        self.o = Ocean()
        self.m = Mountain()
        self.d = Desert()
        self.s = Savannah()
        self.j = Jungle()
        self.area_type = area_type
        string = self.area_type.replace('\n', '')
        self.area_list = list(string)
        self.lines = len(self.area_type.split('\n'))
        self.rows = int(len(self.area_list) / self.lines)
        self.coordinates = [(x, y) for x in range(self.lines)
                            for y in range(self.rows)]
        self.cells = {}

    def create_map(self):
        for i in self.area_list:
            if i == 'O':
                self.area_list[i] = self.o
            elif i == 'M':
                self.area_list[i] == self.m
            elif i == 'D':
                self.area_list[i] = self.d
            elif i == 'S':
                self.area_list[i] = self.s
            else:
                self.area_list[i] = self.j

        for i in self.area_list:
            self.cells[self.coordinates[i]] = self.area_list[i]
        return self.cells


if __name__ == "__main__":
    map_string = """\
                  OOOOOOOOOOOOOOOOOOOOO
                  OOOOOOOOSMMMMJJJJJJJO 
                  OSSSSSJJJJMMJJJJJJJOO
                  OSSSSSSSSSMMJJJJJJOOO
                  OSSSSSJJJJJJJJJJJJOOO
                  OSSSSSJJJDDJJJSJJJOOO
                  OSSJJJJJDDDJJJSSSSOOO
                  OOSSSSJJJDDJJJSOOOOOO
                  OSSSJJJJJDDJJJJJJJOOO
                  OSSSSJJJJDDJJJJOOOOOO
                  OOSSSSJJJJJJJJOOOOOOO
                  OOOSSSSJJJJJJJOOOOOOO
                  OOOOOOOOOOOOOOOOOOOOO"""

    test_map = Map(map_string)
    print(test_map.create_map())
