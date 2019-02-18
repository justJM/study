#%%
import matplotlib.pyplot as plt
import numpy as np
t = np.arange(0.,5.,0.2)

plt.plot(t,t,'ro',t,t**2,'bs',t,t**3,'g^')
# plt.ylabel('y')
# plt.axis([0,6,0,20])


#%%
N=20
x = np.random.rand(N)
y = np.random.rand(N)

plt.scatter(x,y, s=25, c='red',marker='^')


#%%
plt.plot(x,y,'D',c='red',markersize=5)

#%%
np.random.seed(19840929)

N= 50 
x = np.random.rand(N)
y = np.random.rand(N)
c = np.random.rand(N)
s = 10000*(np.random.rand(N))**2

plt.scatter(x,y,s=s,c=c,alpha=0.6)


#%%
x= np.random.rand(10)
y= np.random.rand(10)
z = np.sqrt(x**2 + y**2)

v = np.array([[-1,-1],[-1,1],[1,1],[-1,-1]])
plt.scatter(x,y, s=y*x*10000, c=z ,marker=(11,1),alpha=0.6)

#%%
ind = np.arange(4)
man = np.random.rand(4)*10
wman = np.random.rand(4)*10
w = 0.35
plt.bar(ind-w/2,man,width=w, bottom=0, color = 'red')
plt.bar(ind+w/2,wman,width=w, bottom=0, color = 'b')



#%%
plt.bar(ind,man,width=w, bottom=0, color = 'red')
plt.bar(ind,wman,width=w, bottom=man, color = 'b')

#%%
labels = 'F','H','D','L'
sizes=[15,30,45,10]
explode = (0,0.07,0,0)
c = ['red','blue','green','white']
plt.pie(sizes,colors = c,explode=explode,labels = labels, autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.legend()
#%%

s=0.3
v = np.array([[60.,32.],[37.,40.],[29.,10.]])
cmap = plt.get_cmap('tab20c')
o_c = cmap(np.arange(3)*4)
i_c = cmap(np.array([1,2,5,6,9,10]))
plt.pie(v.sum(axis=1),radius=1,colors=o_c,wedgeprops=dict(width=s,edgecolor='w'))
plt.pie(v.flatten(),radius=1-s,colors=i_c,wedgeprops=dict(width=s,edgecolor='w'))


#%%

#%%
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='white',color_codes=True)

iris = pd.read_csv('C:\Python\iris.csv')

iris.head()


sns.jointplot(x='sepal_length',y='sepal_width', data=iris, height=5)

#%%
sns.FacetGrid(data=iris, size=5, hue='species')\
    .map(plt.scatter, 'sepal_length','sepal_width')\
    .add_legend()


#%%
