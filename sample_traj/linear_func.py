##########################################
# Function to generate a linear trajectory
# by Anirudh Vemula, Aug 15, 2016
##########################################
import numpy as np


def linear_func(n, pLimits):
    """
    Params:
    n = number of points in the trajectory
    pLimits = Limits of the trajectory
    """
    offset = 1.
    x_min = pLimits[0] + offset
    x_max = pLimits[1] - offset
    y_min = pLimits[2] + offset
    y_max = pLimits[3] - offset

    a = 0.5
    b = 0.2

    dx = (x_max - x_min) / n
    dx_old = (2.) / n
    scale = dx / dx_old
    x = (np.arange(-1, 1, dx_old))
    y = a * x - b

    x = x*scale
    y = y*scale

    x = x[None,:]
    y = y[None,:]

    traj = np.hstack((x.T,y.T))

    return traj