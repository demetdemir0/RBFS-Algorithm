This project demonstrates the Recursive Best-First Search (RBFS) algorithm applied to the Romania map problem. The goal is to find the path from a specified initial city to Bucharest using an informed search strategy.

Overview
The code models a map of Romania, where each city is connected to neighboring cities. The task is to navigate through the cities from an initial state (user input) to the goal state, Bucharest, using the RBFS algorithm.

Features
Graph Representation: The Romania map is represented using an undirected graph with cities as nodes and edges representing roads between cities.
Heuristic Function: The heuristic function used is the straight-line distance from each city to Bucharest.
Recursive Best-First Search (RBFS): The RBFS algorithm is used to find the optimal path from the initial city to Bucharest.
Visualization: As the algorithm processes, the states and the path taken are printed out for each step.
Algorithm Details
Node Structure: Each node represents a city and contains:

state: The current city.
g: The path cost from the initial state to the current city.
h: The heuristic estimate of the cost from the current city to Bucharest.
f: The total cost (f = g + h).
Recursive Best-First Search (RBFS):

Starts from the initial state and recursively explores neighboring cities.
For each city, its neighbors are evaluated based on their f value (the sum of the actual cost and heuristic cost).
The algorithm prunes the search tree based on the f value and a limit (f_limit).
The search continues until the goal city (Bucharest) is found or no path exists.
