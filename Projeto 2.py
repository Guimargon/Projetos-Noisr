import random
import matplotlib.pyplot as plt

def random_walk(num_steps, prob_right, num_particles):
    particle_path=[]
    for _ in range (num_particles):
        inicio=[0]
        for prob in range(num_steps):
            prob=random.random()
            if prob<=prob_right:
                inicio.append(inicio[-1]+1)
            else:
                inicio.append(inicio[-1]-1)
        particle_path.append(inicio)
    createplot(num_steps,particle_path)

def createplot(num_steps, particle_paths):
    time = [x for x in range(len(particle_paths[0]))]
#Build the plot with all the particles
    for particle_path in particle_paths:
        plt.plot(particle_path, time)

    plt.title("Random Walk - N particles")
    plt.xlabel("Position")
    plt.ylabel("Time")
    plt.show()

num_steps = 100
prob_right = 0.90
num_particles = 10

random_walk(num_steps, prob_right, num_particles)