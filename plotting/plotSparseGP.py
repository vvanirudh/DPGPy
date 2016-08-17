###############################################
# Function to plot a sparseGP
# by Anirudh Vemula, Aug 17, 2016
###############################################

def plotSparseGP(x, y, dx_dt, dy_dt, traj):
    """
    Params:
    x = points at which GP prediction is done
    y = points at which GP prediction is done
    dx_dt = GP predictions
    dy_dt = GP predictions
    traj = Trajectory data
    """
    import numpy as np
    import matplotlib.pyplot as plt


    x_min = np.min(x) - 1
    x_max = np.max(x) + 1
    y_min = np.min(y) - 1
    y_max = np.max(y) + 1

    x_range = x_max - x_min
    y_range = y_max - y_min

    if x_range > y_range:
        y_min = (y_min+y_max)/2. - x_range/2.
        y_max = (y_min+y_max)/2. + x_range/2.
    else:
        x_min = (x_min+x_max)/2. - y_range/2.
        x_max = (x_min+x_max)/2. + y_range/2.


    # Plotting
    plt.figure()
    plt.quiver(x, y, dx_dt, dy_dt)
    plt.plot(traj[:,0], traj[:,1], 'ro')
    plt.axis((x_min, x_max, y_min, y_max))
    plt.show()