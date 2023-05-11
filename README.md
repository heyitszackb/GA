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

-   Optimize the runtime with local searching (use timer to verify)
-   Color the top 5 individuals
-   Somehow track energy...?
-   See if the population can be generated differently
    Instead of picking two random parents and making a child from the most fit ones, we could have it
    select maybe 5 or 10 individuals and chose the top from those to make a child from? Or another system.
    If a person is dead there should be a low chance that the genetic material passes on.
-   Get rid of the dead people in the calculations and in the visualization (could be removed from the population array just like the food is)
-   Food should not spawn on top of creatures ever (should respawn the food if it tries to do that)
-   Create const booleans for display options (display lines, sense grid, etc)
-   Slight issue (?). All the creatures have to learn is that having both scale genes be positive is all that they need, they do not have to be closer and closer to 1 (which is fine but we might want to make it harder for them to figure it out?).
-   Use neural network to map decisions based on surroundings? (i.e. fight, eat food, move, which direction to move, etc given the current individual's stats?)
-   Interaction between genes
    When you have more energy, you get bigger and slower? So only eating when you need to is better?
    Everything is mapped through a NN and the genes are the weights between the nodes?

# NN Notes

Inputs: Closest creature to you and closest food to you (could expand to be all creatures near you and all food near you).
Outputs: Which direction to step, how much to step in that direction (more steps is exponentially more energy)

# Done

-   Move drawing functionality off into the classes
