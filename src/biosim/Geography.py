# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim import Fauna as Fa
import math
import random as rd


class BaseGeography:
    """
    A class that instantiates a cell with area type Ocean, Mountain, Desert,
    Savannah or Jungle. Area types have different qualities. The methods in
    this class and subclass describe how the animals inside a cell eat, migrate
    and mate. There are also methods for how fodder grows in a cell.
    :param: geo_p dict: default parameters
    """
    geo_p = {'f_max': None, 'alpha': None}

    @classmethod
    def set_parameter(cls, new_parameters):
        """
        This method let you set new parameters instead of the default ones
        :param new_parameters: dict with new parameters
        """
        for key in new_parameters:
            cls.geo_p[key] = new_parameters[key]

    def __init__(self):
        self.pop_herbivores = []
        self.pop_carnivores = []
        self.fodder = self.geo_p['f_max']
        self.animals_here = True

    @property
    def pop_total(self):
        """
        Current animal population in cell
        :return: list
        """
        return self.pop_carnivores + self.pop_herbivores

    @property
    def herbivore_pop(self):
        """
        :return: int: Current amount of herbivores in cell
        """
        return len(self.pop_herbivores)

    @property
    def carnivore_pop(self):
        """
        :return: int: Current amount of carnivores in cell
        """
        return len(self.pop_carnivores)

    @property
    def total_pop(self):
        """
        :return: int: Total population in a cell
        """
        return len(self.pop_total)

    def populate_cell(self, population_list):
        """
        Populate cell with a list of animals
        :param population_list: list: containing animal instances
        """
        for animal in population_list:
            if type(animal).__name__ == 'Herbivore':
                self.pop_herbivores.append(animal)
            elif type(animal).__name__ == 'Carnivore':
                self.pop_carnivores.append(animal)

    def add_animal(self, animal):
        """
        Add a single animal to the cell
        """
        if type(animal).__name__ == 'Herbivore':
            self.pop_herbivores.append(animal)
        else:
            self.pop_carnivores.append(animal)

    def remove_animals(self, population_list):
        """
        Remove a list of animals from the cell
        :param population_list: list of animal instances
        """
        for animal in population_list:
            if type(animal).__name__ == 'Herbivore':
                self.pop_herbivores.remove(animal)
            elif type(animal).__name__ == 'Carnivore':
                self.pop_carnivores.remove(animal)

    def animals_die(self):
        """
        Method removes the dead animals from a cell
        """
        for herb in self.pop_herbivores[::-1]:
            if herb.check_death():
                self.pop_herbivores.remove(herb)
        for carn in self.pop_carnivores[::-1]:
            if carn.check_death():
                self.pop_carnivores.remove(carn)

    def propensity_herb(self):
        """
        Find the propensity of the cell for herbivores
        :return: int: propensity
        """
        if isinstance(self, Ocean) or isinstance(self, Mountain):
            return 0
        else:
            e_k = self.fodder / ((self.herbivore_pop + 1) *
                                 Fa.Herbivore().p['F'])
            return math.exp(Fa.Herbivore().p['landa'] * e_k)

    def propensity_carn(self):
        """
        Find the propensity of the cell for carnivores
        :return: int: propensity
        """
        if isinstance(self, Ocean) or isinstance(self, Mountain):
            return 0
        else:
            e_k = self.get_herb_weight() / ((self.carnivore_pop + 1) *
                                            Fa.Carnivore().p['F'])
            return math.exp(Fa.Herbivore().p['landa'] * e_k)

    def check_migration(self):
        """
        Method that checks if animals in cell can migrate to another cell.
        :return: list: animals ready to migrate
        """
        migrating_animals = []
        for animal in self.pop_total:
            if animal.animal_moved is False:
                prob_move = animal.p['mu'] * animal.fitness
                if rd.random() < prob_move:
                    migrating_animals.append(animal)
        return migrating_animals

    def fodder_eaten(self):
        """
<<<<<<< HEAD
        A method that removes the fodder that gets eaten by the herbivores
        fodder: Amount of fodder in cell
        :return: appetite, ate: How much fodder the animal ate
        """
        appetite = Fa.Herbivore.p['F']

        if appetite <= self.fodder:
            self.fodder -= appetite
            return appetite
        elif 0 < self.fodder < appetite:
            ate = self.fodder
            self.fodder = 0
            return ate
        else:
            return 0

    @staticmethod
    def sort_animal_fitness(population):
        """
        Sorts the herbivores and carnivores in the cell in order of fitness
        :return: sorted list
        """
        population.sort(key=lambda animal: animal.fitness, reverse=True)
        return population

    def herbivore_eat(self):
        """
        All the herbivores in cell eat fodder if available
        """
        self.sort_animal_fitness(self.pop_herbivores)
        for animal in self.pop_herbivores:
            animal.eat(self.fodder_eaten())

    def carnivore_eat(self):
        """
        All the carnivores in cell tries to eat herbivores in cell. Fittest
        carnivore is first to go. Herbivores are removed if carnivore is
        successful
        """
        self.sort_animal_fitness(self.pop_carnivores)
        self.sort_animal_fitness(self.pop_herbivores)
        for carnivore in self.pop_carnivores:
            self.pop_herbivores = carnivore.eat(self.pop_herbivores)

    def get_herb_weight(self):
        """
        Method to get the combined weight of all the herbivores in the cell
        used for calculating propensity
        :return: int
        """
        herb_weight = 0
        for herb in self.pop_herbivores:
            herb_weight += herb.weight
        return herb_weight

    def animal_mating(self):
        """
        All the animals in the cell try to mate and newborns are added to
        population if successful
        :return:
        """
        herb_born = []
        for animal in self.pop_herbivores:
            if animal.check_birth(self.herbivore_pop):
                potential_herb = Fa.Herbivore()
                if animal.p['xi'] * potential_herb.weight > animal.weight:
                    continue
                else:
                    herb_born.append(potential_herb)
                    animal.weight -= animal.p['xi'] * potential_herb.weight

        carn_born = []
        for animal in self.pop_carnivores:
            if animal.check_birth(self.carnivore_pop):
                potential_carn = Fa.Carnivore()
                if animal.p['xi'] * potential_carn.weight > animal.weight:
                    continue
                else:
                    carn_born.append(potential_carn)
                    animal.weight -= animal.p['xi'] * potential_carn.weight

        self.pop_herbivores.extend(herb_born)
        self.pop_carnivores.extend(carn_born)

    def age_weightloss(self):
        """
        Animals in cell updates age and weight each year
        """
        for animal in (self.pop_carnivores + self.pop_herbivores):
            animal.aging()
            animal.weight_decrease()

    def fodder_growth(self):
        """
        Fodder grows depending on area type each year. Jungle is restored to
        max, while fodder in savannah grows grows according to formula below
        """
        if isinstance(self, Jungle):
            self.fodder = self.geo_p['f_max']
        elif isinstance(self, Savannah):
            self.fodder += self.geo_p['alpha'] * (self.geo_p['f_max']
                                                  - self.fodder)
        else:
            self.fodder = 0


