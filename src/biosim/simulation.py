# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from biosim import Fauna as Fa
from biosim import Geography as Geo
from biosim import Map as Ma
import random as rd
import pandas as pd
import numpy as np
from matplotlib import colors
import matplotlib.pyplot as plt
import textwrap
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
        """
        :param island_map: Multi-line string specifying island geography
        :param ini_pop: List of dictionaries specifying initial population
        :param seed: Integer used as random number seed
        :param ymax_animals: Number specifying y-axis limit for graph showing
        animal numbers
        :param cmax_animals: Dict specifying color-code limits for animal
        densities
        :param img_base: String with beginning of file name for figures,
        including path
        :param img_fmt: String with file type for figures, e.g. 'png'
        """
        rd.seed(seed)
        self.island_map = island_map
        self.map = Ma.Map(island_map)
        self.add_population(ini_pop)
        self._year = 0

        if ymax_animals is None:
            self.ymax_animals = 15000
        else:
            self.ymax_animals = ymax_animals

        if cmax_animals is None:
            self.cmax_animals = {'Herbivore': 100, 'Carnivore': 50}

        # For saving images and simulation
        self.img_ctr = 0
        self.final_year = None
        self.img_fmt = img_fmt
        if img_base is None:
            self.img_base = os.path.join('..', 'BioSim')
        else:
            self.img_base = img_base

        # For different graphics
        self.fig = None
        self.ax_year = None
        self.ax_map = None
        self.ax_line = None
        self.ax_heat_h = None
        self.ax_heat_c = None
        self.herb_density = None
        self.carn_density = None
        self.ax_animal_count = None
        self.final_year = None
        self.herbivore_line = None
        self.carnivore_line = None

    @staticmethod
    def set_animal_parameters(species, params):
        """
        Sets new parameters for animal species.
        :param species: String, name of animal species
        :param params: Dict with valid parameter specification for species
        """
        if species == 'Herbivore':
            Fa.Herbivore.set_parameter(params)
        elif species == 'Carnivore':
            Fa.Carnivore.set_parameter(params)

    @staticmethod
    def set_landscape_parameters(landscape, params):
        """
        Sets new parameters for landscape type.
        :param: landscape: String, letter code specifying geography type
        :param: params: Dict with valid parameter specifying geography type
        """
        if landscape == 'J':
            Geo.Jungle.set_parameter(params)
        elif landscape == 'S':
            Geo.Savannah.set_parameter(params)

    @property
    def year(self):
        """Current year"""
        return self._year

    @property
    def num_animals(self):
        """
        Total number of animals on island.
        :return: int
        """
        num_animals = 0
        for coord, cell in self.map.island.items():
            num_animals += cell.total_pop
        return num_animals

    @property
    def num_animals_per_species(self):
        """
        Number of animals per species in island, as dictionary.
        :return: dict
        """
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
        """
        Pandas DataFrame with animal count per species for
        each cell on island.
        :return: pd dataframe: 'rows' 'columns' 'Herbivores' 'Carnivores'
        """
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
        Add a population to specific locations on the island
        :param: population: dict
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
        """
        Creates a map plot from string of the island.
        Source: Hans Ekkehard Plesser
        """
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
        self.ax_map.set_title('Geography')

        axlg = self.fig.add_axes([0.03, 0.525, 0.1, 0.4])
        axlg.axis('off')
        for ix, name in enumerate(('O', 'M', 'J',
                                   'S', 'D')):
            axlg.add_patch(plt.Rectangle((0., ix * 0.2), 0.3, 0.1,
                                         edgecolor='none',
                                         facecolor=color_code[name[0]]))
            axlg.text(0.35, ix * 0.2, name, transform=axlg.transAxes)

    def make_line_plot(self):
        """
        Creates the herbivore and carnivore interactive plot, i.e. the graph
        in the interactive graphics window showing the total number of
         herbivores on the island.
        """
        if self.herbivore_line is None:
            herb_plot = self.ax_line.plot(np.arange(
                0, self.final_year), np.full(self.final_year, np.nan))
            self.herbivore_line = herb_plot[0]
        else:
            x, y = self.herbivore_line.get_data()
            new_x = np.arange(x[-1] + 1, self.final_year)
            if len(new_x) > 0:
                new_y = np.full(new_x.shape, np.nan)
                self.herbivore_line.set_data(
                    np.hstack((x, new_x)), np.hstack((y, new_y)))

        if self.carnivore_line is None:
            carnivore_plot = self.ax_line.plot(np.arange(
                0, self.final_year), np.full(self.final_year, np.nan))
            self.carnivore_line = carnivore_plot[0]
        else:
            x, y = self.carnivore_line.get_data()
            new_x = np.arange(x[-1] + 1, self.final_year)
            if len(new_x) > 0:
                new_y = np.full(new_x.shape, np.nan)
                self.carnivore_line.set_data(
                    np.hstack((x, new_x)), np.hstack((y, new_y)))

    def update_population_plot(self):
        """
        A method that updates the population plot with new values
        :return:
        """

        n_herb, n_carn = self.num_animals_per_species.values()

        herb_y = self.herbivore_line.get_ydata()
        herb_y[self.year] = n_herb
        self.herbivore_line.set_ydata(herb_y)

        carn_y = self.carnivore_line.get_ydata()
        carn_y[self.year] = n_carn
        self.carnivore_line.set_ydata(carn_y)

    def heat_map_herbivore(self):
        """
        Creates heat map plot of carnivores on the island
        """
        herb_cell = self.animal_distribution.pivot('Row', 'Col', 'Herbivore')

        self.herb_density = self.ax_heat_h.imshow(herb_cell,
                                                  vmax=self.cmax_animals
                                                  ['Herbivore'],
                                                  interpolation='nearest',
                                                  cmap='Greens')
        self.ax_heat_h.set_title('Herbivore population density')

    def heat_map_carnivore(self):
        """
        Creates heat map plot of carnivores on the island
        """
        carn_cell = self.animal_distribution.pivot('Row', 'Col', 'Carnivore')

        self.herb_density = self.ax_heat_c.imshow(carn_cell,
                                                  vmax=self.cmax_animals
                                                  ['Carnivore'],
                                                  interpolation='nearest',
                                                  cmap='Reds')
        self.ax_heat_c.set_title('Carnivore population density')

    def update_all(self):
        """
        Updates plots for simulation
        """
        self.heat_map_carnivore()
        self.heat_map_herbivore()
        self.update_population_plot()
        self.ax_year.set_text(f'Year: {self.year}')
        self.ax_animal_count.set_text(f'Pop: {self.num_animals}')

        plt.pause(1e-6)

    def simulate(self, num_years, vis_years=1, img_years=None):
        """
        Runs simulation while visualizing the result. saves image files
        :param num_years: number of years to simulate
        :param vis_years: years between visualization updates
        :param img_years: years between visualizations saved to files (default:
        vis_years)

        Image files will be numbered consecutively.
        """
        if img_years is None:
            img_years = vis_years

        self.final_year = self._year + num_years
        self.setup_graphics()

        while self._year < self.final_year:

            if self._year % vis_years == 0:
                self.update_all()

            if self._year % img_years == 0:
                self.save_graphic()
            self._year += 1
            self.map.annual_cycle()

    def setup_graphics(self):
        """
        Sets up figure graphic for plotting each subplot simulation
        instantiated in the simulation method
        """
        if self.fig is None:
            self.fig = plt.figure()
            self.fig.suptitle('Simulation of Rossumøya', fontsize=16)
            self.fig.tight_layout()

        if self.ax_year is None:
            self.ax_year = self.fig.text(0.1, 0.9, f'Year: {self.year}',
                                         fontsize=12)

        if self.ax_animal_count is None:
            self.ax_animal_count = self.fig.text(0.84, 0.90,
                                                 f'Pop: {self.num_animals}',
                                                 fontsize=12)

        if self.ax_map is None:
            self.ax_map = self.fig.add_subplot(221)
            self.standard_map()

        if self.herb_density is None:
            self.ax_heat_h = self.fig.add_subplot(223)
            self.heat_map_herbivore()

        if self.carn_density is None:
            self.ax_heat_c = self.fig.add_subplot(224)
            self.heat_map_carnivore()

        if self.ax_line is None:
            self.ax_line = self.fig.add_subplot(2, 2, 2)
            self.ax_line.set_ylim(0, self.ymax_animals)
        self.make_line_plot()
        self.ax_line.set_xlim(0, self.final_year + 1)
        self.ax_line.set_title('Populations')

    def save_graphic(self):
        """
        Saves graphic in specified img_base
        """
        if self.img_base is None:
            return

        plt.savefig('{base}_{num:05d}.{type}'.format(base=self.img_base,
                                                     num=self.img_ctr,
                                                     type=self.img_fmt))
        self.img_ctr += 1

    def make_movie(self, movie_fmt=DEFAULT_MOVIE_FORMAT):
        """
        Create MPEG4 movie from visualization images saved.
        """
        if self.img_base is None:
            raise RuntimeError("No filename defined.")

        if movie_fmt == 'mp4':
            try:
                # Parameters chosen according to http://trac.ffmpeg.org/wiki/
                # Encode/H.264,
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


