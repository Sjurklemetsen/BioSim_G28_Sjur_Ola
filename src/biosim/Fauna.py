# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'


class Fauna:
    """
    Class for all the animals in the fauna.
    """
    def __init__(self):
        pass

    def age(self):
        """
        Age og the animals increase by one for each year
        :return:
        """
        pass

    def weight_decrease(self):
        """
        The weight of the animal decrease for each year
        :return:
        """

    def fitness(self):
        """
        The fitness of the animal
        :return:
        """

    def migration(self):
        """
        The animal are moving to another cell each year if it meets certain
        fitness levels and if its enough fodder in the neighbour cells
        :return:
        """
        pass

    def birth(self):
        """
        An animal can give birth to a child if all the conditions are met
        :return:
        """
        pass

    def death(self):
        """
        An animal dies if its fitness is equal to zero or worth a certain
        probability
        :return:
        """
        pass


class Herbivore(Fauna):
    def __init__(self):
        super().__init__(self)

    def eat(self):
        """
        The herbivore is eating if its placed in a jungle or savannah cell
        The fodder decrease when a animale eat
        :return:
        """


    def new_ground(self):
        """
        Herbivores move to a cell with more food and depending on their fitness
        :return:
        """
        pass


class Carnivore(Fauna):
    def __init__(self):
        super().__init__(self)

    def eat(self):
        """
        The weight of the animal increase every time the animal eat
        The amount of herbivores decrease if a carnivore eats
        :return:
        """
        pass

    def new_ground(self):
        """
        Where the new cell is depends on fitness and the amount of herbivores
        :return:
        """


