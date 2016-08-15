###################################################
# Script to execute the DPGP model on synthetic data
# by Anirudh Vemula, Aug 15, 2016
###################################################

from generateTrajsWithAvoidance import generateTrajsWithAvoidance
from plotTrajs import plotTrajs
from groupTraj import groupTraj

import GPy as gp
import numpy as np

# Hyperparameters
lx = 2
ly = 2

###############################################################
# Generate n trajectories
###############################################################

n_traj = 1
n_points = 30
x_min, x_max, y_min, y_max = (-5,5,-5,5)
pLimit = [x_min, x_max, y_min, y_max]
speed = 1.
sigma_noise = 0.05

trajs = generateTrajsWithAvoidance(n_traj, n_points, pLimit, speed, sigma_noise)

n_traj = trajs['n_traj']
plotTrajs(trajs, 'initialization')

###############################################################
# DPGP initialization
###############################################################
sigma_noise = 0.5
sigma_input = 1
hyperparam = [lx, ly, sigma_input, sigma_noise]
n_sweep = 200

trajs['n_clus'] = int(np.round(np.log(n_traj)))
cluster = np.zeros((n_traj, n_sweep))
cluster[:,0] = np.random.uniform(low=0, high=trajs['n_clus'], size=(n_traj,))

trajs['cluster'] = cluster
count, sparseGPs = groupTraj(0, trajs);

alpha = 0.5

