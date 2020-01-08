# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'


class Biography:
    """
    Biography of the whole island
    """
    def __init__(self, f_max):
        pass


class Ocean(Biography):
    """
    Island area type that is impassable (passive) in simulation
    """
    def __init__(self, f_max):
        super().__init__(self, f_max)

    pass

class Mountain:
    """
    Island area type that is impassable (passive) in simulation
    """
    def __init__(self):
        super().__init__(self, f_max)
    """

    """

class Desert(Biography):
    """
    Area type that holds no fodder, but animals can inhabit the cells
    """
    def __init__(self):
        super().__init__(self, f_max)
    """

    """

class Savannah(Biography):
    """
    Area type that holds some fodder, but can suffer overgrazing
    """
    def __init__(self, f_max_savannah, alpha):
        super().__init__(self, f_max)
    """

    """
    def fodder_growth(self, alpha):
        """
        Fodder growth for savannah
        :param alpha: amount of growth
        :return:
        """


class Jungle(Biography):
    """
    Area type that holds alot of fodder snd replenishes fodder to max each year.
    """
    def __init__(self, f_max_jungle):
        super().__init__(self, f_max)

    def fodder_replenish(self):
        """
        Replenishes fodder each year
        :return:
        """

