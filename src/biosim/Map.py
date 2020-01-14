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
    def __init__(self, area_type):
        self.map_dict = self.create_map(area_type)

    def create_map(self, area_type):
        """
        A method that makes the map containing many cells that contain a
        geography instance with animals
        - Check if all edges are area type ocean.
        - Raise ValueError if you type something else then allowed letters
        :param: List
        :return: Dict
        """
        string = area_type.replace('\n', '')
        area_list = list(string)
        lines = len(area_type.split('\n'))
        rows = int(len(area_list) / lines)
        coordinates = [(x, y) for x in range(lines) for y in range(rows)]

        for i in area_list:
            if i == 'O':
                area_list[i] = Ocean()
            elif i == 'M':
                area_list[i] = Mountain()
            elif i == 'D':
                area_list[i] = Desert()
            elif i == 'S':
                area_list[i] = Savannah()
            else:
                area_list[i] = Jungle()

        for i in area_list:
            self.map_dict[coordinates[i]] = area_list[i]
        return self.map_dict



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
    #print(test_map.create_map())
