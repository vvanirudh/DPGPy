############################################
# Function to calculate the likelihood of a
# given trajectory under the current GP
# by Anirudh Vemula, Aug 16, 2016
#############################################

def traj_likelihood_indep(sparseGP, traj):
    """
    Params:
    sparseGP = the sparseGP corresponding to the current motion pattern
    traj = the current trajectory
    """
    import GPy as gp
    import numpy as np
    import ipdb

    m_x = sparseGP['sparseGP_x']
    m_y = sparseGP['sparseGP_y']

    mu_x_vec, var_x_vec = m_x.predict(traj['traj'])
    mu_y_vec, var_y_vec = m_y.predict(traj['traj'])

    vx = traj['v'][:,0][:,None]
    vy = traj['v'][:,1][:,None]

    x_diff = vx - mu_x_vec
    y_diff = vy - mu_y_vec

    lx = -0.5 * np.log(var_x_vec) - 0.5 * ((x_diff**2) / var_x_vec)
    ly = -0.5 * np.log(var_y_vec) - 0.5 * ((y_diff**2) / var_y_vec)

    lx = np.sum(lx)
    ly = np.sum(ly)
    
    #ipdb.set_trace()
    
    return lx + ly