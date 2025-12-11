import random
from tsp.run_simulated_annealing import run_sa_instance
from tsp.geometry import precompute_distances
from tsp.tour import generate_random_points
import matplotlib.pyplot as plt

def main():
    num_cities = 250
    points = generate_random_points(num_cities, seed = random.seed()) 
    dist_matrix = precompute_distances(points)

    INITIAL_TEMP = 5.0             
    COOLING_RATE = 0.99999
    FINAL_STOPPING_TEMP = 0.00001 
    
    absolute_best_length = float('inf')
    absolute_best_tour = None

    print("Running Multiple Restart Simulated Annealing, press Ctrl+C to stop...")
    print(f"Cities: {num_cities} | T_stop: {FINAL_STOPPING_TEMP}")
    
    run_id = 1
    fig, ax = plt.subplots()
    plt.ion()

    try:
        while True:
            best_len, best_tour = run_sa_instance(points,dist_matrix,run_id,initial_temp=INITIAL_TEMP,cooling_rate=COOLING_RATE,stopping_temp=FINAL_STOPPING_TEMP)
            if best_len < absolute_best_length:
                absolute_best_length = best_len
                absolute_best_tour = best_tour

            ax.clear()

            x = [points[i][0] for i in best_tour] + [points[best_tour[0]][0]]
            y = [points[i][1] for i in best_tour] + [points[best_tour[0]][1]]
            
            ax.plot(x, y, marker="o", linestyle="-", color="red")
            ax.set_title(f" Run {run_id} | Length: {best_len:.4f} | Best so far: {absolute_best_length:.4f}")
            ax.set_xlim(0, 1)
            ax.set_ylim(0, 1)
            fig.canvas.draw()
            fig.canvas.flush_events()
            plt.pause(0.01)

            run_id += 1

    except KeyboardInterrupt:
        print("\nComputations Stopped.")
            
    print("Final Multiple Restart Summary:")
    print(f"Best Length Found: {absolute_best_length:.4f}")
    print(f"Best Tour: {absolute_best_tour}")
    print(f"Total Runs Completed: {run_id - 1}")
    print("City Coordinates:")
    for i, (x, y) in enumerate(points):
        print(f"City {i}: ({x:.4f}, {y:.4f})")
        
    if absolute_best_tour:
        plt.ioff()
        plt.close(fig)
        fig, ax = plt.subplots()
        
        x = [points[i][0] for i in absolute_best_tour] + [points[absolute_best_tour[0]][0]]
        y = [points[i][1] for i in absolute_best_tour] + [points[absolute_best_tour[0]][1]]

        ax.plot(x, y, marker="o", linestyle="-", color="red")
        ax.set_title(f"Best Length Found | Length: {absolute_best_length:.4f}")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        fig.savefig("best_tour.png")
        print(f"Final best tour plot saved as 'best_tour.png'")

        plt.show()

if __name__ == "__main__":
    main()