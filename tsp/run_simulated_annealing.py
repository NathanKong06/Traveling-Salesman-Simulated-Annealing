from tsp.simulated_annealing import simulated_annealing_tsp

def run_sa_instance(points, dist_matrix, run_id, initial_temp, cooling_rate, stopping_temp):
    solver = simulated_annealing_tsp(points, dist_matrix, initial_temp=initial_temp, cooling_rate=cooling_rate, stopping_temp=stopping_temp)
    
    best_length = float('inf')
    best_tour = None
    
    for tour, length, _ in solver:
        if length < best_length:
            best_length = length
            best_tour = tour

    print(f"Run {run_id}: Best Length: {best_length:.4f}")
    return best_length, best_tour
