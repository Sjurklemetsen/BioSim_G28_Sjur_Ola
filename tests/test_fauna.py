# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from biosim import Fauna as Fa
import random as rd
import pytest


class TestFauna:
    """
    Tests for Fauna class.
    """
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        p = {
            "w_birth": 8.0,
            "sigma_birth": 1.5,
            "beta": 0.9,
            "eta": 0.05,
            "a_half": 40.0,
            "phi_age": 0.2,
            "w_half": 10.0,
            "phi_weight": 0.1,
            "mu": 0.25,
            "landa": 1.0,
            "gamma": 0.2,
            "zeta": 3.5,
            "xi": 1.2,
            "omega": 0.4,
            "F": 10.0,
        }
        f = {
            "w_birth": 6.0,
            "sigma_birth": 1.0,
            "beta": 0.75,
            "eta": 0.125,
            "a_half": 60.0,
            "phi_age": 0.4,
            "w_half": 4.0,
            "phi_weight": 0.4,
            "mu": 0.4,
            "landa": 1.0,
            "gamma": 0.8,
            "zeta": 3.5,
            "xi": 1.1,
            "omega": 0.9,
            "F": 50.0,
            "DeltaPhiMax": 10.0
        }
        Fa.Carnivore.set_parameter(f)
        Fa.Herbivore.set_parameter(p)
        # før tester
        yield
        # etter tester

    def test_constructor_default(self):
        """
        Tests instantiation of constructor default and its parameters
        """
        herb = Fa.Herbivore()
        assert isinstance(herb, Fa.Herbivore)
        assert herb.age == 0
        assert herb.weight >= 0
        assert herb.fitness >= 0

    def test_aging(self):
        """
        Test that the age of a animal is the correct one.
        Test that the age is equal to zero when a animal is born
        """
        herb = Fa.Herbivore()
        herb.aging()
        assert herb.age == 1
        assert Fa.Herbivore().age == 0
        assert isinstance(herb.age, int)

    def test_weight_decrease(self):
        """
        Tests if weight_decrease function decreases weight according to formula
        """
        herb = Fa.Herbivore(weight=10)
        herb.weight_decrease()
        print(herb.weight)
        assert herb.weight == 9.5

    def test_get_weight(self):
        """
        Tests if function returns correct weight and that its an integer
        """
        herb = Fa.Herbivore(weight=10)
        assert herb.get_weight() == 10
        assert isinstance(herb.get_weight(), (int, float))

    def test_update_fitness(self):
        """
        Tests if the fitness returns a integer
        Tests that fitness is zero when weight is 0
        """
        herb = Fa.Herbivore()
        herb2 = Fa.Herbivore(weight=0)
        assert isinstance(herb.fitness, (int, float))
        assert herb2.fitness == 0

    def test_check_death(self):
        """
        Tests if an animal with weight=0 returns True(animal dies) and that
        the function returns a boolean expression
        Tests that an animal dies with a possibility and survives with another
        possibility
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
        carn = Fa.Carnivore(weight=60, age=20)
        print(min(1, herb.p['gamma'] * herb.fitness*(4 - 1)))  # 0.58
        assert herb.check_birth(1) is False
        rd.seed(11)  # rd.random() = 0.45
        assert herb.check_birth(4) is True
        assert isinstance(herb.check_birth(40), bool)
        assert herb2.check_birth(100) is False
        assert carn.check_birth(6) is True

    def test_herbivore_eat(self):
        """
        Test that weight increases with 9 when appetite*beta = 9
        Test that fitness increases when an animal eats
        """
        herb = Fa.Herbivore(weight=1)
        a = herb.fitness
        herb.eat(10)
        assert herb.weight == 10
        assert a < herb.fitness

    def test_carnivore_prob_eating(self):
        """
        Tests that method returns a bool
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
        """
        Tests that new parameters can be set with method
        """
        new_p = {
            'w_birth': 4,
            'sigma_birth': 2,
            'F': 15}
        Fa.Herbivore.set_parameter(new_p)
        h = Fa.Herbivore()
        assert h.p['w_birth'] == 4
        assert h.p['F'] == 15
        reset = {'w_birth': 8, 'sigma_birth': 1.5, 'F': 10}
        Fa.Herbivore.set_parameter(reset)
