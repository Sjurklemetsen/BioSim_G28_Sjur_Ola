# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'


class Geography:
    """
    Biography of the whole island
    """
    f_max = None

    def __init__(self, f_max):
        pass


class Ocean(Geography):
    """
    Island area type that is impassable (passive) in simulation
    """
    f_max = None

    def __init__(self, f_max):
        super().__init__(self, f_max)
    pass


class Mountain:
    """
    Island area type that is impassable (passive) in simulation
    """
    f_max = None

    def __init__(self):
        super().__init__(self, f_max)
    """

    """


class Desert(Geography):
    """
    Area type that holds no fodder, but animals can inhabit the cells
    """
    f_max = None

    def __init__(self):
        super().__init__(self, f_max)


class Savannah(Geography):
    """
    Area type that holds some fodder, but can suffer overgrazing
    """
    f_max = 300
    alpha = 0.3

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


class Jungle(Geography):
    """
    Area type that holds a lot of fodder snd replenishes fodder to max each year.
    """
    f_max = 800

    def __init__(self, f_max_jungle):
        super().__init__(self, f_max)

    def fodder_replenish(self):
        """
        Replenishes fodder each year
        :return:
        """
        pass
    
    def fodder_amount(self):
        pass
