############################################
# Function to calculate the average sample from
# a set of samples
# by Anirudh Vemula, Aug 16, 2016
############################################

def averageSample(cluster):
    """
    Params:
    cluster = cluster assignments for all sweeps
    """

    num_traj, num_sample = cluster.shape