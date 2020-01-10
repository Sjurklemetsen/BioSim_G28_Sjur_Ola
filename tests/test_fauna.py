# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim import Fauna as fa


class FaunaTest:
    """
    Tests for Fauna class.
    """

    def test_fitness(self):
        """
        tests if the fitness returns a boolean expression
        :return: bool
        """
        a = fa.Fauna()
        assert isinstance(a.fitness(), int)

    def test_age(self):
        """
        Test if the age of an animal in the fauna is the correct one.
        Test that the age is equal to zero when a animal is born
        Test that

        :return:
        """
        h = fa.Herbivore()
        assert h.age() == 0
        assert isinstance(h.age(), int)

    def test_weight(self):
        """
        Tests if age on an animal
        :return:
        """
        f = fa.Fauna(weight=10)
        w = f.animal_weight()
        assert w == 10

    def test_migration(self):
        """
        Test if the animals move towards the most optimal cell
        Test if the animal only moves to one of the four adjacent cells
        Test if the animal cannot move to a mountain or ocean cell
        :return:
        """
        pass

    def test_birth(self):
        """
        When there is only one animal, test that no birth occurs.
        Test that the mother looses the right amout of weight after birth
        Test that animals cant give more than 1 offspirng each cycle
        Test that animals cannot give birth if their weight is too low
        :return:
        """
        pass

    def test_death(self):
        """
        Test that an animal dies when its fitness is zero
        :return:
        """
        pass

    def test_herbivore(self):
        """
        Test the characteristics unique for herbivores such as feeding
        :return:
        """
        pass

    def test_carnivore(self):
        """
        Test the characteristics unique for carnivores
        :return:
        """
        pass
