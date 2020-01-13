# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

import random as rd
import numpy as np


class Fauna:
    """
    Class for an animal in the fauna
    """
    p = {
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

    def set_parameter(self, new_p):
        """
        This method let you set new parameters instead of the default ones
        :param new_p: dictionary with new parameters
        """
        for key in new_p:
            self.p[key] = new_p

    def __init__(self, age=0, weight=None):
        self.age = age
        self.weight = weight
        if weight is None:
            self.weight = np.random.normal(self.p['w_birth'],
                                           self.p['sigma_birth'])
        self.fitness = self.update_fitness()

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
        self.weight -= self.p['eta'] * self.weight
        self.update_fitness()

    def get_weight(self):
        """
        :return: The weight of the animal: float
        """
        return self.weight

    def update_fitness(self):
        """
        Update the fitness of the animal based on the new age and weight
        :return: New updated value: float
        """
        if self.weight <= 0:
            return 0
        else:
            self.fitness = 1 / (1 + np.exp(self.p['phi_age'] * (
                self.age - self.p['a_half']
                    ))) * 1 / (1 + np.exp(-self.p['phi_weight'] * (
                        self.weight - self.p['w_half'])))
        return self.fitness

    def check_death(self):
        """
        Function that checks if the animal is dead or not
        :return: Boolean expression
        """
        if self.update_fitness() == 0:
            return True
        elif rd.random() < self.p['omega'] * (1 - self.update_fitness()):
            return True
        else:
            return False

    def check_migration(self):
        """
        Method that check if the animal is ready to move to another cell
        :return: Boolean expression
        """
        prob_move = self.p['mu'] * self.update_fitness()
        return rd.random() < prob_move

    def check_birth(self, n_animals):
        """
        A Method that check if an animal is ready to give birth or not
        :param n_animals:
        :return: Boolean expression
        """
        probability = min(1, self.p['gamma'] * self.update_fitness() *
                          (n_animals - 1))

        if self.weight < self.p['zeta'] * (self.p['w_birth'] +
                                           self.p['sigma_birth']):
            return False
        elif rd.random() <= probability:
            return True
        else:
            return False


class Herbivore(Fauna):
    p = {
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

    def __init__(self, age=0, weight=None):
        super().__init__(age=age, weight=weight)

    def eat(self, appetite):
        """
        The herbivore has a weight increase if it eats fodder in a jungle or
        a savannah cell
        :return:
        """
        self.weight += appetite * self.p['beta']
        self.update_fitness()


class Carnivore(Fauna):
    p = {
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

    def __init__(self, age=0, weight=None):
        super().__init__(age=age, weight=weight)

    def prob_eating(self, herb):
        """
        Chances for a carnivore to eat a herbivore
        :input: A list of herbivores with sorted fitness.
        :return: Boolean expression
        """
        if self.fitness <= herb.fitness:
            return 0
        elif 0 < self.fitness - herb.fitness < self.p['DeltaPhiMax']:
            return (self.fitness - herb.fitness) / self.p['DeltaPhiMax']
        else:
            return 1


    def eat(self, herb_w):
        """
        The weight of the animal increase every time the animal eat
        The amount of herbivores decrease if a carnivore eats
        update weight
        update fitness
        :return:
        """
        self.weight += herb_w * self.p['beta']
        self.update_fitness()


if __name__ == "__main__":
    herb = Herbivore(weight=60, age=20)
    print(herb.check_migration())

    """n_animals = 60
    p = min(1, 0.2 * herb.update_fitness() * (n_animals - 1))
    print(p)
    print(herb.check_birth(6))
    print(herb.aging())
    print(herb.age)
    print(herb.weight)
    print(herb.update_fitness())
    print(herb.check_death())
    print(herb.check_migration())
    print(rd.random())"""



