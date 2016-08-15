##############################################
# Function to process trajectory and find out
# speeds and add Noise
# by Anirudh Vemula, Aug 15, 2016
##############################################

def processTraj(traj, dt, sigma_noise):
    """
    Params:
    traj = the trajectory
    dt = times
    sigma_noise = Noise to be added
    """
    import numpy as np

    n = traj.shape[0]

    v = np.zeros((n,2))

    for i in range(n-1):
        v[i,0] = (traj[i+1,0] - traj[i,0]) / dt[i]
        v[i,1] = (traj[i+1,1] - traj[i,1]) / dt[i]

    v[n-1,0] = v[n-2,0]
    v[n-1,1] = v[n-2,1]

    dx_noise = sigma_noise * np.random.randn(n)
    dy_noise = sigma_noise * np.random.randn(n)

    v[:,0] = v[:,0] + dx_noise
    v[:,1] = v[:,1] + dy_noise

    traj[1:,0] = traj[0:n-1,0] + v[0:n-1,0]*dt[0:n-1]
    traj[1:,1] = traj[0:n-1,1] + v[0:n-1,1]*dt[0:n-1]

    return traj, v