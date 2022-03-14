# SWEN-711: Homework 4
For homework 4

# Question One
## Environment Dynamics
1. p = 0.8
    * The correct action is attempted
1. p = 0.05
    * The agent is confused and moves +90&deg;
1. p = 0.05
    * The agent is confused and moves -90&deg;
1. p = 0.1
    * The agent is confused and does not move

## Assumptions
1. The agent cannot move out of the world, an attempt to do so will result in no movement

## Part 1
See [P1.py](src/P1.py) for the python code related to part 1. Because of the above (Environment Dynamics)[#environment-dynamics] there is some variablility but a sample statistical analysis of the observed discounted returns is below:
```
Mean:  -25.838
Standard Deviation:  49.91129888111509
Maximum:  10
Minimuim:  -490
```