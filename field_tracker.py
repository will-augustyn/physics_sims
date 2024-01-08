import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

def force(velocity):
    magnetic_field = np.array([1, 1, 1])
    electric_field = np.array([2, 2, 2,])
    F = electric_field + np.cross(velocity, magnetic_field)
    return F

#displacement =  velocity * dt

def make_plot(total_time, dt, velocity, mass):
    t = 0
    positionsx = []
    positionsy = []
    positionsz = []
    displacement = np.array([0, 0, 0])
    while t < total_time:
        acceleration = force(velocity)/mass
        velocity = velocity + (acceleration * dt) 
        displacement = displacement + (velocity * dt)
        positionsx.append(displacement[0])
        positionsy.append(displacement[1])
        positionsz.append(displacement[2])
        t += dt
    ax = plt.figure().add_subplot(projection='3d')
    ax.plot(positionsx, positionsy, positionsz)
    return