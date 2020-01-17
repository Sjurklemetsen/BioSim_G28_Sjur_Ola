# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim import Geography as geo
import random as rd
import pytest


class TestGeography:
    """
    Tests for the geography class where we work with the different
    landscapes.
    """

    def test_constructor_default(self):
        jung = geo.Jungle()
        # sava = geo.Savannah()
        # ocean = geo.Ocean()
        assert isinstance(jung, geo.Jungle)
        # assert isinstance(sava, geo.Savannah)
        # assert isinstance(ocean, geo.Ocean)
        # assert jung.fodder == 800
        # assert sava.fodder == 300 and sava.geo_p['alpha'] == 0.3
        assert isinstance(jung.pop_herbivores and jung.pop_carnivores, list)

    def test_populate_cell(self):
        """
        Tests that herbivores and carnivores population is increased with
        method and that list contains instances of the animal
        """
        j = geo.Jungle()
        herbs = [geo.Herbivore() for _ in range(10)]
        carns = [geo.Carnivore() for _ in range(5)]
        j.populate_cell(herbs)
        j.populate_cell(carns)
        print(j.pop_herbivores)
        assert isinstance(j.pop_herbivores[0], geo.Herbivore)
        assert len(j.pop_herbivores) == 10
        assert len(j.pop_carnivores) == 5

    def test_add_animal(self):
        """
        Tests that herbivore and carnivore population lists expands with the
        method.
        Tests that the list contains an instance fauna
        :return:
        """
        jung = geo.Jungle()
        jung.add_animal(geo.Herbivore(age=5, weight=20))
        jung.add_animal(geo.Herbivore())
        a = geo.Carnivore()
        jung.add_animal(a)
        assert len(jung.pop_carnivores) == 1
        assert len(jung.pop_herbivores) == 2
        assert isinstance(jung.pop_herbivores[0], geo.Herbivore)
        assert jung.pop_carnivores[0] == a

    def test_remove_animals(self):
        """
        test if an animal with weight zero dies
        test
        :return:
        """
        jung = geo.Jungle()
        herbs = [geo.Herbivore(weight=0), geo.Herbivore(weight=0)]
        carns = [geo.Carnivore(weight=0)]
        jung.populate_cell(herbs)
        jung.populate_cell(carns)
        jung.remove_animals(jung.pop_herbivores + jung.pop_carnivores)
        assert len(jung.pop_herbivores) == 0
        assert len(jung.pop_carnivores) == 0

    def test_animal_die(self):
        """
        Tests that animals in a cell dies when checked for death is True and
        survives when False
        """
        jung = geo.Jungle()
        a = geo.Herbivore(age=10, weight=20)
        herbs = [geo.Herbivore(weight=0), a]
        carns = [geo.Carnivore(weight=0)]
        jung.populate_cell(herbs)
        jung.populate_cell(carns)
        rd.seed(51)  # p = 0.24
        jung.animals_die()
        assert len(jung.pop_herbivores) == 1
        assert len(jung.pop_carnivores) == 0
        assert a == jung.pop_herbivores[0]

    def test_pop_methods(self):
        """
        Test if the population methods return the correct amount of animals in
        in the cell
        """
        jung = geo.Jungle()
        jung.populate_cell([geo.Herbivore(), geo.Herbivore(), geo.Carnivore()])
        assert jung.herbivore_pop() == 2
        assert jung.carnivore_pop() == 1
        assert jung.total_pop() == 3

    def test_sort_animal_fitness(self):
        """
        Tests if herbivore pop list remains the same when fitness is already
        sorted right.
        trengs mer...
        """
        j = geo.Jungle()
        s = geo.Savannah()
        miks = [geo.Herbivore(age=20, weight=40), geo.Herbivore(weight=20),
                geo.Herbivore(weight=0)]
        miks2 = [geo.Herbivore(age=20, weight=0), geo.Herbivore(weight=20),
                 geo.Herbivore(weight=50)]
        j.populate_cell(miks)
        s.populate_cell(miks2)
        j.sort_animal_fitness(miks)
        s.sort_animal_fitness(miks2)
        assert j.pop_herbivores == miks
        assert s.pop_herbivores != miks2

    def test_propensity_herbivore(self):
        """
        Tests propensity for herbivores in different kind of cells and that
        propensity is different when population is added
        """
        j = geo.Jungle()
        s = geo.Savannah()
        m = geo.Mountain()
        o = geo.Ocean()
        d = geo.Desert()
        assert j.propensity_herb() == pytest.approx(5.54*10**34, 0.001)
        print(s.propensity_herb())
        assert s.propensity_herb() == pytest.approx(10.68*10**12, 0.001)
        assert m.propensity_herb() == 0
        assert o.propensity_herb() == 0
        assert d.propensity_herb() == 1
        j.populate_cell([geo.Herbivore() for _ in range(100)])
        assert j.propensity_herb() == pytest.approx(2.2, 0.01)

    def test_propensity_carnivore(self):
        """
        Tests propensity in cell for carnivores
        """
        j = geo.Jungle()
        s = geo.Savannah()
        m = geo.Mountain()
        o = geo.Ocean()
        d = geo.Desert()
        herbs = [geo.Herbivore(weight=10)for _ in range(5)]
        j.populate_cell(herbs)
        o.populate_cell([geo.Herbivore() for _ in range(10)])
        d.populate_cell(herbs)
        print(j.propensity_carn())
        assert j.propensity_carn() == pytest.approx(2.7, 0.01)
        assert s.propensity_carn() == 1
        assert m.propensity_carn() == 0 and o.propensity_carn() == 0
        assert d.propensity_carn() == j.propensity_carn()

    def test_check_migration(self):
        """
        Test if method returns a list with animals ready to migrate and that
        it is the same animal.
        """
        j = geo.Jungle()
        s = geo.Savannah()
        c = geo.Carnivore(age=10, weight=50)  # prob = 0.399
        s.populate_cell([geo.Herbivore(age=10, weight=39),
                         geo.Carnivore(weight=10), geo.Carnivore(weight=10),
                         geo.Carnivore(weight=100)])  # prob = 0.236
        j.add_animal(c)
        rd.seed(21)  # 0.164 then 0.68
        a = j.check_migration()
        rd.seed(10)  # prob 4 iterering = 0.20
        b = s.check_migration()
        assert len(a) == 1 and a[0] == c
        assert isinstance(a, list)
        assert len(b) == 1

    def test_fodder_eaten(self):
        """
        Tests that method returns fodder and fodder eaten when there's
        bountiful of food.
        Tests that method returns fodder and fodder eaten when animal has a
        bigger appetite than the cell offers
        Tests that fodder eaten is 0 when there's no fodder left to eat
        """
        j = geo.Jungle()
        j.populate_cell([geo.Herbivore(weight=10)])
        jung = j.fodder_eaten()
        assert isinstance(jung, (int, float))
        assert j.fodder == 790 and j.fodder_eaten() == 10
        j.fodder = 5
        assert j.fodder_eaten() == 5
        assert j.fodder == 0
        assert j.fodder_eaten() == 0

    def test_herbivore_eat(self):
        """
        Test if the herbivore eat method works as it should
        """
        j = geo.Jungle()
        j.populate_cell([geo.Herbivore(weight=0),
                         j.populate_cell(geo.Herbivore() for _ in range(9))])
        j.herbivore_eat()
        assert j.fodder == 700
        assert j.pop_herbivores[-1].get_weight() == 9

    def test_carnivore_eat(self):
        """
        Tests if the carnivore eats the least fittest herbivore
        Tests if population of herbivores decreases when carnivore eats
        Tests if weight increases according to formula when carnivore eats
        and stops eating when stomach full
        Tests that next carnivore eats and increases weight
        Tests that when carni
        """
        j = geo.Jungle()
        j.populate_cell([j.populate_cell(geo.Herbivore(age=60, weight=10)
                                         for _ in range(1000))])
        j.populate_cell([geo.Carnivore(age=10, weight=60),
                         geo.Carnivore(weight=30)])
        j.carnivore_eat()
        assert 0 < len(j.pop_herbivores) < 1000
        assert 30 < j.pop_carnivores[1].weight <= 60

    def test_get_herb_weight(self):
        """
        Tests that method returns combined weight of herbivores in cell
        """
        d = geo.Desert()
        d.populate_cell([geo.Herbivore(weight=10) for _ in range(10)])
        assert d.get_herb_weight() == 100

    def test_animal_mating(self):
        """
        Tests that babies born is an instance of its species
        Tests that population grows by one when probability of birth for a
        animal of the same species is 100%
        """
        j = geo.Jungle()
        j.populate_cell([geo.Carnivore(age=1, weight=100),
                         geo.Herbivore(age=1, weight=100)])
        # j.populate_cell(geo.Carnivore(age=1, weight=100))
        # j.add_animal(geo.Herbivore(age=1, weight=100))
        j.populate_cell([geo.Herbivore(age=10, weight=10) for _ in range(7)])
        j.populate_cell([geo.Carnivore(age=60, weight=10) for _ in range(7)])
        j.animal_mating()
        assert len(j.pop_herbivores) == 9
        assert isinstance(j.pop_herbivores[-1], geo.Herbivore)
        assert len(j.pop_carnivores) == 9
        assert isinstance(j.pop_carnivores[-1], geo.Carnivore)

    def test_age_weightloss(self):
        d = geo.Desert()
        d.populate_cell([geo.Herbivore(age=1, weight=5),
                         geo.Carnivore(weight=10)])
        d.age_weightloss()
        herb = d.pop_herbivores[0]
        assert herb.age == 2 and herb.weight == 4.75
        carn = d.pop_carnivores[0]
        assert carn.age == 1 and carn.weight == 8.75

    def test_fodder_growth(self):
        o = geo.Ocean()
        s = geo.Savannah()
        s.fodder = 100
        j = geo.Jungle()
        j.fodder = 200
        o.fodder_growth()
        s.fodder_growth()
        j.fodder_growth()
        assert o.fodder == 0
        assert s.fodder == 160
        assert j.fodder == 800

    def test_jungle(self):
        """
        Test if jungle is a instance
        Test if fodders in the jungle is equal to f max in the start of each
        cycle
        :return:
        """
        j = geo.Jungle()
        j.fodder = 10
        j.fodder_growth()
        assert isinstance(j, geo.Jungle)
        assert j.fodder == 800

    def test_savannah(self):
        """
        Test if savannah is a instance
        Test if fodders in the jungle is updated for each cycle
        :return:
        """
        s = geo.Savannah()
        assert s.fodder == 300
        assert isinstance(s, geo.Savannah)
        assert s.geo_p['f_max'] == 300
        assert s.geo_p['alpha'] == 0.3

    def test_desert(self):
        """
        Test if the fodder equals zero
        :return:
        """
        d = geo.Desert()
        assert isinstance(d, geo.Desert)
        assert d.geo_p['f_max'] == 0
        assert d.fodder == 0

    def test_ocean(self):
        """
        Tests if ocean is an instance
        :return:
        """
        o = geo.Ocean()
        assert isinstance(o, geo.Ocean)
        assert o.geo_p['f_max'] is None

    def test_mountain(self):
        """
        Test if mountain is an instance
        :return:
        """
        m = geo.Mountain()
        assert isinstance(m, geo.Mountain)
        assert m.geo_p['f_max'] is None

    def test_set_parameter(self):
        new_parameters = {'f_max': 1000, 'alpha': 500}
        geo.Jungle.set_parameter(new_parameters)
        jung = geo.Jungle()
        assert jung.geo_p['f_max'] == 1000
        assert jung.fodder == 1000