# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim.Geography import *
import math
import random as rd


class Map:
    """
    Map of the islands biography containing all the cells from Geography
    Makes a dictionary with coordinate tuples as key and instance classes
    as values
    """

    def __init__(self):
        self.map_dict = {}


    def create_map(self, area_type):
        for line in area_type:
            line.replace(' ', '')
            line.replace('\n', '')
        self.check_string(area_type)

        area_list = list(area_type)
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

    """def check_string(self, string):

        Check if the string input is one of the allowed categories
        Check if the edges at the map is ocean
        Check if the map is a square

        accepted_landscape = ["J", "S", "D", "M", "O"]
        for row in string:
            for cell in row:
                if cell not in accepted_landscape:
                    raise ValueError(' That is an invalid landscape')


        bot_right = max(self.map_dict.keys())
        top_left = min(self.map_dict.keys())

        for coord, cell in self.map_dict.items():
            if coord[0] == top_left[0] or coord[1] == top_left[1]
                if type(cell).__name__ != "Ocean":
                    raise ValueError('The border of the map must be ocean')
            elif coord[0] == bot_right[0] or coord[1] == bot_right[1]:
                if type(cell).__name__ != "Ocean":
<<<<<<< HEAD
                    raise ValueError('The border of the map cannot be ocean')
"""
=======
                    raise ValueError('The border of the map must be ocean')
            else:
                continue


        for row in range(self.rows):
            for line in string





>>>>>>> Map_branch

    def populate_map(self, coordinates, population):
        """
        A method that populate the map with animals in each cell
        :return:
        """
        self.map_dict[coordinates].populate_cell(population)

    def find_cell(self, cell_to_find):
        """
        for cell in map:
            if cell_to find == cell:
        """
        pass

    @staticmethod
    def find_neighbor_cells(position):
        """
        Method to find the neighbouring cells of a position
        :param position: Tuple
        :return: List
        """
        neighbours = [(position[0] + 1, position[1]),  # S
                      (position[0] - 1, position[1]),  # N
                      (position[0], position[1] + 1),  # Ø
                      (position[0], position[1] - 1)]  # V
        return neighbours

    def migrate_to(self, position):
        """
        Calculates which neighbour cell animal migrates to
        :return: tuple
        """
        neigh = self.find_neighbor_cells(position)
        propensity_list = []
        for cell in neigh:
            propensity_list.append(self.map_dict[cell].propensity_herb())
        if sum(propensity_list) == 0:
            return position

        print(propensity_list)
        sum_propen = sum(propensity_list)
        print(sum_propen)
        p = []
        for prop in propensity_list:
            p.append(prop / sum_propen)

        print(p)

        coord_prob = []
        for x, y in zip(neigh, p):
            coord_prob.append((x, y))

        prob = sorted(coord_prob, key=lambda pro: pro[1])
        print(prob)
        a = rd.random()
        if a <= prob[0][1]:
            return prob[0][0]
        elif prob[0][1] < a <= prob[1][1]:
            return prob[1][0]
        elif prob[1][1] < a <= prob[2][1]:
            return prob[2][0]
        else:
            return prob[3][0]

        # Noe feil med sannsynlighets testen

    def move(self):
        """
        The animals move from one cell to another
        :return:
        """
        for loc, cell in self.map_dict.items():
            if cell.animals_here:
                moving_animals = cell.check_migration()
                for animal in moving_animals:
                    if animal.animal_moved is not True:
                        new_cell = self.migrate_to(loc)
                        self.map_dict[new_cell].add_animal(animal)
                        animal.animal_moved = True
                cell.remove_animals(moving_animals)
            else:
                continue

        for loc, cell in self.map_dict.items():
            for animal in cell.pop_total:
                animal.animal_moved = False

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
        for coord, land in self.map_dict.items():
            land.fodder_growth()
            land.herbivore_eat()
            land.carnivore_eat()
            land.animal_mating()
            land.move()
            land.age_weightloss()
            land.animal_die()


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

    pos = (2, 6)
    m = Map()
    m.create_map(area_type)
    m.populate_map((2, 7), [Herbivore()for _ in range(5)])
    print(m.find_neighbor_cells(pos))
    print(m.migrate_to(pos))
    m.move

