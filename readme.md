

<!-- INTRODUCTION-->
## Very Brisk Introduction to 1D Cellular Automata

Cellular automata are a favourite example of how a few simple rules can lead to vast and complex behavour.  

A singular 1D cellular automaton is a 'cell' whose state is either on or off, who can observe the state of $r$ neighbours to its left and right, and who has a specific action (turn/stay on or turn/stay off) assigned for every possible neighbourhood that it can observe. The rules are recorded in a rule table that states a specific action for every combination of neighbouring states and that of the acting cell. 

For example one rule in the table with $r = 3$ could look like:

```python
([0,1,1,1,0,1,0]) ->  1
```

So, if the centre cell finds itself in this situation (with itself on, left neighbours off on on, right neighbours off, on, off ) then it will remain on for the next time step. There are $2^{2r + 1}$ possible states that the rule table has to account for. Consequently, there are $2^{2^{2r + 1}}$ possible rule tables. This is a **big** number, and tucked away in the galactic number of possibilities are many interesting (or even useful) behaviours.

The magic happens when several cellular automata are put together 'shoulder to shoulder' in a ring formation, and update their states simultaneously over a series of time steps, following the same rules.


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

The automata object found in automata.py only depends on NumPy:
  ```sh
  pip install numpy
  ```

The visualizations in majority_rule.ipynb require matplotlib:
  ```sh
  pip install matplotlib
  ```

### Installation

Just clone the repo:
  ```sh
  git clone git@github.com:LachlanGray/Automata.git
  ```

<!-- USAGE -->
## Usage

Get started with a python file or notebook in the same directory as automata.py, and import Automata:
  ```python
  from automata import Automata
  ```
Numpy and pyplot are also useful to have handy:
  ```python
  import numpy as np
  import matplotlib.pyplot as plt
  ```
Initialize an Automata object with the number of cells, and rule radius. The Rule and initial state are chosen randomly by default, but can be updated later. This object stores the state of all $N$ cells and the update rule. 
  ```python
  N,r = 40, 1
  a = Automata(N,r)
  ```
To run the automata several time steps, use `play(M)` which applies the update $M$ times and returns a shape `(M,N)` numpy array which contains the state of the automata at each time step, from top to bottom. 
  ```python
  M = 40
  g = a.play(M)
  ```
Which can be displayed with
  ```python
  plt.imshow(g)
  plt.axis('off')
  ```
 
![](https://github.com/LachlanGray/Automata/blob/main/images/g1.png)
![](https://github.com/LachlanGray/Automata/blob/main/images/g2.png)
![](https://github.com/LachlanGray/Automata/blob/main/images/g3.png)
![](https://github.com/LachlanGray/Automata/blob/main/images/g4.png)

Here are some examples of what you might see. Also note that since the automata are in a ring formation, the the leftmost and rightmost cell in each row are next-door neighbours.

### Other functions

`Automata.print_rule()` Prints the the automata's rule table. 

`Automata.update_rule(rule)` Sets a new rule table for the automata. It takes a binary numpy array of length $2^{2r+1}$, corresponding to all of the possible local states in alphanumeric order (i.e. the order printed by print_rule). 

`Automata.set_begin_state(state)` Sets a new initial state for the automata. It takes a binary numpy array of length $N$, one entry for each cell. 

`Automata.tick()` Advances the state of the automata by one time step. 

`Automata.maj_rule(M)` Returns the fraction of 1's in the global state after $M$ timesteps. 


## majority_rule.ipynb

This is a python implementation of the genetic algorithm described by James Crutchfield, Rajarshi Das, and Melanie Mitchell [In this paper](https://www.santafe.edu/research/results/working-papers/a-genetic-algorithm-discovers-particle-based-compu) to solve [the majority-rule problem](https://en.wikipedia.org/wiki/Majority_problem_(cellular_automaton)). 

The goal of the majority-rule problem is to find rules that cause the automata to collectively determine the majority state at the beginning of the game. In a nutshell, if more than half of the automata were on at the first time step, then they should all be on by the M'th timestep, otherwise they should all be off. 




