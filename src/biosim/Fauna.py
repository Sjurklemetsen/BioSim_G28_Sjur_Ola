# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

import numpy as np


class Fauna:
    """
    Class for all the animals in the fauna.
    """
    @classmethod
    def birth_weight(cls):
        return np.random.normal(cls.w_birth, cls.sigma_birth)

    def __init__(self):
        self.age = 0
        self.weight = self.birth_weight()

    def age(self):
        """
        Age og the animals increase by one for each year
        :return:
        """
        self.age += 1

    def weight_decrease(self):
        """
        The weight of the animal decrease for each year
        :return:
        """
        return self.eta * self.weight

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
    w_birth = 8.0
    sigma_birth = 1.5
    beta = 0.9
    eta = 0.05
    a_half = 40.0
    phi_age = 0.2
    w_half = 10.0
    phi_weight = 0.1
    mu = 0.25
    lamda = 1.0
    gamma = 0.2
    zeta = 3.5
    xi = 1.2
    omega = 0.4
    F = 10.0

    def __init__(self):
        pass
        super().__init__(self)
        pass

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
    w_birth = 6.0
    sigma_birth = 1.0
    beta = 0.75
    eta = 0.125
    a_half = 60.0
    phi_age = 0.4
    w_half = 4.0
    phi_weight = 0.4
    mu = 0.4
    lamda = 1.0
    gamma = 0.8
    zeta = 3.5
    xi = 1.1
    omega = 0.9
    F = 50.0
    DeltaPhiMax = 10.0

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


