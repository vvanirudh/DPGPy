#################################
# Function to initialize the array
# of sparseGPs
# by Anirudh Vemula, Aug 15, 2016
#################################

def initialize_SparseGPs_array(hyperparam, trajs):
    """
    Params:
    hyperparam = Hyperparameters
    trajs = Trajectories data
    """
    import numpy as np
    from build_sparseGP import build_sparseGP
    
    sparseGPs = [{} for i in range(trajs['n_clus'])]
    samples = np.random.choice(trajs['n_traj'], trajs['n_clus'])

    for i in range(trajs['n_clus']):
        # Build GP for vx
        sparseGPs[i]['sparseGP_x'] = build_sparseGP(trajs['data'][samples[i]]['traj'], trajs['data'][samples[i]]['v'][:,0], hyperparam)
        # Build GP for vy
        sparseGPs[i]['sparseGP_x'] = build_sparseGP(trajs['data'][samples[i]]['traj'], trajs['data'][samples[i]]['v'][:,1], hyperparam)

    return sparseGPs