##########################################
# Function to build array of sparseGPs
# corresponding to the motion patterns
# by Anirudh Vemula, Aug 16, 2016
##########################################

def build_SparseGPs_array(hyperparam, sparseGPs):
    """
    Params:
    hyperparam = vector containing the hyperparameters
    sparseGPs = structure containing the trajectory data    
    """

    num_motion_patterns = len(sparseGPs)
    
    for i in range(num_motion_patterns):
        # Build GP for vx
        sparseGPs[i]['sparseGP_x'] = build_sparseGP(sparseGPs[i]['data']['traj'], sparseGPs[i]['data']['v'][:,0], hyperparam)
        # Build GP for vy
        sparseGPs[i]['sparseGP_y'] = build_sparseGP(sparseGPs[i]['data']['traj'], sparseGPs[i]['data']['v'][:,1], hyperparam)

    return sparseGPs