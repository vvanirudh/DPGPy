##################################################
# Function to plot array of sparseGPs
# by Anirudh Vemula, Aug 17, 2016
##################################################


def plotSparseGP_array(sparseGPs, num_shown):
    """
    Params:
    sparseGPs = array of sparseGPs
    num_shown = max number of GPs to be shown
    """
    import numpy as np
    from plotSparseGP import plotSparseGP
    import ipdb
    
    n = np.min(np.array([num_shown, len(sparseGPs)]))

    for i in range(n):
        x_min = np.min(sparseGPs[i]['data']['traj'][:,0])
        x_max = np.max(sparseGPs[i]['data']['traj'][:,0])
        y_min = np.min(sparseGPs[i]['data']['traj'][:,1])
        y_max = np.max(sparseGPs[i]['data']['traj'][:,1])

        x_query = np.arange(x_min, x_max+0.5, 0.5)
        y_query = np.arange(y_min, y_max+0.5, 0.5)
        
        X_query, Y_query = np.meshgrid(x_query, y_query)

        X_query = np.reshape(X_query, (x_query.shape[0]*y_query.shape[0],))
        Y_query = np.reshape(Y_query, (x_query.shape[0]*y_query.shape[0],))        
        
        m_x = sparseGPs[i]['sparseGP_x']
        m_y = sparseGPs[i]['sparseGP_y']
        
        x_vel_sparse, x_var_sparse = m_x.predict(np.column_stack((X_query, Y_query)))
        y_vel_sparse, y_var_sparse = m_y.predict(np.column_stack((X_query, Y_query)))

        plotSparseGP(X_query, Y_query, x_vel_sparse, y_vel_sparse, sparseGPs[i]['data']['traj'])