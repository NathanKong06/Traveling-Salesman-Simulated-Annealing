import random

def create_random_tour(num_cities):
    tour = list(range(num_cities))
    random.shuffle(tour)
    return tour

def two_opt_swap(tour, i, j):
    if i > j:
        i, j = j, i
    
    prefix = tour[:i]
    segment_to_reverse = tour[i:j+1]
    reversed_segment = segment_to_reverse[::-1]
    suffix = tour[j+1:]
    return prefix + reversed_segment + suffix

def generate_random_points(n, seed = None):
    """Generates N random (x, y) coordinates between 0 and 1."""
    if seed is not None:
        random.seed(seed)
    return [(random.random(), random.random()) for _ in range(n)]