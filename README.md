# Carl and Zack's Machine Learning Final Project

### Proposal

Our idea for the major project for this course is to create a simulation using genetic algorithms in which two species of animals will compete for survival to mimic the scientific theory of natural selection.

### Design

The algorithm will run either for a set number of generations or until one species has gone extinct.

Each generation will be a literal generation of the species in which new offspring will be generated and the old generation will die out.

Each species will have certain attributes (such as speed, vision, size, fertility, strength, color, energy, etc).

We’ll start using a 2D pixel grid system and, if time allows, expand to 3D.

Because we are using a genetic algorithm, we will use no training data, but rather a fitness function yet to be defined.

### Thoughts

The hardest part of this assignment will probably be fine tuning the genes that we will use for each species so that one does not quickly dominate the other. We will also need to play around with the environment (food, obstacles, water, etc).

# How to Run

You need to install the `pyxel` python module with `pip install pyxel`. This is for the graphics processing of the simulation.

Run the program by typing `pyxel run genertic_algorithm.py`

# TODO:

-   Move drawing functionality off into the classes
-   Optimize the runtime with local searching (use timer to verify)
-   Color the top 5 individuals
-   Somehow track energy...?
-   See if the population can be generated differently
-   Get rid of the dead people in the calculations and in the visualization
-   Food should not spawn on top of creatures ever (should respawn the food if it tries to do that)
-   Create const booleans for display options (display lines, sense grid, etc)
