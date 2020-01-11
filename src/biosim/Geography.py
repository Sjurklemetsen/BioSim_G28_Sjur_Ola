# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim.Fauna import *


class Geography:
    """
    A class that contain cell with a certain area type and with an animal
    inside it
    The methods in this class and subclass describe how the animals inside a
    cell eat, migrate and mate. There are also methods for how fodder grows in
    a cell.
    """
    geo_p = {'f_max': None, 'alpha': None}

    def set_parameter(self, new_parameters):
        """
        This method let you set new parameters instead of the default ones
        :param new_parameters: dictionary with new parameters
        """
        for key in new_parameters:
            self.geo_p[key] = new_parameters

    def __init__(self):
        self.pop_herbivores = []
        self.pop_carnivores = []
        self.fodder = 0

    def add_animal(self, animal):
        """
        Add an instance of the animal class to the list of herbivores or
        carnivores.
        :param animal: An instance of the Fauna subclasses
        """
        if type(animal).__name__ == 'Herbivore':
            self.pop_herbivores.append(animal)
        elif type(animal).__name__ == 'Carnivore':
            self.pop_carnivores.append(animal)

    def remove_animals(self):
        """
        This method removes the dead animals from a cell
        """
        for animal in self.pop_herbivores:
            if animal.check_death():
                self.pop_herbivores.pop(animal)
        for animal in self.pop_carnivores:
            if animal.check_death():
                self.pop_carnivores.pop(animal)

    def herbivore_pop(self):
        """
        :return: How many herbivores in a cell
        """
        return len(self.pop_herbivores)

    def carnivore_pop(self):
        """
        :return: How many carnivores in a cell
        """
        return len(self.pop_carnivores)

    def total_pop(self):
        """
        :return: Total population in a cell
        """
        return len(self.pop_herbivores) + len(self.pop_carnivores)

    def remove_fodder(self):
        """
        A method that removes the fodder that gets eaten by the animals
        :return: appetite - How much fodder the animal eat
        """
        appetite = Herbivore.p['F']

        if appetite <= self.fodder:
            self.fodder -= appetite
            return appetite
        elif 0 < self.fodder < appetite:
            self.fodder = 0
            appetite = self.fodder
            return appetite
        else:
            return 0

    def herbivore_eat(self):
        """
        All the herbivores in the cell eat fodder
        :return:
        """
        for animal in self.pop_herbivores:
            animal.eat()
            self.remove_fodder()

    def sort_animal_fitness(self, population):
        """
        Sort the herbivores in the cell after their fitness
        :return:
        """
        pass

    def carnivore_eat(self):
        """
        Carnivore eat
        :return: 
        """
        self.sort_animal_finess(self.pop_carnivores)
        self.sorted_herbivores()
        for animal in self.pop_carnivores:
            elf.sorted_herbivores()
            animal.eat(weight killed animal) # Carnivore eat and gain weight
            self.sorted_herbivores()
            self.herbivore_pop().pop[-1] # Herbivore with worst fitness die
        pass

class Jungle(Geography):
    """
    A jungle cell where carnivore can hunt herbivore and herbivore can eat food
    Fodder replenish each year to f_max.
    """
    geo_p = {'f_max': 800}

    def __init__(self):
        super().__init__()
        self.fodder = self.geo_p['f_max']

    def fodder_growth(self):
        """
        Replenishes fodder each year
        :return:
        """
        self.fodder = self.f_max
        pass

    def fodder_eaten(self, fodder_eaten):
        """
        A method that removes the fodder that gets eaten by the animals
        :return:
        """
        self.fodder -= fodder_eaten
    pass



class Savannah(Geography):
    """
    A savannah cell that holds fodder, but can suffer overgrazing
    """
    geo_p = {'f_max': 300, 'alpha': 0.3}

    def __init__(self):
        super().__init__(self)

    def get_fodder(self):
        pass

    def fodder_growth(self):
        """
        Fodder growth for savannah
        :return:
        """
        pass


class Desert(Geography):
    """
    Area type that holds no fodder, but animals can inhabit the cells
    """

    def __init__(self):
        super().__init__(self)
        pass
    pass


class Ocean(Geography):
    """
    A Ocean. No fodder and no animals are allowed to move here
    Ocean cell types are passive in this simulation
    """

    def __init__(self):
        super().__init__(self)
    pass


class Mountain:
    """
    A Mountain cell. No fodder and no animals are allowed to move here
    Mountain cell types are passive in this simulation
    """
    f_max = None

    def __init__(self):
        super().__init__(self)
        pass
    pass




if __name__ == "__main__":
    geo = Geography()
    g = geo.add_animal(Herbivore())
    print(geo.herbivores)
