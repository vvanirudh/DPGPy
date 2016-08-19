##########################################
# Function to generate a quadratic shaped
# trajectory
# by Anirudh Vemula, Aug 17, 2016
##########################################

def quadratic(n, pLimits):
    """
    Params:
    n = number of points in the trajectory
    pLimits = Limits of the trajectory
    """
    import numpy as np

    offset = 1
    x_min = pLimits[0] + offset
    x_max = pLimits[1] - offset
    y_min = pLimits[2] + offset
    y_max = pLimits[3] - offset

    dx = (x_max - x_min) / n
    dx_old = (2.) / n
    scale = dx / dx_old
    x = (np.arange(-1, 1, dx_old))
    y = x**2

    x = x*scale
    y = y*scale

    traj = np.column_stack((x,y))

    return traj