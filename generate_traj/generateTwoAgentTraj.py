##############################################
# Function to generate a pair of trajectories
# for two agents, that model cooperative
# collision avoidance (if needed)
# by Anirudh Vemula, Aug 14, 2016
###############################################

def generateTwoAgentTraj(n, pLimit, speed, threshold, func):
    """
    Params:
    n = number of points in the trajectory
    pLimit = limits of the trajectory
    speed = speed of the agent
    threshold = threshold at which agents avoid each other
    func = Function to generate trajectory
    """
    from moveAgentStraight import moveAgentStraight
    import numpy as np
    
    traj1 = func(n, pLimit)
    traj2 = func(n, pLimit)

    traj2 = np.flipud(traj2)

    traj1 = traj1 + (np.random.rand() - 0.5)
    traj2 = traj2 + (np.random.rand() - 0.5)

    while True:
        
        distances = np.sqrt(np.sum((traj1 - traj2)**2, axis=1))
        collisions = np.where(distances < threshold)
        
        if collisions[0].size==0:
            break

        else:
            print "Collision detected"
            ind = collisions[0][0]
            
            traj1 = moveAgentStraight(traj2, traj1, ind, threshold)
            traj2 = moveAgentStraight(traj1, traj2, ind, threshold)

    dt1 = np.zeros((n+1,))
    dt2 = np.zeros((n+1,))

    for i in range(n-1):
        dt1[i] = np.sum((traj1[i+1] - traj1[i])**2) / speed;
        dt2[i] = np.sum((traj2[i+1] - traj2[i])**2) / speed;

    dt1[n] = dt1[n-1]
    dt2[n] = dt2[n-1]

    return traj1, traj2, dt1, dt2