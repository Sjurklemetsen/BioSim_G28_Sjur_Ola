# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim import Geography as geo


class TestGeography:
    """
    Tests for the geography class where we work with the different
    landscapes.
    """
    def test_constructor_default(self):
        jung = geo.Jungle()
        sava = geo.Savannah()
        assert isinstance(jung, geo.Jungle)
        assert isinstance(sava, geo.Savannah)
        #assert jung.fodder == 800
        #assert sava.fodder == 300
        #assert isinstance(jung.pop_herbivores, list)

    def test_set_parameter(self):
        new_parameters = {'f_max': 1000, 'alpha': 500}

    def test_add_animal(self):
        jung = geo.Jungle()


    def test_ocean(self):
        """
        Tests if ocean is an instance
        :return:
        """
        o = Ocean()
        assert issubclass(Ocean, Geography)
        assert isinstance(o, Ocean)

    def test_mountain(self):
        """
        Test if mountain is an instance
        :return:
        """
        m = Mountain()
        assert issubclass(Mountain, Geography)
        assert isinstance(m, Mountain)

    def test_desert(self):
        """
        Test if the fodder equals zero
        :return:
        """
        d = Desert()
        assert issubclass(Desert, Geography)
        assert isinstance(d, Desert)
        assert "default param" f_max == 0
        pass


    def test_savannah(self):
        """
        Test if savannah is a instance
        Test if fodders in the jungle is updated for each cycle
        :return:
        """
        s = Savannah()
        assert issubclass(Savannah, Geography)
        assert isinstance(s, Savannah)
        assert "default param" f_max == 200
        assert "test if fodder grows to formula each year"
        pass

    def test_jungle(self):
        """
        Test if jungle is a instance
        Test if fodders in the jungle is equal to f max in the start of each
        cycle
        :return:
        """
        j = Jungle()
        j_fodder = Jungle().fodder_replenish()
        assert issubclass(Jungle, Geography)
        assert isinstance(j, Jungle)
        assert "default param" f_max == 800
        assert j_fodder == "defaut param" f_max
        pass
