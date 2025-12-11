import random
import matplotlib.pyplot as plt
from tsp.geometry import precompute_distances
from tsp.simulated_annealing import simulated_annealing_tsp
from tsp.tour import generate_random_points

def main():
    num_cities = 250
    points = generate_random_points(num_cities, seed = random.seed()) 
    dist_matrix = precompute_distances(points)

    INITIAL_TEMP = 5.0             
    COOLING_RATE = 0.99999
    FINAL_STOPPING_TEMP = 0.00001 

    fig, ax = plt.subplots()
    plt.ion()

    print("Running Simulated Annealing with Real-time Visualization")
    print(f"Cities: {num_cities} | T_stop: {FINAL_STOPPING_TEMP}")

    sa_solver = simulated_annealing_tsp(points, dist_matrix,initial_temp=INITIAL_TEMP,cooling_rate=COOLING_RATE,stopping_temp=FINAL_STOPPING_TEMP)

    current_best_length = float('inf')
    last_plot_temp = None  # Track last temperature plotted

    try:
        for current_tour, current_length, temp in sa_solver:
            if current_length < current_best_length:
                current_best_length = current_length

            temp_rounded = round(temp, 3)
            if last_plot_temp is None or temp_rounded != last_plot_temp:
                last_plot_temp = temp_rounded

                x = [points[i][0] for i in current_tour] + [points[current_tour[0]][0]]
                y = [points[i][1] for i in current_tour] + [points[current_tour[0]][1]]

                if 'line' not in locals():
                    line, = ax.plot(x, y, marker="o", linestyle="-", color="red")
                    ax.set_xlim(0, 1)
                    ax.set_ylim(0, 1)
                else:
                    line.set_data(x, y)

                ax.set_title(f"Length: {current_length:.4f} | Temp: {temp:.5f}")
                fig.canvas.draw()
                fig.canvas.flush_events()
                plt.pause(0.001)
    except KeyboardInterrupt:
        print("\nExiting")

    print("Final Summary:")
    print(f"Best Length Found: {current_best_length:.4f}")
    print(f"Total Cities: {num_cities}")
    print("City Coordinates:")
    for i, (x_coord, y_coord) in enumerate(points):
        print(f"City {i}: ({x_coord:.4f}, {y_coord:.4f})")

    plt.ioff()
    plt.close(fig)
    fig, ax = plt.subplots()

    x = [points[i][0] for i in current_tour] + [points[current_tour[0]][0]]
    y = [points[i][1] for i in current_tour] + [points[current_tour[0]][1]]

    ax.plot(x, y, marker="o", linestyle="-", color="red")
    ax.set_title(f"Best Length Found | Length: {current_best_length:.4f}")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    fig.savefig("best_tour.png")
    print(f"Final best tour plot saved as 'best_tour.png'")

    plt.show()

if __name__ == "__main__":
    main()