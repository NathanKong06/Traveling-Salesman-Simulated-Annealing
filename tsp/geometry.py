import math
import numpy as np 

def euclidean_distance(p1, p2):
    return math.dist(p1, p2)

def precompute_distances(points):
    """Calculates all city-to-city distances and stores them in an N x N matrix."""
    num_cities = len(points)
    dist_matrix = np.zeros((num_cities, num_cities))
    for i in range(num_cities):
        for j in range(i + 1, num_cities):
            dist = euclidean_distance(points[i], points[j])
            dist_matrix[i, j] = dist
            dist_matrix[j, i] = dist 
    return dist_matrix

def tour_length(tour, dist_matrix):
    """Calculates the total length of a given tour using the precomputed matrix."""
    length = 0.0
    num_cities = len(tour)
    for i in range(num_cities):
        city_a = tour[i]
        city_b = tour[(i + 1) % num_cities]
        length += dist_matrix[city_a, city_b]
    return length