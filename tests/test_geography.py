# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim import Geography as geo


class TestGeography:
    """
    Tests for the geography class where we work with the different
    landscapes.
    """
    def test_constructor_default(self):
        jung = geo.Jungle()
        #sava = geo.Savannah()
        #ocean = geo.Ocean()
        assert isinstance(jung, geo.Jungle)
        #assert isinstance(sava, geo.Savannah)
        #assert isinstance(ocean, geo.Ocean)
        #assert jung.fodder == 800
        #assert sava.fodder == 300 and sava.geo_p['alpha'] == 0.3
        assert isinstance(jung.pop_herbivores and jung.pop_carnivores, list)

    def test_set_parameter(self):
        new_parameters = {'f_max': 1000, 'alpha': 500}
        jung = geo.Jungle()
        #jung.set_parameter(new_parameters)
        #assert jung.geo_p['f_max'] == 1000
        #assert jung.fodder == 1000

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
        jung.add_animal(geo.Carnivore())
        assert len(jung.pop_carnivores) == 1
        assert len(jung.pop_herbivores) == 2
        assert isinstance(jung.pop_herbivores[0], geo.Fauna)

    def test_remove_animals(self):
        """
        test if an animal with weight zero dies
        test
        :return:
        """
        jung = geo.Jungle()
        jung.add_animal(geo.Herbivore(weight=0))
        jung.add_animal(geo.Carnivore(weight=0))
        assert len(jung.pop_herbivores) == 1
        jung.remove_animals()
        assert len(jung.pop_herbivores) == 0
        assert len(jung.pop_carnivores) == 0

    def test_pop_methods(self):
        """
        Test if the population methods return the correct amount of animals in
        in the cell
        """
        jung = geo.Jungle()
        jung.add_animal(geo.Herbivore())
        jung.add_animal(geo.Herbivore())
        jung.add_animal(geo.Carnivore())
        assert jung.herbivore_pop() == 2
        assert jung.carnivore_pop() == 1
        assert jung.total_pop() == 3

    def test_sort_animal_fitness(self):
        """
        Tests if herbivore pop list remains the same when fitness is already
        sorted right.
        trengs mer...
        :return:
        """
        j = geo.Jungle()
        j.add_animal(geo.Herbivore(age=20, weight=40))
        j.add_animal(geo.Herbivore(weight=20))
        j.add_animal(geo.Herbivore(weight=0))
        pop = j.pop_herbivores
        j.sort_animal_fitness(pop)
        assert j.pop_herbivores == pop

    def test_fodder_eaten(self):
        """
        Tests that method returns fodder and fodder eaten when there's
        bountiful of food.
        Tests that method returns fodder and fodder eaten when animal has a
        bigger appetite than the cell offers
        Tests that fodder eaten is 0 when there's no fodder left to eat
        """
        j = geo.Jungle()
        j.add_animal(geo.Herbivore(weight=10))
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
        j.add_animal(geo.Herbivore(weight=0))
        for animal in range(9):
            j.add_animal(geo.Herbivore())
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
        for n in range(1000):
            j.add_animal(geo.Herbivore(age=60, weight=10))
        j.add_animal(geo.Carnivore(age=10, weight=60))
        j.add_animal(geo.Carnivore(weight=30))
        j.carnivore_eat()
        assert 0 < len(j.pop_herbivores) < 1000
        assert 30 < j.pop_carnivores[1].weight <= 60

    def test_animal_mating(self):
        """
        Tests that babies born is an instance of its species
        Tests that population grows by one when probability of birth for a
        animal of the same species is 100%
        """
        j = geo.Jungle()
        j.add_animal(geo.Carnivore(age=1, weight=100))
        j.add_animal(geo.Herbivore(age=1, weight=100))
        for n in range(7):
            j.add_animal(geo.Herbivore(age=10, weight=10))
            j.add_animal(geo.Carnivore(weight=10, age=60))
        j.animal_mating()
        assert len(j.pop_herbivores) == 9
        assert isinstance(j.pop_herbivores[-1], geo.Herbivore)
        assert len(j.pop_carnivores) == 9
        assert isinstance(j.pop_carnivores[-1], geo.Carnivore)

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
        s.fodder_growth()
        assert s.fodder == 300
        s.fodder = 100
        s.fodder_growth()
        assert s.fodder == 160
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