class Jungle(BaseGeography):
    """
    Cell where carnivores hunt herbivores and herbivores eat fodder.
    Fodder replenishes each year to max.
    """
    geo_p = {'f_max': 800}

    def __init__(self):
        super().__init__()


class Savannah(BaseGeography):
    """
    A savannah cell that holds fodder, but can suffer overgrazing. Carnivores
    hunt herbivores here and herbivores eat fodder.
    """
    geo_p = {'f_max': 300, 'alpha': 0.3}

    def __init__(self):
        super().__init__()


class Desert(BaseGeography):
    """
    Area type that holds no fodder, but animals can inhabit the cells.
    Carnivore hunt herbivores here
    """
    geo_p = {'f_max': 0}

    def __init__(self):
        super().__init__()


class Ocean(BaseGeography):
    """
    Ocean cell holds no fodder and no animals are allowed to move or placed
    here. Ocean cell types are passive in this simulation
    """
    def __init__(self):
        super().__init__()
        self.animals_here = False


class Mountain(BaseGeography):
    """
    Mountain cell holds no fodder and no animals are allowed to move or placed
    here. Mountain cell types are passive in this simulation
    """
    def __init__(self):
        super().__init__()
        self.animals_here = False


if __name__ == "__main__":
    j = Jungle()
    herbs = [Fa.Herbivore(age=60, weight=50), Fa.Herbivore(age=100, weight=55),
             Fa.Herbivore(age=70, weight=60)]
    carns = [Fa.Carnivore(weight=100), Fa.Carnivore(weight=100)]
    j.populate_cell(herbs)
    j.populate_cell(carns)
    rd.seed(5)
    """print(rd.random())
    print(rd.random())
    print(rd.random())
    print(rd.random())
    print(rd.random())
    print(rd.random())"""

    j.carnivore_eat()
    print(j.herbivore_pop)
    print(j.carnivore_pop)

    """
    print(a)
    j = Jungle()
    l = [Herbivore(), Herbivore(), Carnivore(), Herbivore(), Carnivore()]
    j.populate_cell(l)
    print(j.herbivore_pop())
    print(j.carnivore_pop())

    
    j = Jungle()
    j.add_animal(Herbivore(age=0, weight=40))
    j.add_animal(Herbivore(age=5, weight=27))
    j.add_animal(Herbivore(age=50, weight=83))
    j.add_animal(Herbivore(age=25, weight=35))
    j.add_animal(Herbivore(age=18, weight=60))
    j.add_animal(Herbivore(age=10, weight=45))

    j.add_animal(Carnivore(age=5, weight=40))
    j.add_animal(Carnivore(age=5, weight=40))

    print(j.herbivore_pop())
    print(j.carnivore_pop())
    j.animal_mate()
    print(j.herbivore_pop())
    print(j.carnivore_pop())

    print(Herbivore().p['F'])
    j = Jungle()
    for animal in range(100):
        j.add_animal(Herbivore(age=60, weight=10))
    j.add_animal(Carnivore(age=4, weight=80))
    j.add_animal(Carnivore(age=5, weight=40))
    j.carnivore_eat()
    print(len(j.pop_herbivores))
    print(j.pop_carnivores[0].weight)
    print(j.pop_carnivores[1].weight)
    # j.animal_mate()
    # print(len(j.pop_herbivores))

    j = Jungle()
    for animal in range(10):
        j.add_animal(Herbivore(weight=10))
    j.add_animal(Carnivore(age=4, weight=40))
    print(len(j.pop_herbivores))
    print(len(j.pop_carnivores))
    #print((j.pop_carnivores[0].fitness - j.pop_herbivores[0].fitness) / 10)
    #print(j.pop_carnivores[0].weight)
    #j.sort_animal_fitness(j.pop_herbivores)
    print(len(j.pop_herbivores))
    j.carnivore_eat()
    print(j.pop_carnivores[0].weight)
    print(len(j.pop_herbivores))
    """

    """j = Jungle()
    j.fodder = 5
    print(j.fodder)
    print(j.fodder_eaten())
    j.fodder_eaten()
    print(j.fodder)
    print(j.fodder_eaten())"""

    """
    j = Jungle()
    j.add_animal(Herbivore(weight=10))
    j.add_animal(Herbivore(weight=5))
    print(j.fodder)
    print(j.pop_herbivores[0].get_weight())
    print(j.pop_herbivores[1].get_weight())
    j.herbivore_eat()
    print(j.fodder)
    print(j.pop_herbivores[0].get_weight())
    print(j.pop_herbivores[1].get_weight())
"""

    """jung = Jungle()
    jung.add_animal(Herbivore(weight=0))
    jung.add_animal(Herbivore())
    print(len(jung.pop_herbivores))
    jung.remove_animals()
    print(len(jung.pop_herbivores))
    herb = Herbivore(age=20, weight=50)
    print(herb.check_death())"""

    # new = {'f_max': 1000, 'alpha': 500}
    # jung.set_parameter(new)
    # print(jung.geo_p['f_max'])
    # print(jung.fodder)
    # jung.add_animal(Herbivore())
    # print(len(jung.pop_herbivores))
    # g = geo.add_animal(Herbivore())
    # print(geo.herbivores)
    """jung = Jungle()
    herb = [Herbivore(), Herbivore(weight=0), Herbivore()]
    print(herb)
    jung.sort_animal_fitness(herb)
    print(herb)"""
