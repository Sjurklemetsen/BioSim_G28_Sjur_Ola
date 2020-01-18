# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.biosim import Fauna as fa
from src.biosim import Geography as geo
from src.biosim import Map as ma
import random as rd

class BioSim:
    def __init__(
        self,
        island_map,
        ini_pop,
        seed,
        ymax_animals=None,
        cmax_animals=None,
        img_base=None,
        img_fmt="png",
    ):
        rd.seed(seed)
        self.island = ma.Map(island_map)
        self.add_population(ini_pop)

        ini_herbs = [{’loc’: (10, 10),
        ’pop’: [{’species’: ’Herbivore’,
        ’age’: 5,
        ’weight’: 20}
        for _ in range(150)]}]
        ini_carns = [{’loc’: (10, 10),
        ’pop’: [{’species’: ’Carnivore’,
        ’age’: 5,
        ’weight’: 20}
        for _ in range(40)]}]

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
            fa.Herbivore.set_parameter(params)
        elif species == 'Carnivore':
            fa.Carnivore.set_parameter(params)

    def set_landscape_parameters(self, landscape, params):
        """
        Set parameters for landscape type.

        :param landscape: String, code letter for landscape
        :param params: Dict with valid parameter specification for landscape
        """
        if landscape == 'J':
            geo.Jungle.set_parameter(params)
        elif landscape == 'S':
            geo.Savannah.set_parameter(params)

    def simulate(self, num_years, vis_years=1, img_years=None):
        """
        Run simulation while visualizing the result.

        :param num_years: number of years to simulate
        :param vis_years: years between visualization updates
        :param img_years: years between visualizations saved to files (default: vis_years)

        Image files will be numbered consecutively.
        """

    def add_population(self, population):
        """
        Add a population to the island

        :param population: List of dictionaries specifying population
        """
        for dict in population:



        populate_map(coord, population)


    @property
    def year(self):
        """Last year simulated."""

    @property
    def num_animals(self):
        """Total number of animals on island."""

    @property
    def num_animals_per_species(self):
        """Number of animals per species in island, as dictionary."""

    @property
    def animal_distribution(self):
        """Pandas DataFrame with animal count per species for each cell on island."""

    def make_movie(self):
        """Create MPEG4 movie from visualization images saved."""


if __name__ == "__main__":
    geo = """
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
    OOOOOOOOOOOOOOOOOOOOO
    """
    ini_herbs = [{'loc': (10,10),
                  'pop': [{'species': 'Herbivore',
                               'age': 5,
                               'weight': 20}
                              for _ in range(150)]}]
    ini_carns = [{'loc': (10, 10),
                  'pop': [{'species': 'Carnivore',
                           'age': 5,
                           'weight': 20}
                          for _ in range(40)]}]
    sim = BioSim(geo, ini_herbs, seed=123456)
    #sim.set_animal_parameters()
    #sim.set_landscape_parameters()
    sim.add_population()