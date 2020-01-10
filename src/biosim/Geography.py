# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim.Fauna import *


class Geography:
    """
    A class that contain cell with a certain area type and with an animal
    inside it
    """

    def __init__(self):
        self.herbivores = []
        self.carnivores = []
        self.f_max = None


class Ocean(Geography):
    """
    A Ocean. No fodder and no animals are allowed to move here
    Ocean cell types are passive in this simulation
    """

    def __init__(self):
        super().__init__(self)
    pass


class Mountain:
    """
    A Mountain cell. No fodder and no animals are allowed to move here
    Mountain cell types are passive in this simulation
    """
    f_max = None

    def __init__(self):
        super().__init__(self)
        pass
    pass


class Desert(Geography):
    """
    Area type that holds no fodder, but animals can inhabit the cells
    """

    def __init__(self):
        super().__init__(self)
        pass
    pass


class Savannah(Geography):
    """
    A savannah cell that holds fodder, but can suffer overgrazing
    """

    def __init__(self):
        super().__init__(self)
        self.f_max = 300
        self.alpha = 0.3

    def fodder_growth(self):
        """
        Fodder growth for savannah
        :return:
        """


class Jungle(Geography):
    """
    A jungle cell where carnivore can hunt herbivore and herbivore can eat food
    Fodder replenish each year to f_max.
    """

    def __init__(self, fodder):
        self.f_max = 800
        self.fodder = self.f_max

    def add_animal(self):
        self.herbivores.append(Herbivore())
        self.carnivores.append(Carnivore())

    def fodder_growth(self):
        """
        Replenishes fodder each year
        :return:
        """
        self.fodder = self.f_max

    def fodder_eaten(self, fodder_eaten):
        """
        A method that removes the fodder that gets eaten by the animals
        :return:
        """
        self.fodder -= fodder_eaten

    def fodder_amount(self):
        return self.fodder

    def check_herb_pop(self):
        """
        Check how many animals that currently are residing in this jungle cell
        """
        return len(self.herbivores)

    def check_carn_pop(self):
        return len(self.carnivores)

    def remove_animals(self):
        """
        This method removes a the dead animals from a cell
        :return:
        """
        for animal in self.herbivores:
            if animal.check_death():
                self.herbivores.pop(animal)
        for animal in self.carnivores:
            if animal.check_death():
                self.carnivores.pop(animal)
