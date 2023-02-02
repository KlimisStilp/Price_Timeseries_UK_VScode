def reliability_diagram(df, obs, mu, std):
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




