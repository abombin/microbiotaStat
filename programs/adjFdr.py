import pandas as pd
from statsmodels.stats import multitest



data=pd.read_csv("C:/Users/abomb/Projects/microbiotaPhd/output/totalDietS.csv")
print(data.columns)

def adjustFdr(df, pCol):
    pVals=df[pCol].tolist()
    U1, p=multitest.fdrcorrection(pVals, alpha=0.05, method='indep', is_sorted=False)
    df.insert(loc=2, column="pVal_FDR", value=p, allow_duplicates=True)
    return df


adjustDf=adjustFdr(df=data, pCol='pVal')

adjustDf.to_csv("C:/Users/abomb/Projects/microbiotaPhd/output/totalDietSFdr.csv")



