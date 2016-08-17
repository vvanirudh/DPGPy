####################################################
# Function to build a sparse GP regression model for
# the given data (must use GPy)
# by Anirudh Vemula, Aug 15, 2016
####################################################

def build_sparseGP(traj, speed, hyperparam):
    """
    Params:
    traj = trajectory data (x,y)
    speed = output data dx/dt or dy/dt
    hyperparam = set of hyperparameters 
    """
    import GPy as gp
    import ipdb
    
    # Retrieve hyperparameters
    lx = hyperparam[0]
    ly = hyperparam[1]
    sigma_input = hyperparam[2]
    sigma_noise = hyperparam[3]

    # Construct kernel
    K = gp.kern.RBF(input_dim=2, lengthscale=[lx,ly], variance=sigma_input, ARD=True) + gp.kern.White(input_dim=2, variance=sigma_noise)

    speed_vec = speed[:,None]

    # Debug statement
    #ipdb.set_trace()
    
    # Model
    m = gp.models.SparseGPRegression(traj, speed_vec, kernel=K)
    # Optimize?
    #m.optimize('bfgs', messages=False, max_f_eval=100)
    
    return m