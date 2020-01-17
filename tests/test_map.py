# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim import Map as ma
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
        m = ma.Map()
        m.create_map(map)

    def test_check_map_string(self):
        """
        Tests that input for map creation is valid
        """
        pass

    def test_find_neighbour_cells(self):
        """
        Tests that function finds the neighbouring cells of the input
        """
        map = """
                         OOOO
                         OSDO
                         OOOO"""
        map = textwrap.dedent(map)
        m = ma.Map()
        assert isinstance(m.find_neighbor_cells((2, 3)), list)

    def test_migrate_to(self):
        """
        Tests that migration works correctly
        Tests that it returns a coordinate tuple
        """
        map = """
                         OOOO
                         OSDO
                         OOOO"""
        map = textwrap.dedent(map)
        m = ma.Map()
        m.create_map(map)

        pos = (1, 2)
        pop = [ma.Herbivore()for _ in range(20)]
        m.populate_map(pos, pop)
        assert isinstance(m.migrate_to(pos), tuple)

    def test_move(self):
        """
        Tests that animal moves to the right cell
        Test that the animal doesnt move more then once
        Test that the animals are added to the new cell and removed from the
        old cell
        """

        map = """\
                 OOOO
                 OSDO
                 OOOO"""
        m = ma.Map(map)
        rd.seed(5)
        m.populate_map((1, 2), [ma.Carnivore(
            age=10, weight=50) for _ in range(100)])
        m.populate_map((1, 2), [ma.Herbivore(
            age=15, weight=30) for _ in range(10)])

        print(m.island[1, 2].total_pop())
        m.move()
        print(m.island[1, 2]).totalpop())
        assert m.island[1, 2].total_pop() == 56






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
        m = ma.Map()
        m.create_map(map)
        m.populate_map()