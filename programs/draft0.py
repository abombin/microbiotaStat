from operator import mod
import pandas as pd
import scipy.stats as stats
from itertools import product
data=pd.read_csv("C:/Users/abomb/Projects/microbiotaPhd/allDiets_collection_total.csv")

def getCombinations(var):
    varList=pd.unique(data[var].tolist())
    output = list(product(varList, varList))
    return output

def defGetDietComb():
    normal=data.loc[data['Type']=='N' ]
    normalList=pd.unique(normal['Diet'].tolist())
    modified=data.loc[(data['Type']=='HF') | (data['Type']=='HS')]
    modifiedList=pd.unique(modified['Diet'].tolist())
    output = list(product(normalList, modifiedList))
    return output

# function get p values of comparisons statistic and difference in means

def mwTest(compareBy):
    comparisons=[]
    pVals=[]
    meanDifference=[]
    groups=defGetDietComb()
    for i in groups:
        var1=i[0]
        var2=i[1]
        diets=(var1+'_vs_'+var2)
        group1=data.loc[(data['Diet']==var1)]
        xVar=group1[compareBy].dropna()
        xVarMean=xVar.mean()
        group2=data.loc[(data['Diet']==var2)]
        yVar=group2[compareBy].dropna()
        yVarMean=yVar.mean()
        U1, p=stats.mannwhitneyu(xVar, yVar, nan_policy='omit')
        difference=(xVarMean-yVarMean)
        # append lists
        comparisons.append(diets)
        pVals.append(p)
        meanDifference.append(difference)
        print(pVals)
        print(meanDifference)



mwTest('Sum(Total Collected)')

