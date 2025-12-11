import math 
import random 
from tsp.tour import create_random_tour, two_opt_swap
from tsp.geometry import tour_length

def simulated_annealing_tsp(points, dist_matrix, initial_temp = 5.0, cooling_rate = 0.99999, stopping_temp = 0.00001):
    num_cities = len(points)
    
    current_tour = create_random_tour(num_cities)
    current_length = tour_length(current_tour, dist_matrix)

    best_tour = current_tour[:]
    best_length = current_length

    current_temp = initial_temp # Temperature starts high to allow acceptance of bad moves
    
    yield best_tour, best_length, current_temp

    while current_temp > stopping_temp:
        # Pick two indices for a 2-opt move; retry until non-adjacent
        while True:
            i, j = random.sample(range(num_cities), 2) # Pick two distinct indices
            if abs(i - j) > 1 and abs(i - j) < num_cities - 1: # Check if they are not adjacent and acceptable
                break
            if (i == 0 and j == num_cities - 1) or (j == 0 and i == num_cities - 1): # Reject circular adjacency (first and last city)
                continue
            
        if i > j: 
            i, j = j, i  # Normalize order so i < j for consistent segment reversal
                
        # Identify the four edges involved in the 2-opt move: (a-b) and (c-d) will be replaced with (a-c) and (b-d)
        a_idx = current_tour[(i - 1) % num_cities] # City before i
        b_idx = current_tour[i]                    # City at i
        c_idx = current_tour[j]                    # City at j
        d_idx = current_tour[(j + 1) % num_cities] # City after j
        
        # Compute the cost of the current edges being removed
        old_cost = dist_matrix[a_idx, b_idx] + dist_matrix[c_idx, d_idx]
        # Compute the cost of the new edges after the swap
        new_cost = dist_matrix[a_idx, c_idx] + dist_matrix[b_idx, d_idx]
        
        # Difference in cost determines move benefit (negative = improvement)
        delta_E = new_cost - old_cost

        # Accept move always if better; otherwise probabilistically
        if delta_E < 0:
            accept_move = True
        else:
            acceptance_prob = math.exp(-delta_E / current_temp)
            accept_move = random.random() < acceptance_prob
        
        # Perform the 2-opt reversal if the move is accepted
        if accept_move:
            current_tour = two_opt_swap(current_tour, i, j)
            current_length += delta_E
        
        if current_length < best_length:
            best_tour = current_tour[:]
            best_length = current_length

        # Cool the temperature 
        current_temp *= cooling_rate
        
        yield best_tour, best_length, current_temp