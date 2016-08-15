########################################
# Function to plot the given trajectories
# by Anirudh Vemula, Aug 15, 2016
########################################

def plotTrajs(trajs, string_in):
    """
    Params:
    trajs = Trajectories to be plotted
    string_in = String to be displayed
    """
    import matplotlib.pyplot as plt
    import numpy as np
        
    n_trajs = trajs['n_traj']
    colors = ['r','b','g','y','m','c','k']

    # Not implementing subplots, for now

    num_cluster = np.max(trajs['cluster'][:,-1])

    for i in range(n_trajs):
        clus_assign = trajs['cluster'][i,-1]
        c = colors[np.mod(int(clus_assign), 7)]

        traj = trajs['data'][i]['traj']
        
        plt.plot(traj[:,0], traj[:,1], c)
        plt.plot(traj[0,0], traj[0,1], c+'*')

    plt.title(string_in+' - found '+str(num_cluster) + ' clusters, total ' + str(n_trajs) + ' trajs')
    plt.axis('equal')
    plt.show()