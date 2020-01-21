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
import numpy as np
import subprocess
import os

FFMPEG_BINARY = r'C:/Users/sjurk/OneDrive/Dokumenter/Skole/INF200/Movie' \
                r'/ffmpeg-20200115-0dc0837-win64-static/ffmpeg-20200115' \
                r'-0dc0837-win64-static/bin/ffmpeg.exe'

DEFAULT_GRAPHICS_DIR = os.path.join('..', 'data')
DEFAULT_GRAPHICS_NAME = 'dv'
DEFAULT_MOVIE_FORMAT = 'mp4'


class BioSim:
    def __init__(
            self,
            island_map,
            ini_pop,
            seed,
            ymax_animals=None,
            cmax_animals=None,
            img_base=None,
            img_fmt="png"
    ):
        rd.seed(seed)
        self.island_map = island_map
        self.map = Ma.Map(island_map)
        self.add_population(ini_pop)
        self.ymax_animals = ymax_animals
        self._year = 0

        if cmax_animals is None:
            self.cmax_animals = {}

        # For saving images and simulation
        self.img_ctr = 0
        self.final_year = None
        self.img_fmt = img_fmt
        if img_base is None:
            self.img_base = os.path.join('..', 'BioSim')

        # For different graphics
        self.fig = None
        self.ax_year = None
        self.ax_map = None
        self.ax_line = None
        self.ax_heat_h = None
        self.ax_heat_c = None
        self.herb_density = None
        self.carn_density = None
        self.map_geo = None
        self.line_herb = None
        self.line_carn = None
        self.year_plot = None
        self.final_year = None
        self.carn_y = []
        self.herb_y = []
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
        data = {}
        rows = []
        col = []
        herbs = []
        carns = []
        for coord, cell in self.map.island.items():
            herbs.append(cell.herbivore_pop)
            carns.append(cell.carnivore_pop)
            rows.append(coord[0])
            col.append(coord[1])
        data['Row'] = rows
        data['Col'] = col
        data['Herbivore'] = herbs
        data['Carnivore'] = carns
        return pd.DataFrame(data)

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

        self.ax_map.imshow(island_map, interpolation='nearest')
        self.ax_map.set_xticks(range(len(island_map[0])))
        self.ax_map.set_xticklabels(range(0, 1 + len(island_map[0])))
        self.ax_map.set_yticks(range(len(island_map)))
        self.ax_map.set_yticklabels(range(0, 1 + len(island_map)))

        """for ix, name in enumerate(('Ocean', 'Mountain', 'Jungle',
                                   'Savannah', 'Desert')):
            self.ax_map.add_patch(plt.Rectangle((0., ix * 0.2), 0.3, 0.1,
                                         edgecolor='none',
                                         facecolor=color_code[name[0]]))
            self.ax_map.text(0.35, ix * 0.2, name, transform=axlg.transAxes)
    
"""

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

    def update_population_plot(self):
        n_herb, n_carn = self.num_animals_per_species.values()
        self.herb_y.append(n_herb)
        self.carn_y.append(n_carn)
        self.ax_line.plot(range(self.year + 1), self.herb_y,
                          'g', self.carn_y, 'r')
        self.ax_line.legend(['Herbivore', 'Carnivore'])


    def heat_map_herbivore(self):
        """
        A method that shows the population in each cell by showing colors
        :return:
        """

        herb_cell = self.animal_distribution.pivot('Row', 'Col', 'Herbivore')

        self.herb_density = self.ax_heat_h.imshow(herb_cell, interpolation='nearest', cmap='Greens')
        self.ax_heat_h.set_title('Herbivore population density')

    def heat_map_carnivore(self):

        carn_cell = self.animal_distribution.pivot('Row', 'Col', 'Carnivore')

        self.herb_density = self.ax_heat_c.imshow(carn_cell, interpolation='nearest', cmap='Reds')
        self.ax_heat_c.set_title('Carnivore population density')


    def year_count(self):
        pass
        #self.year_plot = self.ax_year.text(8, 8, f'Year: {self.year}')

    def update_all(self):
        self.heat_map_carnivore()
        self.heat_map_herbivore()
        self.year_count()
        self.update_population_plot()
        plt.pause(1e-6)

    def simulate(self, num_years, vis_years=1, img_years=None):
        """
        Run simulation while visualizing the result.
        :param num_years: number of years to simulate
        :param vis_years: years between visualization updates
        :param img_years: years between visualizations saved to files (default: vis_years)

        Image files will be numbered consecutively.
        """
        if img_years is None:
            img_years = vis_years

        self.final_year = self._year + num_years
        self.setup_graphics()

        while self._year < self.final_year:

            if self.num_animals == 0:
                break

            if self._year % vis_years == 0:
                self.update_all()

            if self._year % img_years == 0:
                self.save_graphic()
            self._year += 1
            self.map.annual_cycle()

        """for year in range(num_years):
            self.map.annual_cycle()
            self._year += 1"""

    def setup_graphics(self):

        if self.fig is None:
            self.fig = plt.figure()

        #if self.year_plot is None:
            #self.ax_year =
            #self.year_count()

        if self.ax_map is None:
            self.ax_map = self.fig.add_subplot(221)

            #self.ax_map = self.fig.add_axes([0.04, 0.45, 0.45, 0.6])
            self.standard_map()

        if self.herb_density is None:
            self.ax_heat_h = self.fig.add_subplot(223)

            #self.ax_heat_h = self.fig.add_axes([0.04, 0.0, 0.45, 0.6])
            self.heat_map_herbivore()

        if self.carn_density is None:
            self.ax_heat_c = self.fig.add_subplot(224)

            #self.ax_heat_c = self.fig.add_axes([0.54, 0.0, 0.45, 0.6])
            self.heat_map_carnivore()

        if self.ax_line is None:
            self.ax_line = self.fig.add_subplot(322)
            if self.ymax_animals is not None:
                self.ax_line.set_ylim(0, self.ymax_animals)
            self.ax_line.set_xlim(0, self.final_year + 1)
            self.ax_line.set_title('Populations')


    def save_graphic(self):
        if self.img_base is None:
            return

        plt.savefig('{base}_{num:05d}.{type}'.format(base=self.img_base,
                                                     num=self.img_ctr,
                                                     type=self.img_fmt))
        self.img_ctr += 1

    def make_movie(self, movie_fmt=DEFAULT_MOVIE_FORMAT):
        """Create MPEG4 movie from visualization images saved."""
        if self.img_base is None:
            raise RuntimeError("No filename defined.")

        if movie_fmt == 'mp4':
            try:
                # Parameters chosen according to http://trac.ffmpeg.org/wiki/Encode/H.264,
                # section "Compatibility"
                subprocess.check_call([FFMPEG_BINARY,
                                       '-i',
                                       '{}_%05d.png'.format(self.img_base),
                                       '-y',
                                       '-profile:v', 'baseline',
                                       '-level', '3.0',
                                       '-pix_fmt', 'yuv420p',
                                       '{}.{}'.format(self.img_base,
                                                      movie_fmt)])
            except subprocess.CalledProcessError as err:
                raise RuntimeError('ERROR: ffmpeg failed with: {}'.format(err))


if __name__ == "__main__":

    Geo = """\
             OOOOOOO
             OJSSDDO
             OJSDDOO
             OOOOOOO"""

    ini_herbs = [{'loc': (1, 1),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 10}
                          for _ in range(200)]}]
    ini_carns = [{'loc': (2, 2),
                  'pop': [{'species': 'Carnivore',
                           'age': 5,
                           'weight': 60}
                          for _ in range(20)]}]
    sim = BioSim(Geo, ini_herbs, seed=123456)
    sim.add_population(ini_carns)
    sim.simulate(20)

    #print(sim.num_animals_per_species)
    #sim.plot_island_population()
    #sim.heat_map_herbivore()
    #sim.heat_map_carnivore()
    #sim.heat_map_carnivore()
    #sim.setup_graphics()
    #sim.standard_map()



