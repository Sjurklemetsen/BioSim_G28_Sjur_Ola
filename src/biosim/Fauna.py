# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

import math
import random as rd
import numpy as np


class Fauna:
    """
    Class for an animal in the fauna
    """
    parameters = {
        'w_birth': None,
        'sigma_birth': None,
        'beta': None,
        'eta': None,
        'a_half': None,
        'phi_age': None,
        'w_half': None,
        'phi_weight': None,
        'mu': None,
        'landa': None,
        'gamma': None,
        'zeta': None,
        'xi': None,
        'omega': None,
        'F': None,
        'DeltaPhiMax': None
    }

    def __init__(self, age=None, weight=None):
        self.age = age
        self.weight = weight
        self.fitness = 0
        self.update_fitness()

        if age is None:
            self.age = 0
        if weight is None:
            self.weight = np.random.normal(self.w_birth, self.sigma_birth)

    def aging(self):
        """
        Age og the animals increase by one for each year
        :return:
        """
        self.age += 1
        self.update_fitness()

    def weight_decrease(self):
        """
        The weight of the animal decrease for each year
        :return:
        """
        self.weight -= self.eta * self.weight
        self.update_fitness()

    def update_fitness(self):
        """
        Update the fitness of an animal based on the new age and weight
        :return:
        """
        if self.weight <= 0:
            self.fitness = 0
        else:
            self.fitness = (1 / (1 + math.exp(
                self.phi_age * (self.age - self.a_half))) * 1 / (
                    1 / (1 + math.exp(
                        - self.phi_weight(self.weight - self.w_half)))
                            ))

    def check_death(self):
        """
        Function that checks if the animal is dead or not
        :return: Boolean expression
        """
        if self.fitness == 0:
            return True
        elif rd.random() < self.omega * (1 - self.fitness):
            return True
        else:
            return False

    def check_migration(self):
        """
        Method that check if the animal is ready to move to another cell
        :return: Boolean expression
        """
        prob_move = self.mu * self.fitness
        return rd.random() < prob_move

    def check_birth(self, n_animals):
        """
        A Method that check if an animal is ready to give birth or not
        :param n_animals:
        :return: Boolean expression
        """
        probability = min(1, self.gamma * self.fitness * (n_animals - 1))

        if self.weight < self.zeta * (self.w_birth + self.sigma_birth):
            return False
        if rd.random() <= probability:
            return True
        else:
            return False


class Herbivore(Fauna):
    parameters = {
        "w_birth": 8.0,
        "sigma_birth": 1.5,
        "beta": 0.9,
        "eta": 0.05,
        "a_half": 40.0,
        "phi_age": 0.2,
        "w_half": 10.0,
        "phi_weight": 0.1,
        "mu": 0.25,
        "lambda": 1.0,
        "gamma": 0.2,
        "zeta": 3.5,
        "xi": 1.2,
        "omega": 0.4,
        "F": 10.0,
    }

    def __init__(self, age=None, weight=None):
        super().__init__(self)
        pass
    pass

    def eat(self, fodder):
        """
        The herbivore is eating if its placed in a jungle or savannah cell
        The fodder decrease when a animal eat
        weight update
        :return:
        """

        "self.weight += self.beta *"
        pass


class Carnivore(Fauna):
    parameters = {
        "w_birth": 6.0,
        "sigma_birth": 1.0,
        "beta": 0.75,
        "eta": 0.125,
        "a_half": 60.0,
        "phi_age": 0.4,
        "w_half": 4.0,
        "phi_weight": 0.4,
        "mu": 0.4,
        "lambda": 1.0,
        "gamma": 0.8,
        "zeta": 3.5,
        "xi": 1.1,
        "omega": 0.9,
        "F": 50.0,
        "DeltaPhiMax": 10.0
    }

    def __init__(self, age=None, weight=None):
        super().__init__(self)
        self.age = age
        self.weight = weight
        if age is None:
            self.age = 0

        if weight is None:
            self.weight = np.random.normal(self.w_birth, self.sigma_birth)

    def eat(self):
        """
        The weight of the animal increase every time the animal eat
        The amount of herbivores decrease if a carnivore eats
        update weight
        update fitness
        :return:
        """
        pass
