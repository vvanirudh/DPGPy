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
    import numpy as np
    from similarityDist import similarityDist

    num_traj, num_sample = cluster.shape

    similarity_matrix = np.zeros(num_sample,num_sample)

    for i in range(num_sample):
        for j in range(i):
            similarity_matrix[i,j] = similarityDist(cluster[:,i], cluster[:,j])
            similarity_matrix[j,i] = similarity_matrix[i,j]

    # Best configuration
    similarity_score = np.sum(similarity_matrix, axis=0)

    # Throw away the bottom 30% samples
    reduced_num_samples = np.floor(0.5 * num_sample)
    order_ind = np.argsort(similarity_score)
    reduced_sim_matrix = similarity_matrix[order_ind[0:reduced_num_samples], order_ind[0:reduced_num_samples]]
    reduced_sim_score = np.sum(reduced_sim_matrix, axis=0)
    ind = np.argmax(reduced_sim_score)

    sample = cluster[:,order_ind[ind]]
    return sample