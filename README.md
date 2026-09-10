# Pathfinding Visualiser

This is a grid-based visualisation of Dijkstra's shortest path algorithm, built with Python and pygame.

## What it does
Draw walls on a grid, set a start and end point, and let the Dijkstra's algorithm explore the grid to find the shortest path between them. The explored cells are shown in blue, and the final shortest path is highlighted in yellow.

## Controls
- Left click — start (first click), end (second click), then walls rest of clicks
- Right click — deletes a cell
- SPACE — run Dijkstra's algorithm
- C — clear the grid

## How it works
Grid is treated as a graph where each cell connects to its four neighbours. Dijkstra's algorithm follows a priority queue to explore the closest unvisited cell first which tracks the shortest known distance to each cell as it goes. Once it reaches the end point, it traces back through a recorded path to show the shortest route.

## Installation
```
pip install pygame
python main.py
```
