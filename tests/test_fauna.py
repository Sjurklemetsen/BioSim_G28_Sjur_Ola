# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim import Fauna as fa
import random as rd


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
        rd.seed(111)
        herb = fa.Herbivore(weight=0)
        herb1 = fa.Herbivore(weight=20, age=10)
        assert herb1.check_death() is False
        assert herb.check_death() is True
        assert isinstance(herb1.check_death(), bool)

    def test_check_migration(self):
        """
        Test if method works and returns a boolean expression (True for ready
        to move and False will not move)
        """
        rd.seed(11)
        herb = fa.Herbivore(age=10, weight=50)
        print(herb.fitness*herb.p['mu'])
        assert herb.check_migration() is False
        assert isinstance(herb.check_migration(), bool)

    def test_check_birth(self):
        """
        When there is only one animal, test that no birth occurs.
        Test that animals cannot give birth if their weight is too low, too low
        would be less than 33.25 with default parameters.
        test that method works and returns True or False
        """
        herb = fa.Herbivore(weight=60, age=20)
        herb2 = fa.Herbivore(weight=33.24, age=2)
        print(min(1, herb.p['gamma'] * herb.update_fitness()*(4 - 1)))  # 0.58
        assert herb.check_birth(1) is False
        rd.seed(11)  # rd.random() = 0.45
        assert herb.check_birth(4) is True
        assert isinstance(herb.check_birth(40), bool)
        assert herb2.check_birth(100) is False

    def test_herbivore_eat(self):
        """
        Test that weight increases with 9 when appetite*beta = 9
        Test that fitness increases when an animal eats
        :return:
        """
        herb = fa.Herbivore(weight=1)
        a = herb.fitness
        herb.eat(10)
        assert herb.weight == 10
        assert a < herb.fitness

    def test_carnivore_prob_eating(self):
        """
        Tests that method returns a boolean
        Tests that method returns 0 when fitness of carnivore is less or equal
        to herbivores fitness
        Tests that when rd.random() is less than probability of eating returns
        True
        """
        c = fa.Carnivore(age=10, weight=60)
        herb = fa.Herbivore(age=80, weight=3)
        c2 = fa.Carnivore(age=10, weight=60)
        rd.seed(224)  # 0.0652
        assert c.prob_eating(herb) is True
        assert isinstance(c.prob_eating(herb), bool)
        assert c2.prob_eating(herb) is True

    def test_carnivore_eat(self):
        """
        Tests that the weight increases according to formula when a carnivore
        eats a herbivore.
        Tests that the population decreases when carnivore eats
        """
        c = fa.Carnivore(weight=40)
        c2 = fa.Carnivore(weight=40)
        c2.p['DeltaPhiMax'] = 0.001
        w = c.weight
        herb = [fa.Herbivore(weight=10)]
        herbs = [fa.Herbivore(age=10, weight=10) for _ in range(1000)]
        assert len(c.eat(herbs)) == 995
        assert 0 < (c.weight-w) <= 45
        assert len(c2.eat(herb)) == 0
        assert c2.weight == 47.5



