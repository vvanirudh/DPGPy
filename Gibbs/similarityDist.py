############################################
# Function to define the similarity distance
# between two cluster assignments
# by Anirudh Vemula, Aug 16, 2016
############################################

def similarityDist(v1, v2):
    """
    Params:
    v1 = 1st cluster assignment
    v2 = 2nd cluster assignment
    """
    import numpy as np
    import ipdb

    num_clus_1 = int(np.max(v1))
    num_clus_2 = int(np.max(v2))

    n = v1.shape[0]

    label1 = np.zeros((n, num_clus_1))
    label2 = np.zeros((n, num_clus_2))

    for i in range(num_clus_1):
        label1[:,i] = (v1==i)

    for i in range(num_clus_2):
        label2[:,i] = (v2==i)

    tmp = np.dot(label1.T,label2)
    simLevel = 0

    for i in range(num_clus_1):
        for j in range(num_clus_2):
            simLevel = simLevel + tmp[i,j] * np.sum(label1[:,i] == label2[:,j])

    return simLevel