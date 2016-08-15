#######################################
# Function to group trajectories in the
# same cluster
# by Anirudh Vemula, Aug 15, 2016
#######################################

def groupTraj(sweep_count, trajs):
    """
    Params:
    sweep_count = Current sweep index
    """
    import numpy as np

    # Remove empty clusters
    c, ia, ic = np.unique(trajs['cluster'][:,sweep_count], return_index=True, return_inverse=True)
    c_ind = np.argsort(c)

    trajs['cluster'][:,sweep_count] = c_ind[ic]
    trajs['cluster'][:,sweep_count] = reorder_vec(trajs['cluster'][:,sweep_count])
    
    trajs['n_clus'] = int(np.max(trajs['cluster'][:,sweep_count])) + 1

    count = np.ones(trajs['n_clus'],)
    count = count.astype(int)

    sparseGPs = [{} for i in range(trajs['n_clus'])]
    
    for i in range(trajs['n_clus']):
        indices = np.where(trajs['cluster'][:,sweep_count] == i)
        indices = indices[0]
        count[i] = indices.shape[0]

        # Concatenate all trajectories belonging to the same cluster
        sparseGPs[i]['data'] = {}
        sparseGPs[i]['data']['traj'] = np.zeros((trajs['n_points'], count[i]*2))
        sparseGPs[i]['data']['v'] = np.zeros((trajs['n_points'], count[i]*2))
        sparseGPs[i]['count'] = count[i]

        for j in range(int(count[i])):
            sparseGPs[i]['data']['traj'][:,j:j+2] = trajs['data'][indices[j]]['traj']
            sparseGPs[i]['data']['v'][:,j:j+2] = trajs['data'][indices[j]]['v']

    return count, sparseGPs
            
def reorder_vec(vec):
    """
    Helper Function
    """
    import numpy as np
    n = vec.shape[0]
    vec_p = 9999 * np.ones(n,)
    num = 0
    for i in range(n):
        if vec_p[i] == 9999:
            ind = np.where(vec == vec[i])
            vec_p[ind[0]] = num
            num = num + 1
    return vec_p