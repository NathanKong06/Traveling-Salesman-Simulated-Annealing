# Traveling Salesman Problem — Simulated Annealing

## Overview

This project implements a Simulated Annealing (SA) algorithm to solve the Traveling Salesman Problem (TSP). The TSP aims to find the shortest possible tour visiting a set of cities exactly once and returning to the starting city.  

The project includes:

- A Python implementation of SA with 2-opt swaps.
- Real-time visualization of the tour as the algorithm progresses.
- Precomputed distance matrices for efficiency.
- Configurable parameters for temperature, cooling, and number of cities.

---

## Features

- Generate a random set of cities in 2D space.
- Solve the TSP using Simulated Annealing.
- Observe live updates of the tour during optimization.
- Output the best tour after completion.
- Save the final tour plot as `best_tour.png`.

---

## Installation

1. Install Requirements

```bash
pip install -r requirements.txt
```

2. Run the Main Script or the Visualization Script

```bash
python main.py
python main_visualization.py
```

## Usage

### Run the main visualization script

```bash
python main_visualization.py
```

- Press Ctrl+C at any time to exit and save the current best tour.
- The final tour will be plotted and saved as best_tour.png.
- Output includes tour length and city coordinates.

### Run the main script

```bash
python main.py
```

- This script runs multiple restarts of SA.
- The best tour found across all restarts is displayed and saved.
- Press Ctrl+C to exit and save the best tour found so far.

### Optional parameters (edit in code)

- INITIAL_TEMP: Starting temperature for SA.
- COOLING_RATE: Rate at which the temperature decreases.
- FINAL_STOPPING_TEMP: Stopping condition for SA.
- num_cities: Number of cities to generate.

## Project Structure

```text
├── main_visualization.py      # Run SA with real-time visualization
├── main.py                    # Multiple restart SA 
├── tsp/
│   ├── geometry.py            # Distance calculations and tour length
│   ├── run_simulated_annealing.py  # Utility to run SA (single run)
│   ├── simulated_annealing.py # Simulated Annealing algorithm
│   └── tour.py                # Tour creation and 2-opt swap
└── README.md                  # Project overview and instructions
```

## Key Functions

- simulated_annealing_tsp(points, dist_matrix, ...)
Runs SA for a set of points with a distance matrix, yields tour updates for visualization.
- precompute_distances(points)
Calculates an N x N distance matrix for all cities.
- tour_length(tour, dist_matrix)
Computes the total length of a given tour.
- two_opt_swap(tour, i, j)
Performs a 2-opt swap between indices i and j in a tour.
- generate_random_points(num_cities, seed)
Generates num_cities random points in 2D space.
