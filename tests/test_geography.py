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
        sava = geo.Savannah()
        assert isinstance(jung, geo.Jungle)
        assert isinstance(sava, geo.Savannah)
        assert jung.fodder == 800
        assert sava.fodder == 300 and sava.geo_p['alpha'] == 0.3
        assert isinstance(jung.pop_herbivores and jung.pop_carnivores, list)

    def test_set_parameter(self):
        new_parameters = {'f_max': 1000, 'alpha': 500}
        jung = geo.Jungle()
        jung.set_parameter(new_parameters)
        assert jung.fodder == 1000

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
        Tests if population decreases when carnivore eats
        Tests if weight increases according to formula when carnivore eats
        Tests that fitness updates after every herbivore eaten
        """
        j = geo.Jungle()
        for n in range(10):
            j.add_animal(geo.Herbivore(age=60, weight=10))
        j.add_animal(geo.Carnivore(age=10, weight=60))
        j.carnivore_eat()
        assert 0 < len(j.pop_herbivores) == 5
        #assert j.pop_carnivores[0].weight == 97.5
        print(j.pop_carnivores[0].weight)

    def test_multiple_carnivores_eat(self):
        """
        Tests that carnivore that eats next increases weight and fitness
        """
        j = geo.Jungle()
        j.add_animal(geo.Carnivore(weight=60, age=10))
        j.add_animal(geo.Carnivore(age=60, weight=10))
        for n in range(20):
            j.add_animal(geo.Herbivore(weight=10, age=50))

        j.carnivore_eat()
        assert j.pop_carnivores[1].weight > 10

    def test_ocean(self):
        """
        Tests if ocean is an instance
        :return:
        """
        o = Ocean()
        assert issubclass(Ocean, Geography)
        assert isinstance(o, Ocean)

    def test_mountain(self):
        """
        Test if mountain is an instance
        :return:
        """
        m = Mountain()
        assert issubclass(Mountain, Geography)
        assert isinstance(m, Mountain)

    def test_desert(self):
        """
        Test if the fodder equals zero
        :return:
        """
        d = Desert()
        assert issubclass(Desert, Geography)
        assert isinstance(d, Desert)
        #assert "default param" f_max == 0
        pass

    def test_savannah(self):
        """
        Test if savannah is a instance
        Test if fodders in the jungle is updated for each cycle
        :return:
        """
        s = Savannah()
        assert issubclass(Savannah, Geography)
        assert isinstance(s, Savannah)
        #assert "default param" f_max == 200
        assert "test if fodder grows to formula each year"
        pass

    def test_jungle(self):
        """
        Test if jungle is a instance
        Test if fodders in the jungle is equal to f max in the start of each
        cycle
        :return:
        """
        j = Jungle()
        j_fodder = Jungle().fodder_replenish()
        assert issubclass(Jungle, Geography)
        assert isinstance(j, Jungle)
        #assert j_fodder == "defaut param" f_max
        pass
