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

print(defGetDietComb())
