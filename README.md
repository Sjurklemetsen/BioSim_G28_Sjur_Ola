# Modelling the ecosystem at Rossumøya
This project is a simulation of the dynamic population and landscape of Rossumøya.
The simulation has been made by two students who attend Norwegian University of Life Science.
The project was written as a school project in january 2020.
In this simulation the island has been split into many cells, each with a different area type.
In these cells live animals who prey on each other and eat what fodder the landscape
has to offer. In this simulation the landscape and animals goes through a yearly cycle
where they interact with each other in many different ways. 

## Geography
The island has been split into many cells, where each cell is either ocean, mountain, 
desert, savannah or jungle. In the geography class all the information about the cells are
stored. No animals are permitted in ocean and mountain cells. There is only fodder for herbivores in 
savannah and jungle cells, but carnivores can hunt in every cell where there is animals. 
Geography is the baseclass, and each of the landscapes are subclasses. To make BaseGeography class
we imported all the methods and class from Fauna module. 

## Fauna
Each cell has many instances of an animal from the fauna. There are two kinds of animals in
the fauna: Herbivore and carnivore. Herbivore eat the fodder that grows in the jungle and 
savannah and the carnivore prey on the herbivore. Herbivore and carnivore are two subclasses
from the baseclass fauna. In the fauna class everything that concerns a specific animal is 
stored. For example how much a certain animal weighs, what his chances are of eating or 
if he is going to die that year or not. Each animal has a certain age, weight and fitness 
that is calculated out from those values. 

## Map
All the cells together make up the map. In this class every method that concerns the cells are stored at the
same time. The animals migrate to different cells and a method for simulating an annual cycle on the island is 
also stored here. To create the map we use the BaseFauna class, BaseGeography class and all their subclasses.

## Simulation
In this module we have the BioSim class. in this class the simulation is run several years, and 
results are plotted in graphs. In simulation every class from the other modules is used. 










