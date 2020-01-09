# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

import numpy as np
import math
import random as rd


class Fauna:
    """
    Class for a animal in the fauna
    """
    w_birth = None
    sigma_birth = None
    beta = None
    eta = None
    a_half = None
    phi_age = None
    w_half = None
    phi_weight = None
    mu = None
    landa = None
    gamma = None
    zeta = None
    xi = None
    omega = None
    F = None

    @property
    def fitness(self):
        """
        The fitness of an animal
        :return:
        """
        return (1 / (1 + math.exp(
            self.phi_age * (self.age - self.a_half))) * 1 / (
                1 / (1 + math.exp(
                    - self.phi_weight(self.weight - self.w_half)))
                        ))

    @property
    def migration(self):
        """
        Method that check if the animal is ready to move to another cell
        Lag funksjon som flytter dyr fra en celle til en annen hvis True ####
        :return: Boolean expression
        """
        prob_move = self.mu * self.fitness
        return rd.random() < prob_move

    @property
    def death(self):
        """
        Function that checks if the animal is dead or not
        Lag funksjon som fjerner dyr fra cellene hvis True ####
        :return: Boolean expression
        """
        if self.fitness == 0:
            return True
        elif rd.random() < self.omega * (1 - self.fitness):
            return True
        else:
            return False

    def __init__(self):
        self.age = 0
        self.weight = np.random.normal(self.w_birth, self.sigma_birth)

    def aging(self):
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
        self.weight -= self.eta * self.weight

    def birth(self):
        """
        An animal can give birth to a child if all the conditions are met
        :return:
        """


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
    landa = 1.0
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
        weight update
        :return:
        """

        self.weight += self.beta * fodder


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
        update weight
        update fitness
        :return:
        """
        pass

    """
    Skriv funskjon som fjerner dyr 
    Skriv funskjon som teller antall dyr i en celle 
    
    """
