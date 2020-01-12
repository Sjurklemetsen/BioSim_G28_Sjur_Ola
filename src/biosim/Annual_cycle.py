# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim.Geography import *

class AnnualCycle:
    """
    Annual cycle on Rossumøya
    """

    def __init__(self):
        pass

    def feeding(self):
        """
        Animals eat in order:
        herbivores - carnivores
        Growth of fodder comes first
        :return:
        """
        pass

    def procreation(self):
        """
        Animals give birth
        :return:
        """
        pass

    def migrating(self):
        """
        Animals move one cell with a probability wit the most fodder
        :return:
        """
        pass

    def aging(self):
        """
        Animals age one year
        :return:
        """
        pass

    def loss_of_weight(self):
        """
        Animals lose weight eache year
        :return:
        """
        pass

    def death(self):
        """
        Determines if an animal dies
        :return:
        """
        pass
