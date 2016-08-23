################################################
# Function to generate a set of trajectories
# exhibiting avoidance
# by Anirudh Vemula, Aug 15, 2016
################################################

def generateTrajsWithAvoidance(n_traj, n_points, pLimit, speed, sigma_noise):
    """
    Params:
    n_traj = number of pair of trajectories
    n_points = number of points in each trajectory
    pLimit = limits of the trajectories
    speed = speed of the agents
    sigma_noise = Noise to be added to the trajectories
    """
    import numpy as np
    from generateTwoAgentTraj import generateTwoAgentTraj
    from linear_func import linear_func
    from quadratic import quadratic
    from processTraj import processTraj

    #func = [linear_func, quadratic]
    #num_func = len(func)
    func = linear_func

    traj_counter = 0
    threshold = 0.3

    trajs = {}
    trajs['data'] = [{} for i in range(n_traj*2)]

    while traj_counter < n_traj*2:

        speed_in = speed
        
        traj1, traj2, dt1, dt2 = generateTwoAgentTraj(n_points, pLimit, speed, threshold, func)

        traj1, v1 = processTraj(traj1, dt1, sigma_noise)
        traj2, v2 = processTraj(traj2, dt2, sigma_noise)

        trajs['data'][traj_counter]['traj'] = traj1
        trajs['data'][traj_counter]['v'] = v1
        trajs['data'][traj_counter]['dt'] = dt1
        trajs['data'][traj_counter]['speed'] = speed_in

        trajs['data'][traj_counter+1]['traj'] = traj2
        trajs['data'][traj_counter+1]['v'] = v2
        trajs['data'][traj_counter+1]['dt'] = dt2
        trajs['data'][traj_counter+1]['speed'] = speed_in

        traj_counter += 2

    trajs['n_traj'] = n_traj*2
    trajs['cluster'] = np.ones((n_traj*2,1))
    trajs['sweep_count'] = 1
    trajs['n_clus'] = 1
    trajs['n_points'] = n_points
    
    return trajs
