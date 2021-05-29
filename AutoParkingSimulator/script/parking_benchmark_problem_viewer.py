import os
import matplotlib.pyplot as plt
import fnmatch
from parking_slot_generator import ParkingSpace
from vehicle import Car

if __name__ == "__main__":
    # specify the parking environment (should be named as 'yml', but I am too lazy to refactor them).
    parking_lot_environment = "../benchmark_problem/parking_lot01_parking_space.txt"
    parking_lot_environment_file_handle = open(parking_lot_environment, 'r')

    # load the parking lot image.
    map_name = parking_lot_environment_file_handle.readline().strip()
    parking_lot_img = plt.imread("../" + map_name)[:, :]

    # load related benchmark problems
    benchmark = open("../benchmark_problem/" + "parking_lot01_parking_space_agent5_instance20.txt", 'r')
    instance_view = 0

    # the parking lot used by the problem
    _ = benchmark.readline()

    # the number of agents
    num_agent = int(benchmark.readline().strip())
    # the number of instances when there are 5 agents
    num_instance = int(benchmark.readline().strip())

    # it is hard to remove cars from the plot, so create a new one....
    fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
    x_max = parking_lot_img.shape[1] * ParkingSpace.resolution
    y_max = parking_lot_img.shape[0] * ParkingSpace.resolution
    ax.set_xlim(0, x_max)
    ax.set_ylim(0, y_max)
    ax.imshow(parking_lot_img, extent=[0, x_max, 0, y_max], origin="lower", cmap='gray')

    # the cars in the parking lot (figure window)
    agents = []
    for _ in range(num_agent):
        agents.append(Car(ax, "gray"))
        agents[-1].vehicle_inflation_example_disable()

    # show the benchmark problem
    for k in range(num_instance):
        for i in range(num_agent):
            x, y, theta = benchmark.readline().strip().split(' ')  # remove '\n'
            agents[i].update_state(float(x), float(y), float(theta), 0)

        if k == instance_view:
            plt.show()

    # finish playing the current benchmark...
    benchmark.close()
