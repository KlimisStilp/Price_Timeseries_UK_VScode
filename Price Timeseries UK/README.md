# Price-Timeseries-UK

## Description

Python Notebook that merge Price, Solar Generation, Wind offshore Generation and Wind onshore generation into one dataset.<p>
Creates segments of this dataset regarding every hour of the day and adds 6-month lags.<p>
Train every dataset with LassoCV, using as cross-validation the expanding window rule with TimeSeriesSplit. <p>
Feeds the residuals of Lasso into GARCH model in order to model the volatility. <p>

Timeline of the data: 2015 ~ 2020<p>
Price is given in daily frequency, with 1 hour gap.<p>



## Data
- Solar Generation (Covariate) (ENTSOE)
- Wind On Shore Generation (Covariate) (ENTSOE)
- Wind Off Shore Generation (Covariate) (ENTSOE)
-  Price (Target Variable) (Covariate) (ENTSOE)


