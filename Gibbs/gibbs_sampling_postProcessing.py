####################################################
# Function to do Gibbs sampling and get average, mode
# statistics
# by Anirudh Vemula, Aug 16, 2016
####################################################

def gibbs_sampling_postProcessing(cluster, burn_in, splicing):
    """
    Params:
    cluster = cluster assignments for all sweeps
    burn_in = Burn in value for Gibbs
    splicing = Splicing value for Gibbs   
    """
    import numpy as np
    from averageSample import averageSample
    import ipdb

    # Burn in
    cluster_p = cluster[burn_in+1:,:]

    # Splicing
    cluster_p = cluster_p[::splicing,:]

    # Reordering
    m,n = cluster_p.shape

    for i in range(m):
        cluster_p[i,:] = reorder_vec(cluster_p[i,:])

    config = []
    config_count = []
    cluster_pp = np.copy(cluster_p)

    mm = m

    while mm > 0:

        config.append(cluster_pp[0,:])

        tmp_mat = (cluster_pp - np.tile(config[-1], (mm,1)))

        diff = np.max(tmp_mat.T,axis=0)

        ind = np.where(diff!=0)

        cluster_pp = cluster_pp[ind[0],:]

        config_count.append(mm - ind[0].shape[0])

        mm,n = cluster_pp.shape

    # Convert config and config_count to arrays
    config = np.array(config)
    config_count = np.array(config_count)
    
    value_ind = np.argmax(config_count)

    mode = config[value_ind,:]
    avgSample = averageSample(cluster_p)
    
    return avgSample, mode, config, config_count

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