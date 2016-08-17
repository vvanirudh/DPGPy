###################################################
# Script to execute the DPGP model on synthetic data
# by Anirudh Vemula, Aug 15, 2016
###################################################

from generateTrajsWithAvoidance import generateTrajsWithAvoidance
from plotTrajs import plotTrajs
from groupTraj import groupTraj
from initialize_SparseGPs_array import initialize_SparseGPs_array
from build_SparseGPs_array import build_SparseGPs_array
from traj_likelihood_indep import traj_likelihood_indep

import GPy as gp
import numpy as np
import ipdb

# Hyperparameters
lx = 2
ly = 2
sigma_noise = 0.5
sigma_input = 1

###############################################################
# Generate n trajectories
###############################################################

n_traj = 1
n_points = 30
x_min, x_max, y_min, y_max = (-5,5,-5,5)
pLimit = [x_min, x_max, y_min, y_max]
speed = 1.
sigma_noise_traj = 0.05

trajs = generateTrajsWithAvoidance(n_traj, n_points, pLimit, speed, sigma_noise_traj)

n_traj = trajs['n_traj']
plotTrajs(trajs, 'initialization')

###############################################################
# DPGP initialization
###############################################################
hyperparam = [lx, ly, sigma_input, sigma_noise]
n_sweep = 2

trajs['n_clus'] = int(np.round(np.log(n_traj)))
cluster = np.zeros((n_traj, n_sweep))
cluster[:,0] = np.random.uniform(low=0, high=trajs['n_clus'], size=(n_traj,))

trajs['cluster'] = cluster
count, sparseGPs = groupTraj(0, trajs);

alpha = 0.5
sparseGPs = initialize_SparseGPs_array(hyperparam, trajs)

#################################################################
# Main Loop
#################################################################
for sweep_num in range(n_sweep):
    trajs['sweep_count'] = sweep_num

    # Build sparseGP for each motion pattern
    if sweep_num > 0:
        sparseGPs = build_SparseGPs_array(hyperparam, sparseGPs)

    # TODO : Update alpha procedure
    
    # Debug printing
    print str(sweep_num+1) + "th sweep, " + str(trajs['n_clus']) + " clusters, alpha: "+str(alpha)
    for pp in count:
        print str(pp),
    print

    # Compute likelihoods for each trajectory from each existing cluster
    
    # Complete log-likelihood
    L = np.zeros((n_traj, trajs['n_clus'] + 1))
    # GP log-likelihood
    L_GP = np.zeros((n_traj, trajs['n_clus'] + 1))

    for k in range(n_traj):
        # Existing clusters
        for j in range(trajs['n_clus']):
            # Set DP alpha parameter for the trajectory
            trajs['data'][k]['DP_alpha'] = alpha

            if j == trajs['cluster'][k, sweep_num]:
                # The current trajectory is already assigned to this cluster
                n_k = count[j] - 1
            else:
                n_k = count[j]

            if n_k == 0:
                # No more trajectories assigned to this cluster
                n_k = alpha

            # Calculate GP likelihood of the current trajectory
            L_GP[k][j] = traj_likelihood_indep(sparseGPs[j], trajs['data'][k])

            # Calculate the complete likelihood of the current trajectory
            L[k][j] = L_GP[k][j] + np.log(n_k / (n_traj - 1 + alpha))

        # TODO : Is this the right normalization const?
        normalization_const = np.max(L[k][:-1])
        l = L[k,:] - normalization_const

        # TODO : Should we use the same normalization const as above?
        l_GP = L_GP[k,:] - normalization_const

        p = np.exp(l)
        p[trajs['n_clus']] = np.mean(np.exp(l_GP[:-1])) * (alpha / (n_traj - 1 + alpha))

        #ipdb.set_trace()

        # Convert p to probabilities
        p = p / np.sum(p)
        
        # Draw z_k
        z_k = np.random.choice(trajs['n_clus']+1, 1, replace=True, p=p)
        # Update cluster
        if z_k == trajs['n_clus']:
            # New cluster
            z_k = count.shape[0]
            count = np.append(count, 0)

        count[trajs['cluster'][k, sweep_num]] = count[trajs['cluster'][k,sweep_num]] - 1
        trajs['cluster'][k, sweep_num] = z_k
        count[z_k] = count[z_k] + 1

    # Initialize for the next iteration
    count, sparseGPs = groupTraj(sweep_num, trajs)
    if sweep_num < n_sweep-1:
        trajs['cluster'][:,sweep_num+1] = trajs['cluster'][:,sweep_num]

# End Loop
##############################################################
# Gibbs Sampling
##############################################################
burn_in = np.floor(n_sweep/2)
splicing = 2
[avgSample, mode, config, config_count] = gibbs_sampling_postProcessing(trajs['cluster'], burn_in, splicing)
