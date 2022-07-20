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

# function to get p values of comparisons statistic and difference in means

def mwTest(compare, variable, treatment):
    comparisons=[]
    pVals=[]
    meanDifference=[]
    groups=defGetDietComb()
    dataSel=data.loc[(data['Treatment']==treatment)]
    for i in groups:
        var1=i[0]
        var2=i[1]
        varComparison=(var1+'_vs_'+var2)
        group1=dataSel.loc[(dataSel[variable]==var1)]
        xVar=group1[compare].dropna()
        xVarMean=xVar.mean()
        group2=dataSel.loc[(dataSel[variable]==var2)]
        yVar=group2[compare].dropna()
        yVarMean=yVar.mean()
        U1, p=stats.mannwhitneyu(xVar, yVar, nan_policy='omit')
        difference=(xVarMean-yVarMean)
        # append lists
        comparisons.append(varComparison)
        pVals.append(p)
        meanDifference.append(difference)
    testResults=pd.DataFrame({'Comparisons': comparisons, 'pVal': pVals, 'Mean_Difference': meanDifference})
    return(testResults)



totalDiet=mwTest(compare='Sum(Total Collected)', variable='Diet', treatment='S')
totalDeitSel=totalDiet.iloc[[1,5,4,8,10,16,20]].reset_index(drop=True)

totalDeitSel.to_csv("C:/Users/abomb/Projects/microbiotaPhd/output/totalDietS.csv", index=False)