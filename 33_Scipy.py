#%%
import numpy as np
from scipy.stats import norm
from scipy import stats
import matplotlib.pyplot as plt

x = np.arange(-5,5.1,0.1)
y = norm.pdf(x=x,loc=0,scale = 1)
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')

#%%
samples = np.random.normal(size = 1000)
loc, std = norm.fit(samples)
print(loc, std)

print(np.mean(samples))
print(np.median(samples))
# bins = np.arange(-3.5,3.6,1)
# pdf = norm.pdf(bins)

# plt.plot(bins,histogram,)

#%%
a = np.random.normal(0,1,size=100)
b = np.random.normal(1,1,size=100)
stats.ttest_ind(a,b)

#%%
a = np.random.normal(0,1,size=100)
b = np.random.normal(1,1,size=100)
bins = np.linspace(-4,4,30)

histogram1, bins = np.histogram(a,bins=bins,normed=True)
histogram2, bins = np.histogram(b,bins=bins,normed=True)
plt.figure(figsize=(6,4))
plt.hist(a,bins=bins,normed=True,label='a')
plt.hist(b,bins=bins,normed=True,label='b')
plt.legend(loc='best')

stats.ttest_ind(a,b)

#%%
from scipy.stats import binom
plt.subplot(131)
plt.xlim(-3,15)
plt.plot(range(16), binom.pmf(range(16),n=10,p=0.1),marker='o')

plt.subplot(132)
plt.xlim(-3,15)
plt.plot(range(-5,16), norm.pdf(range(-5,16),loc=1,scale=np.sqrt(0.9)),color='black')
plt.subplot(133)
plt.plot(range(16), binom.pmf(range(16),n=10,p=0.1),marker='o')
plt.plot(range(-5,16), norm.pdf(range(-5,16),loc=1,scale=0.9**0.5),color='black')



#%%
from scipy.stats import binom
plt.subplot(131)
plt.xlim(-3,15)
plt.plot(range(16), binom.pmf(range(16),n=30,p=0.1),marker='o')

plt.subplot(132)
plt.xlim(-3,15)
plt.plot(range(-5,16), norm.pdf(range(-5,16),loc=3,scale=np.sqrt(2.7)),color='black')
plt.subplot(133)
plt.plot(range(16), binom.pmf(range(16),n=30,p=0.1),marker='o')
plt.plot(range(-5,16), norm.pdf(range(-5,16),loc=3,scale=2.7**0.5),color='black')



#%%
from scipy.stats import chi2

x = np.arange(0,40.1,0.1)
x
plt.plot(x,chi2.pdf(x,3),color='black', label='3')
plt.plot(x,chi2.pdf(x,6),color='red', label='6')
plt.plot(x,chi2.pdf(x,9),color='blue', label='9')
plt.plot(x,chi2.pdf(x,20),color='green', label='20')
plt.legend(loc='upper right')

#%%
x = np.arange(-3,3.1,0.1)
from scipy.stats import t
plt.plot(x,t.pdf(x,3),color='black', label='3')_
plt.plot(x,t.pdf(x,6),color='red', label='6')
plt.plot(x,t.pdf(x,9),color='blue', label='9')
plt.plot(x,t.pdf(x,20),color='green', label='20')
plt.plot(x,norm.pdf(x,0,1),color='yellow', label='N')
plt.legend(loc='upper right')
#%%

x = np.arange(0,4.1,0.1)
from scipy.stats import f
plt.plot(x,f.pdf(x,3,3),color='black', label='3')
plt.plot(x,f.pdf(x,3,6),color='red', label='6')
plt.plot(x,f.pdf(x,3,9),color='blue', label='9')
plt.plot(x,f.pdf(x,3,20),color='green', label='20')
# plt.plot(x,norm.pdf(x,0,1),color='yellow', label='N')
plt.legend(loc='upper right')


#%%
