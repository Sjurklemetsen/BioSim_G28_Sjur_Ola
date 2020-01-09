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

    pop_count = 0
    @classmethod
    def add_population(cls):
        cls.pop_count += 1

    def __init__(self):
        self.o = Geography.Ocean()
        self.m = Geography.Mountain()
        self.d = Geography.Desert()
        self.s = Geography.Savannah()
        self.j = Geography.Jungle()

    def create_map(self):
        string = area_type.replace('\n', '')
        area_list = list(string)
        lines = len(area_type.split('\n'))
        rows = int(len(area_list) / lines)
        coordinates = [(x, y) for x in range(lines) for y in range(rows)]

        for i in area_list:
            if i == 'O':
                area_list[i] = self.o
            elif i == 'M':
                area_list[i] == self.m
            elif i == 'D':
                area_list[i] = self.d
            elif i == 'S':
                area_list[i] = self.s
            else:
                area_list[i] = self.j

        self.cells = {}
        for i in area_list:
            self.cells[coordinates[i]] = area_list[i]

    def add_population(self):








