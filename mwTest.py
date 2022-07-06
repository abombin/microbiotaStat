import pandas as pd
import scipy.stats as stats

data=pd.read_csv("C:/Users/abomb/Projects/microbiotaPhd/allDiets_collection_total.csv")

x=data.loc[data['Diet']=='PR']
xVar=x['Sum(Total Collected)']



y=data.loc[data['Diet']=='R']
yVar=y['Sum(Total Collected)']

wilcox=stats.mannwhitneyu(xVar, yVar, nan_policy='omit')
print(wilcox)

total=data['Sum(Total Collected)'].dropna()

shapiro=stats.shapiro(total)

print(shapiro)
