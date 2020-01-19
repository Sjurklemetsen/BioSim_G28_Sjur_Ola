# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim import Map as Ma
from src.biosim import Fauna as Fa
from src.biosim import Geography as Geo
import textwrap
import random as rd


class TestMap:
    """
    Tests for map class
    """

    def test_map_constructor_default(self):
        """
        Tests map constructor default
        """
        pass

    def test_create_map(self):
        """
        Tests map creation
        """
        map = """
                 OOOO
                 OSDO
                 OOOO"""
        map = textwrap.dedent(map)
        m = Ma.Map(map)
        m.create_map(map)

    def test_check_map_string(self):
        """
        Tests that input for map creation is valid
        """
        pass

    def test_populate_map(self):
        map = """\
                 OOOOOO
                 OJDJJO
                 OSJJOO
                 OOOOOO"""
        m = Ma.Map(map)
        pos = (1, 1)
        pop = [Fa.Carnivore(), Fa.Herbivore(), Fa.Carnivore()]
        m.populate_map(pos, pop)
        assert m.island[1, 1].total_pop == 3
        assert m.island[1, 1].carnivore_pop == 2

    def test_find_neighbour_cells(self):
        """
        Tests that function finds the neighbouring cells of the input
        """
        map = """\
                 OOOO
                 OSDO
                 OOOO"""
        m = Ma.Map(map)
        a = m.find_neighbor_cells((2, 3))
        b = m.find_neighbor_cells((1, 1))
        assert isinstance(a, list)
        assert b == [(2, 1), (0, 1), (1, 2), (1, 0)]
        assert a == [(3, 3), (1, 3), (2, 4), (2, 2)]

    def test_migrate_to(self):
        """
        Returns the position its in when Mountain or Ocean is surrounding it
        Tests that it returns a tuple based on propensity
        Tests that it can return 4 possible outcomes
        """
        map = """\
                 OOOOO
                 OJJJO
                 OJJJO
                 OJJOO
                 OOOOO"""

        map2 = """\
                  OOOO
                  OJMO
                  OOOO"""
        m = Ma.Map(map)
        rd.seed(148)
        pos = (2, 2)
        a = m.migrate_to(pos)
        b = m.migrate_to(pos)
        c = m.migrate_to(pos)
        d = m.migrate_to(pos)
        m2 = Ma.Map(map2)
        assert m2.migrate_to((1, 1)) == (1, 1)
        assert isinstance(a, tuple)
        assert a == (1, 2)
        assert b == (2, 3)
        assert c == (2, 1)
        assert d == (3, 2)

    def test_move(self):
        """
        Tests that animal moves to the right cell
        Test that the animals are added to the new cell and removed from the
        old cell
        """

        map = """\
                 OOOOOO
                 OODOJO
                 OOJJOO
                 OOOOOO"""
        rd.seed(5)
        m = Ma.Map(map)
        m.populate_map((1, 2), [Ma.Carnivore(
            age=10, weight=50) for _ in range(100)])
        m.populate_map((1, 2), [Ma.Herbivore(
            age=15, weight=30) for _ in range(10)])

        new_cell = m.migrate_to((1, 2))
        m.move()

        assert m.island[1, 2].total_pop() + m.island[
            new_cell].total_pop() == 110
        assert m.island[1, 2].total_pop() == 62
        assert m.island[new_cell].total_pop() == 48

    def test_annual_cycle(self):
        """
        Tests that annual cycle works as it should
        """
        map = """
                OOOO
                OJJO
                OOOO"""
        map = textwrap.dedent(map)
        print(map)
        m = Ma.Map()
        m.create_map(map)
        m.populate_map()
