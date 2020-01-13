# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim import Fauna as fa


class TestFauna:
    """
    Tests for Fauna class.
    """

    def test_constructor_default(self):
        herb = fa.Herbivore()
        assert isinstance(herb, fa.Herbivore)
        assert herb.age == 0
        assert herb.weight >= 0
        assert herb.fitness >= 0

    def test_aging(self):
        """
        Test if the age of an animal in the fauna is the correct one.
        Test that the age is equal to zero when a animal is born
        Test that

        :return:
        """
        herb = fa.Herbivore()
        herb.aging()
        assert herb.age == 1
        assert isinstance(herb.age, int)

    def test_weight_decrease(self):
        """
        Tests if weight_decrease function decreases weight
        :return:
        """
        herb = fa.Herbivore(weight=10)
        herb.weight_decrease()
        assert herb.weight <= 10

    def test_get_weight(self):
        """
        Tests if function returns correct weight and that its an integer
        :return:
        """
        herb = fa.Herbivore(weight=10)
        assert herb.get_weight() == 10
        assert isinstance(herb.get_weight(), (int, float))

    def test_update_fitness(self):
        """
        Tests if the fitness returns a integer
        :return: integer
        """
        herb = fa.Herbivore()
        assert isinstance(herb.update_fitness(), (int, float))

    def test_check_death(self):
        """
        Tests if an animal with weight=0 returns True(animal dies) and that
        the function returns a boolean expression
        :return:
        """
        herb = fa.Herbivore(weight=0)
        herb1 = fa.Herbivore()
        assert herb.check_death() is True
        assert isinstance(herb1.check_death(), bool)

    def test_check_migration(self):
        """
        Test if method works and returns a boolean expression (True for ready
        to move and False will not move)
        """
        herb = fa.Herbivore()
        a = herb.check_migration()
        assert isinstance(a, bool)

    def test_birth(self):
        """
        When there is only one animal, test that no birth occurs.
        Test that animals cannot give birth if their weight is too low
        test that method works and returns True or False
        :return:
        """
        herb = fa.Herbivore(weight=60, age=20)
        assert herb.check_birth(1) is False
        assert herb.check_birth(6) is True
        assert isinstance(herb.check_birth(40), bool)

    def test_herbivore_eat(self):
        """
        Test that weight increases with 9 when appetite*beta = 9
        :return:
        """
        herb = fa.Herbivore(weight=1)
        herb.eat(10)
        assert herb.weight == 10

    def test_carnivore_prob_eating(self):
        """
        Tests that method returns 0 when fitness of carnivore is less or equal
        to herbivores fitness
        Test
        """
        c = fa.Carnivore(age=60, weight=0)
        herb = fa.Herbivore(age=10, weight=60)
        c2 = fa.Carnivore(age=10, weight=60)
        assert c.prob_eating(herb) == 0
        assert isinstance(c.prob_eating(herb), (int, float))
        assert 0 < c2.prob_eating(herb) < 1

    def test_carnivore_eat(self):
        """
        Tests that the weight increases when a carnivore eats a herbivore
        """
        c = fa.Carnivore(weight=5)
        herb = fa.Herbivore(weight=10)
        c.eat(herb.weight)
        assert c.weight == 12.5



