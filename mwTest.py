import pandas as pd
import scipy.stats as stats

data=pd.read_csv("C:/Users/abomb/Projects/microbiotaPhd/allDiets_collection_total.csv")

total=data['Sum(Total Collected)'].dropna()
shapiro=stats.shapiro(total)

x=data.loc[data['Diet']=='PR']
xVar=x['Sum(Total Collected)'].dropna()



y=data.loc[data['Diet']=='PR']
yVar=y['Sum(Total Collected)'].dropna()

mwTest=stats.mannwhitneyu(xVar, yVar, nan_policy='omit')
print(mwTest)


U1, p=stats.mannwhitneyu(xVar, yVar, nan_policy='omit')
print(U1)
print(p)
