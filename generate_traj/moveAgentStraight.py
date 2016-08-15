##########################################
# Function to try a different kind of collision
# avoidance
# by Anirudh Vemula, Aug 15, 2016
##########################################

def moveAgentStraight(traj1, traj2, ind, threshold):
    """
    Function always assumes that agent 2 has to be moved w.r.t agent 1
    
    Params:
    traj1 = trajectory of the first agent
    traj2 = trajectory of the second agent
    ind = index of the point at which collision is occuring
    threshold = collision threshold
    """
    import numpy as np
    
    traj2_new = np.copy(traj2)

    if traj1[ind][0] > traj2[ind][0]:
        traj2_new[ind:,0] = traj2[ind:,0] - threshold
    else:
        traj2_new[ind:,0] = traj2[ind:,0] + threshold

    if traj1[ind][1] > traj2[ind][1]:
        traj2_new[ind:,1] = traj2[ind:,1] - threshold
    else:
        traj2_new[ind:,1] = traj2[ind:,1] + threshold

    quad_x = np.polyfit([ind-5,ind-3,ind], [traj2_new[ind-5,0], traj2_new[ind-3,0], traj2_new[ind,0]], 2)
    quad_y = np.polyfit([ind-5,ind-3,ind], [traj2_new[ind-5,1], traj2_new[ind-3,1], traj2_new[ind,1]], 2)

    
    traj2_new[range(ind-5,ind),0] = np.polyval(quad_x, range(ind-5,ind))
    traj2_new[range(ind-5,ind),1] = np.polyval(quad_y, range(ind-5,ind))

    return traj2_new