if __name__ == '__main__':
    plt.ion()
    geogr = """\
               OOOOOOOOOOOOOOOOOOOOO
               OOOOOOOOSMMMMJJJJJJJO
               OSSSSSJJJJMMJJJJJJJOO
               OSSSSSSSSSMMJJJJJJOOO
               OSSSSSJJJJJJJJJJJJOOO
               OSSSSSJJJDDJJJSJJJOOO
               OSSJJJJJDDDJJJSSSSOOO
               OOSSSSJJJDDJJJSOOOOOO
               OSSSJJJJJDDJJJJJJJOOO
               OSSSSJJJJDDJJJJOOOOOO
               OOSSSSJJJJJJJJOOOOOOO
               OOOSSSSJJJJJJJOOOOOOO
               OOOOOOOOOOOOOOOOOOOOO"""
    geogr = textwrap.dedent(geogr)

    ini_herbs = [{'loc': (10, 10),
                  'pop': [{'species': 'Herbivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(150)]}]
    ini_carns = [{'loc': (10, 10),
                  'pop': [{'species': 'Carnivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(40)]}]
    sim = BioSim(island_map=geogr, ini_pop=ini_herbs,
                 seed=123456)
    sim.set_animal_parameters('Herbivore', {'zeta': 3.2, 'xi': 1.8})
    sim.set_animal_parameters('Carnivore', {'a_half': 70, 'phi_age': 0.5,
                                            'omega': 0.3, 'F': 65,
                                            'DeltaPhiMax': 9.})
    sim.set_landscape_parameters('J', {'f_max': 700})
    sim.simulate(num_years=25, vis_years=1, img_years=2000)
    sim.add_population(population=ini_carns)
    sim.simulate(num_years=25, vis_years=1, img_years=2000)

    plt.savefig('check_sim.pdf')
    input('Press ENTER')
