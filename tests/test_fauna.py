# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim import Fauna as Fa
import random as rd


class TestFauna:
    """
    Tests for Fauna class.
    """

    def test_constructor_default(self):
        herb = Fa.Herbivore()
        assert isinstance(herb, Fa.Herbivore)
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
        herb = Fa.Herbivore()
        herb.aging()
        assert herb.age == 1
        assert isinstance(herb.age, int)

    def test_weight_decrease(self):
        """
        Tests if weight_decrease function decreases weight
        :return:
        """
        herb = Fa.Herbivore(weight=10)
        herb.weight_decrease()
        assert herb.weight <= 10

    def test_get_weight(self):
        """
        Tests if function returns correct weight and that its an integer
        :return:
        """
        herb = Fa.Herbivore(weight=10)
        assert herb.get_weight() == 10
        assert isinstance(herb.get_weight(), (int, float))

    def test_update_fitness(self):
        """
        Tests if the fitness returns a integer
        :return: integer
        """
        herb = Fa.Herbivore()
        assert isinstance(herb.fitness, (int, float))

    def test_check_death(self):
        """
        Tests if an animal with weight=0 returns True(animal dies) and that
        the function returns a boolean expression
        :return:
        """
        h_die = Fa.Herbivore(weight=0)
        rd.seed(1)
        h_unlucky = Fa.Herbivore(weight=20, age=90)
        h_survivor = Fa.Herbivore(age=20, weight=40)
        assert h_unlucky.check_death() is True
        assert h_survivor.check_death() is False
        assert h_die.check_death() is True

        assert isinstance(h_die.check_death(), bool)

    def test_check_birth(self):
        """
        When there is only one animal, test that no birth occurs.
        Test that animals cannot give birth if their weight is too low, too low
        would be less than 33.25 with default parameters.
        test that method works and returns True or False
        """
        herb = Fa.Herbivore(weight=60, age=20)
        herb2 = Fa.Herbivore(weight=33.24, age=2)
        print(min(1, herb.p['gamma'] * herb.fitness*(4 - 1)))  # 0.58
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
        herb = Fa.Herbivore(weight=1)
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
        c = Fa.Carnivore(age=10, weight=60)
        herb = Fa.Herbivore(age=80, weight=3)
        herb2 = Fa.Herbivore(age=5, weight=70)
        c2 = Fa.Carnivore(age=60, weight=50)
        rd.seed(224)  # 0.06, 0.19
        assert c.prob_eating(herb) is True
        assert c.prob_eating(herb) is False
        assert c2.prob_eating(herb2) is False
        assert isinstance(c.prob_eating(herb), bool)
        Fa.Carnivore.p['DeltaPhiMax'] = 0.5
        # Carn fitness - herb fitness bigger than DeltaPhiMax
        assert c.prob_eating(herb)

    def test_carnivore_eat(self):
        """
        Tests that the weight increases according to formula when a carnivore
        eats a herbivore.
        Tests that carnivore stops eating when it has tried to kill everyone
        Tests that Carnivore stops eating when carnivore is full
        Tests that Herbivore list decreases when carnivore eats
        """
        c = Fa.Carnivore(weight=40)
        herbs = [Fa.Herbivore(weight=20, age=80) for _ in range(10)]
        herbs2 = [Fa.Herbivore(weight=12, age=80) for _ in range(100)]
        rd.seed(1)
        c.eat(herbs)
        assert len(herbs) == 8
        assert c.weight == 70
        c.eat(herbs2)
        assert len(herbs2) == 95
        assert c.weight == 113.5

    def test_set_parameter(self):
        new_p = {
            'w_birth': 4,
            'sigma_birth': 2,
            'F': 15}
        Fa.Herbivore.set_parameter(new_p)
        h = Fa.Herbivore()
        assert h.p['w_birth'] == 4
        assert h.p['F'] == 15
        Fa.Herbivore.set_parameter({'w_birth': 8, 'sigma_birth': 1.5, 'F': 10})







