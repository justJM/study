#%%
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

s = pd.Series([1,3,5,np.nan,6,8])
s


#%%
d={'a':0,'b':1,'c':2}
pd.Series(d)


#%%
from pandas import Series, DataFrame
import pandas as pd 
sdata = {'Ohio': 35000, 'Texas':71000, 'Oregon':16000,'Utah':5000}
a = Series(sdata)
states = ['Califoenia','Ohio','Oregon','Taxas']
b= Series(sdata, index=states)
b
print(a)
print(b)

#%%
pd.isnull(b)


#%%
b.isnull()

#%%
sales_stats={'day':[1,2,3,4,5,6],'Visitor':[43,45,33,43,78,44],'Revenue':[64,73,62,64,53,66]}
df=DataFrame(sales_stats)
df

#%%
df.loc[:3]

#%%
df=df.set_index('day')
df

#%%
df.iloc[2:5]

#%%
df.loc[3:5]


#%%
df2=pd.DataFrame(sales_stats,index=['a','b','c','d','e','f'])
df2
df2.iloc[3:5]

#%%
df2[['Visitor','day']]

#%%
DataFrame(df2,columns=['Visitor','day','dept'])

#%%
df = pd.DataFrame(data= np.array([[1,2,3],[4,5,6],[7,8,9]]),columns=['A','B','C'])
df
#%%
for i,r in df.iterrows():
    print(r['A'],r['B'])

#%%
for i,r in df.iterrows():
    print(i)
    print(r)


#%%
df = pd.DataFrame({'A':['foo','bar','foo','bar','foo','bar','foo','foo'],'B':['one','one','two','three','two','two','one','three'],'C':np.random.randn(8),'D':np.random.randn(8)})
df

#%%
g=df.groupby('A')
g2=df.groupby(['A','B'])
#%%
print(g.mean())
print(g.sum())
print(g2.mean())
#%%
g.get_group('bar')


#%%
pd.date_range('2018-4-4','2018-4-30')

#%%
pd.date_range(start='2017-5-6', periods=900)


#%%
pd.date_range('2018-4-1','2018-4-19',freq='B')

#%%
pd.date_range('2018-4-1','2018-4-19',freq='W')


#%%
rng = pd.date_range('1/1/2018',periods=72,freq='H')
rng


#%%
ts = pd.Series(np.random.randn(len(rng)),index=rng)
ts
#%%
ts.truncate(before='2018-1-1', after='2018-1-3')


#%%
data=[pd.date_range(start='2017-5-6', periods=10)]
df= pd.DataFrame(data,columns = ['date', [np.random.randint(30,50,10)]])
df
#%%
