# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim.Geography import *


class Map:
    """
    Map of the islands biography containing all the cells from Geography
    Makes a dictionary with coordinate tuples as key and instance classes
    as values
    """

    def __init__(self):
        self.map_dict = {}

    def create_map(self, area_type):
        string = area_type.replace('\n', '')
        string.replace(' ', '')
        area_list = list(string)
        rows = len(area_type.split('\n'))
        cols = int(len(area_list) / rows)
        coordinates = [(x, y) for x in range(rows) for y in range(cols)]

        for ind, val in enumerate(area_list):
            if val == 'O':
                area_list[ind] = Ocean()
            elif val == 'M':
                area_list[ind] = Mountain()
            elif val == 'D':
                area_list[ind] = Desert()
            elif val == 'S':
                area_list[ind] = Savannah()
            else:
                area_list[ind] = Jungle()

        for ind, val in enumerate(area_list):
            self.map_dict[coordinates[ind]] = area_list[ind]
        return self.map_dict

    def check_string(self, string):
        """
        Check if the string input is one of the allowed categories
        Check if the edges at the map is ocean
        Check if the map is a square
        """
        accepted_landscape = ["J", "S", "D", "M", "O"]
        for row in string:
            for cell in row:
                if cell not in accepted_landscape:
                    raise ValueError(' That is an invalid landscape')
        pass

    def populate_map(self, population):
        """
        A method that populate the map with animals in each cell
        :return:
        """
        pass

    def find_cell(self, cell_to_find):
        """
        for cell in map:
            if cell_to find == cell:
        """
        pass

    def move_animals(self):
        """
        Move the animals to a different cell
        :return:
        """
        pass

    def annual_cycle(self):
        """
        An annual cycle on the map where every cell and animal on
        the map goes through yearly changes
        1) Fodder grow
        2) Animal eat
        3) Procreation
        4) Migration
        5) Aging
        6) Loss of weight
        7) Death
        :return:
        """
        pass


if __name__ == "__main__":
    area_type = '''OOOOOOOOOOOOOOOOOOOOO
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
OOOOOOOOOOOOOOOOOOOOO'''
    print(Map().create_map(area_type))
