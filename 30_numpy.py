#%%
import numpy as np

a=np.array([1,4,5,8],float)
a

#%% 
a= np.array([[1,2,3],[4,5,6]],float)
a[0,0]
a[0,1]

#%%
np.arange(10,30,5)

#%%
a= np.arange(0.00,2.00,0.3,)
a
a.dtype
#%%
np.array([0,1,-1,0])/np.array([1,0,0,0])

#%%
a= np.zeros((3,3))
a
#%%
a = np.ones((3,3))
a

#%%
np.ones((2,3))

#%%
np.full((3,3),7)

#%%
np.eye(3)

#%%
np.empty((4,3))

#%%
np.arange(10)

#%%
np.arange(3,21,2)

#%%
np.linspace(0,100,5)

#%%
np.logspace(0.1,1,10)

#%%
np.random.random((3,3))

#%%
np.random.rand(3,3)

#%%
np.random.randint(4,size=10)

#%%
np.random.randint(1,size=10)

#%%
np.random.randint(2,size=(2,4))

#%%
np.random.randint(5,size=(2,4))

#%%
(6.25**0.5)*np.random.randn(2,4)+3 
#정규분포에 표준편차를 곱해주고 평균을 더하고 

#%%
np.array([[1,2,3],[4,5,6]])

#%%
a= np.array([[1,2,3],[4,5,6]])
a[:,:2]

#%%
a=np.array(range(6),float).reshape((2,3))
b=a.transpose()
print(a)
print(b)
#%%
a=np.array([[1,2,3],[4,5,6]])
a.flatten()

#%%
a=np.array([[1,2,3,4,5,6]])
b=np.array([[1,2,3,4,5,6]])
c=np.array([[1,2,3,4,5,6]])
np.concatenate((a,b,c))


#%%

a=np.array([1,2,3,4,5,6])
b=np.array([1,2,3,4,5,6])
c=np.array([1,2,3,4,5,6])
np.concatenate((a,b,c))

#%%
a=np.array([[1,2,3,4,5,6]])
a.T

#%%
a=np.array(range(12))
a
#%%
b=a.reshape(3,4)
b
#%%
c=a.reshape(6,2,-1)

#%%
b.flatten()

#%%
b.ravel()

#%%
x= np.arange(5)
x

#%%
x.reshape(5,1)

#%%
x[:,np.newaxis]

#%%
np.stack([np.ones((3,4)),np.zeros((3,4))],axis=0)

#%%
np.r_[np.array([1,2,3]),np.array([4,5,6])]

#%%
np.c_[np.array([1,2,3]),np.array([4,5,6])]

#%%
a=np.array([1,2,3]),np.array([4,5,6])
np.tile(a,(3,2))

#%%
x = np.arange(3)
x

#%%
y=np.arange(5)
y

#%%
X,Y = np.meshgrid(x,y)
X,Y

#%%
[list(zip(x,y)) for x,y in zip(X,Y)]

#%%
a=np.array([1,2,3],float)
b=np.array([5,2,6],float)
print(a+b)
print(a-b)
#%%
print([1,2,3,4]*2)
print(np.array([1,2,3,4])*2)

#%%
import numpy as np

a=np.array([[1,2,3],[4,5,6]])
np.savetxt(r'c:\python\foo.csv',a,delimiter=',')
np.savetxt(r'c:\python\foo.txt',a,delimiter=',')
#%%
b=np.loadtxt(fname=r'c:\python\foo.txt',delimiter=',')
b

#%%
a=np.array([1,2,3,4,5,7,8],float)
print(a.sum())
print(a.prod())
print(a.mean())
print(a.var())
print(a.std())
print(np.median(a))

#%%
x=np.array([[1,2],[3,4]])
print(x)
print(np.sum(x))
print(np.sum(x,axis=0))
print(np.sum(x,axis=1))

#%%
a=np.array([[1,2,1,3],[5,3,1,8]],float)
c=np.corrcoef(a)
print(c)
np.cov(a)

#%%
a=np.array([1,2,3])
b=np.array([4,5,6])
np.dot(a,b)

#%%
np.inner(a,b)

#%%
np.dot(a,b)

#%%
np.outer(a,b)
#%%
np.cross(a,b)

#%%
