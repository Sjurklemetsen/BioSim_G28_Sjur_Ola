# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim import Fauna as Fa
from src.biosim import Geography as Geo
from src.biosim import Map as Ma
import random as rd
import pandas as pd
from matplotlib import colors
import matplotlib.pyplot as plt
import textwrap


class BioSim:
    def __init__(
            self,
            island_map,
            ini_pop,
            seed):
        """
        ymax_animals=None,
        cmax_animals=None,
        img_base=None,
        img_fmt="png",
        """
        self.island_map = island_map
        rd.seed(seed)
        self.map = Ma.Map(island_map)
        self.add_population(ini_pop)
        self._year = 0
        self.island_map = island_map

        """
        :param island_map: Multi-line string specifying island geography
        :param ini_pop: List of dictionaries specifying initial population
        :param seed: Integer used as random number seed
        :param ymax_animals: Number specifying y-axis limit for graph showing animal numbers
        :param cmax_animals: Dict specifying color-code limits for animal densities
        :param img_base: String with beginning of file name for figures, including path
        :param img_fmt: String with file type for figures, e.g. 'png'

        If ymax_animals is None, the y-axis limit should be adjusted automatically.

        If cmax_animals is None, sensible, fixed default values should be used.
        cmax_animals is a dict mapping species names to numbers, e.g.,
           {'Herbivore': 50, 'Carnivore': 20}

        If img_base is None, no figures are written to file.
        Filenames are formed as

            '{}_{:05d}.{}'.format(img_base, img_no, img_fmt)

        where img_no are consecutive image numbers starting from 0.
        img_base should contain a path and beginning of a file name.
        """

    def set_animal_parameters(self, species, params):
        """
        Set parameters for animal species.

        :param species: String, name of animal species
        :param params: Dict with valid parameter specification for species
        """
        if species == 'Herbivore':
            Fa.Herbivore.set_parameter(params)
        elif species == 'Carnivore':
            Fa.Carnivore.set_parameter(params)

    def set_landscape_parameters(self, landscape, params):
        """
        Set parameters for landscape type.

        :param landscape: String, code letter for landscape
        :param params: Dict with valid parameter specification for landscape
        """
        if landscape == 'J':
            Geo.Jungle.set_parameter(params)
        elif landscape == 'S':
            Geo.Savannah.set_parameter(params)

    def standard_map(self):
        island_string = self.island_map
        string_map = textwrap.dedent(island_string)
        string_map.replace('\n', ' ')

        color_code = {'O': colors.to_rgb('aqua'),
                      'M': colors.to_rgb('grey'),
                      'J': colors.to_rgb('forestgreen'),
                      'S': colors.to_rgb('yellowgreen'),
                      'D': colors.to_rgb('khaki')}

        island_map = [[color_code[column] for column in row]
                      for row in string_map.splitlines()]
        return island_map

        fig = plt.figure()
        axim = fig.add_axes([0.05, 0.5, 0.4, 0.5])  # llx, lly, w, h
        axim.imshow(island_map)
        axim.set_xticks(range(len(island_map[0])))
        axim.set_xticklabels(range(0, 1 + len(island_map[0])))
        axim.set_yticks(range(len(island_map)))
        axim.set_yticklabels(range(0, 1 + len(island_map)))

        axlg = fig.add_axes([0.46, 0.7, 0.06, 0.2])  # llx, lly, w, h
        axlg.axis('off')
        for ix, name in enumerate(('Ocean', 'Mountain', 'Jungle',
                                   'Savannah', 'Desert')):
            axlg.add_patch(plt.Rectangle((0., ix * 0.2), 0.3, 0.1,
                                         edgecolor='none',
                                         facecolor=color_code[name[0]]))
            axlg.text(0.35, ix * 0.2, name, transform=axlg.transAxes)

        plt.show()


        """
        map_colors = []
        for coord, cell in self.map.island.items():
            if cell.__name__ == 'Ocean':
                map_colors.append(coord, map_colors['O'])
            elif cell.__name__ == 'Mountain':
                map_colors.append([coord, map_colors['M'])

        [((0,2),  ]

        fig = plt.figure()
        """

    def plot_island_population(self):
        """
        This method generate a plot of the population on the island
        :return:
        """
        pass

    def update_map(self):
        """
        Update the map plot each year
        :return:
        """
        pass

    def heat_map(self):
        """
        A method that shows the population in each cell by showing colors
        :return:
        """
        """
        :return: 
        """
        pass

    def simulate(self, num_years, vis_years=1, img_years=None):
        """
        Run simulation while visualizing the result.
        :param num_years: number of years to simulate
        :param vis_years: years between visualization updates
        :param img_years: years between visualizations saved to files (default: vis_years)

        Image files will be numbered consecutively.
        """
        for year in range(num_years):
            self.map.annual_cycle()
            self._year += 1

    def add_population(self, population):
        """
        Add a population to the island

        :param population: List of dictionaries specifying population
        """
        for dicti in population:
            location = dicti['loc']
            self.map.check_input_in_sim(location)
            population_list = []
            for popu in dicti['pop']:
                if popu['age'] < 0 or popu['weight'] <= 0:
                    raise ValueError('''Age must be a non negative number and 
                    weight must be a positive number''')
                if popu['species'] == 'Herbivore':
                    population_list.append(Fa.Herbivore(age=popu['age'],
                                                        weight=popu['weight']))
                elif popu['species'] == 'Carnivore':
                    population_list.append(Fa.Carnivore(age=popu['age'],
                                                        weight=popu['weight']))
                else:
                    raise ValueError('That is not a species ')
            self.map.populate_map(location, population_list)

    @property
    def year(self):
        return self._year

    @property
    def num_animals(self):
        """Total number of animals on island."""
        num_animals = 0
        for coord, cell in self.map.island.items():
            num_animals += cell.total_pop
        return num_animals

    @property
    def num_animals_per_species(self):
        """Number of animals per species in island, as dictionary."""
        num_animals_per_species = {}
        herb = 0
        carn = 0
        for coord, cell in self.map.island.items():
            herb += cell.herbivore_pop
            carn += cell.carnivore_pop
        num_animals_per_species['Herbivore'] = herb
        num_animals_per_species['Carnivore'] = carn
        return num_animals_per_species

    @property
    def animal_distribution(self):
        """Pandas DataFrame with animal count per species for
         each cell on island."""
        data = {'Coordinates': list(self.map.island.keys())}
        herbs = []
        carns = []
        for coord, cell in self.map.island.items():
            herbs.append(cell.herbivore_pop)
            carns.append(cell.carnivore_pop)
        data['Herbivore'] = herbs
        data['Carnivore'] = carns
        return pd.DataFrame(data)


    def make_movie(self):
        """Create MPEG4 movie from visualization images saved."""


if __name__ == "__main__":

    Geo = """\
             OOOOOOO
             OJJJJJO
             OJJSOOO
             OOOOOOO"""

    ini_herbs = [{'loc': (1, 1),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 10}
                          for _ in range(150)]}]
    ini_carns = [{'loc': (2, 2),
                  'pop': [{'species': 'Carnivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(40)]}]
    sim = BioSim(Geo, ini_herbs, seed=123456)
    sim.standard_map()



