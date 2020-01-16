# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim import Map as ma
import textwrap


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
        print(map)
        m = ma.Map()
        print(m.create_map(map))

    def test_check_string(self):
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
        print(m.find_neighbor_cells((0, 0)))
        assert isinstance(m.find_neighbor_cells((2, 3)), list)

    def test_migrate_to(self):
        """
        Tests that migration works correctly
        Tests that it returns a coordinate tuple
        """
        map = """
                OOOOO
                OSDJO
                OOOOO"""
        m = ma.Map()
        m.create_map()
        pos = (1, 2)
        assert isinstance(m.migrate_to(pos), tuple)

    def test_move(self):
        """
        Tests that animal moves right
        """
        pass

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