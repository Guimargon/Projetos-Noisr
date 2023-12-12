import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

initial_pos1=1
initial_pos2=4
initial_velocity1=0.1
initial_velocity2=-0.1
mass1=1
mass2=1.5
num_frames=100
box_size=5

def colisaobolas(vel1,vel2,mass1,mass2):
    vel1,vel2=((mass1-mass2)*vel1+2*mass2*vel2)/(mass1+mass2),(2*mass1*vel1+(mass2-mass1)*vel2)/(mass1+mass2)
    return vel1,vel2

def colisaoparedeesquerda(vel1):
    vel1=-vel1
    return vel1

def colisaoparededireita(vel2):
    vel2=-vel2
    return vel2

def simulate_collision(initial_pos1, initial_pos2, initial_velocity1, initial_velocity2, mass1, mass2, num_frames, box_size):
    vel1=initial_velocity1
    vel2=initial_velocity2
    pos1=[initial_pos1]
    pos2=[initial_pos2]

    for _ in range(1,num_frames):

        pos1.append(pos1[-1]+vel1)
        pos2.append(pos2[-1]+vel2)

        if pos1[-1]>pos2[-1]:
            vel1,vel2=colisaobolas(vel1,vel2,mass1,mass2)

        elif pos1[-1]<0:
            vel1=colisaoparedeesquerda(vel1)

        elif pos2[-1]>box_size:
            vel2=colisaoparededireita(vel2)

    createanimation(pos1,pos2,box_size)

def createanimation(positions1, positions2, boxsize):
    num_frames = len(positions1)

    fig, ax = plt.subplots()
    ax.set_xlim(0, boxsize)
    ax.set_ylim(-0.1, 0.1)

    ball1 , = ax.plot(positions1[0], 0,"bo", markersize=10)
    ball2 , = ax.plot(positions2[0], 0, "ro", markersize=10)

    def update(frame):
        ball1.set_xdata(positions1[frame])
        ball2.set_xdata(positions2[frame])
        return ball1, ball2
    ani = FuncAnimation(fig, update, frames=num_frames, blit=True)
    plt.show()

    plt.close(fig)

    return

simulate_collision(initial_pos1,initial_pos2,initial_velocity1,initial_velocity2,mass1,mass2,num_frames,box_size)