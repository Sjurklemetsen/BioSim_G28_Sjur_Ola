# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

import random as rd
import math
import numpy as np


class BaseFauna:
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

    @classmethod
    def set_parameter(cls, new_p):
        """
        This method let you set new parameters instead of the default ones
        :param new_p: dictionary with new parameters
        """
        for key in new_p:
            cls.p[key] = new_p[key]

    def __init__(self, age=0, weight=None):
        self.age = age
        self.weight = weight
        self.animal_moved = False
        if weight is None:
            self.weight = np.random.normal(self.p['w_birth'],
                                           self.p['sigma_birth'])

    @property
    def fitness(self):
        """
        Update the fitness of the animal based on age and weight
        :return: float
        """
        if self.weight <= 0:
            fitness = 0
        else:
            fitness = 1 / (1 + math.exp(self.p['phi_age'] * (
                    self.age - self.p['a_half']
            ))) * 1 / (1 + math.exp(-self.p['phi_weight'] * (
                    self.weight - self.p['w_half'])))
        return fitness

    def aging(self):
        """
        Age of the animals increase by one each year
        """
        self.age += 1

    def weight_decrease(self):
        """
        The weight of the animal decrease each year
        """
        self.weight -= self.p['eta'] * self.weight

    def get_weight(self):
        """
        :return: float
        """
        return self.weight

    def check_death(self):
        """
        Method that checks if the animal is dead
        :return: Boolean expression
        """
        if self.fitness == 0:
            return True
        elif rd.random() < self.p['omega'] * (1 - self.fitness):
            return True
        else:
            return False

    def check_birth(self, n_animals):
        """
        A Method that check if an animal is ready to give birth or not
        :param n_animals: int - How many animals of the same species in a cell
        :return: Boolean expression
        """
        probability = min(1, self.p['gamma'] * self.fitness *
                          (n_animals - 1))

        if self.weight < self.p['zeta'] * (self.p['w_birth'] +
                                           self.p['sigma_birth']):
            return False
        elif rd.random() <= probability:
            return True
        else:
            return False


class Herbivore(BaseFauna):
    """
    A class for herbivores that eat fodder
    """
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
        "landa": 1.0,
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
        The herbivore has a weight increase if it eats fodder
        """
        self.weight += appetite * self.p['beta']


class Carnivore(BaseFauna):
    """
    A class for carnivores that eat herbivores
    """
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
        "landa": 1.0,
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
        :input: list - Herbivores with sorted fitness.
        :return: Boolean expression
        """
        prob = (self.fitness - herb.fitness) / self.p['DeltaPhiMax']

        if self.fitness <= herb.fitness:
            return False
        elif 0 < self.fitness - herb.fitness < self.p['DeltaPhiMax']:
            if prob > rd.random():
                return True
            else:
                return False
        else:
            return True

    def eat(self, pop_herb):
        """
        The carnivore tries to eat the herbivores in the cell.
        The weight of the animal increase every time the animal eat.
        The amount of herbivores decrease if a carnivore eats.
        :return: list - the new herbivore population
        """
        herb_eaten = 0

        for herb in pop_herb[::-1]:
            if self.prob_eating(herb):
                herb_eaten += herb.weight
                if herb_eaten >= self.p['F']:
                    self.weight += (herb_eaten - self.p['F'])*self.p['beta']
                    pop_herb.remove(herb)
                    break
                elif herb_eaten < self.p['F']:
                    self.weight += herb.weight*self.p['beta']
                    pop_herb.remove(herb)
        return pop_herb


if __name__ == "__main__":
    Herbivore.set_parameter(new_p={
            'w_birth': 4,
            'sigma_birth': 2,
            'F': 15})

    h = Herbivore()
    print(Herbivore.p['w_birth'])
    """rd.seed(11)
    print(rd.random()) # 0.827

    c = Carnivore(age=10, weight=70)
    pop_herb = [Herbivore() for n in range(100)]
    print(len(pop_herb))"""



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



