# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

# funker det

class FaunaTest:
    """
    Tests for the fauna class.
    """

    def test_age(self):
        """
        Test if the age of an animal in the fauna is the correct one.
        Test that the age is equal to zero when a animal is born
        Test that

        :return:
        """
        pass

    def test_weight(self):
        """
        Test that an animal looses weight each year
        :return:
        """
        pass

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
