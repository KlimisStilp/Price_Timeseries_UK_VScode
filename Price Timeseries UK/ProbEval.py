def reliability_diagram(df, obs, mu, std):
    """"
    Function that takes as input the name of the dataframe, the name of observation,
    the predicted value and the standard deviation, and creates a reliability diagram.

    Parameters
    ------------
    df: Pandas dataframe
    obs: str, name of the column that contains the observed value
    mu: str, name of the column that contains the predicted mean value
    std: str, name of the column that contains the predicted standard deviation
    width: int, number that indicates the width of the final plot
    height: int, number that indicates the height of the final plot

    Returns
    ------------
    matplotlib plot


    Examples
    ------------
    reliability_diagram(df=df_results[15], obs='Price', mu='Predicted Value', std='sigma')

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



def crps_norm(df, obs, mu, sigma):
    import properscoring as ps

    score = ps.crps_gaussian(df[str(obs)], mu=df[str(mu)], sig=df[str(sigma)])
    return score





