def reliability_diagram(df, obs, mu, std):
    """"
    Function that takes as input the name of the dataframe, the name of observation,
    the predicted value and the standard deviation, and creates a reliability diagram.

    Parameters
    ------------
    df: Pandas dataframe
    obs: Numerical or Array of the observation
    mu: Numerical or Array that contains the predicted mean value
    std: Numerical or Array that contains the standard deviation of the predicted mean value's distribution 
    

    Returns
    ------------
    matplotlib plot
    """
    
    from scipy.stats import norm
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

    x_scatter = np.arange(1,99,1)/100
    y_scatter = []
   

    for q in x_scatter:
        a = (df[str(obs)] < norm.ppf(q, loc=df[str(mu)], scale=df[str(std)])).to_list()
        y_scatter.append(sum(a)/len(df))
    
    sns.scatterplot(x=x_scatter, y=y_scatter, linestyle='dashed', color='red', marker='o')
    plt.axline((0,0), slope=1, color='black')
    plt.title('Reliability Diagram')
    plt.xlabel('Nominal')
    plt.ylabel('Observed Relative Frequency')



def crps_norm(df, obs, m, sigma):
    import properscoring as ps

    score = ps.crps_gaussian(df[str(obs)], mu=df[str(m)], sig=df[str(sigma)])
    return score

def pinball_loss_norm(df, obs, mu, std):
    from scipy.stats import norm
    import matplotlib.pyplot as plt
    import seaborn as sns
    import numpy as np

    x_val = np.arange(1,99,1)/100
    y_val = []

    for x in x_val:
        q_point = norm.ppf(x, loc=df[str(mu)], scale=df[str(std)])
        a = np.asarray((df[str(obs)] < q_point)*(1-x)*(q_point - df[str(obs)]) + (df[str(obs)] >= q_point)*(x)*(df[str(obs)] - q_point))
        y_val.append(np.mean(a))

    sns.scatterplot(x=x_val, y=y_val)




