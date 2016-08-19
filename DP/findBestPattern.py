############################################
# Function to find the best cluster for a given
# trajectory
# by Anirudh Vemula, Aug 17, 2016
############################################

def findBestPattern(traj, sparseGPs):
    """
    Params:
    traj = Trajectory data
    sparseGPs = collection of GPs
    """
    import numpy as np
    from traj_likelihood_indep import traj_likelihood_indep
    
    n = len(sparseGPs)

    L_GP = np.zeros(n,)
    L = np.zeros(n,)
    num_counts = np.zeros(n,)

    alpha = 0

    # Find the best fitting cluster
    for i in range(n):
        L_GP[i] = traj_likelihood_indep(sparseGPs[i], traj)

        num_counts[i] = sparseGPs[i]['count']
        alpha = traj['DP_alpha']

    L = L_GP + np.log(num_counts / (np.sum(num_counts) + alpha))/3.

    ind_order = np.argsort(L)

    ind = ind_order[-1]

    return ind