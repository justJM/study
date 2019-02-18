#%%
from random import *
import numpy as np
from sklearn import linear_model, datasets, neighbors
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

#%%
l = 10
x = []
y = []
for i in range(l):
    x.append([i])
    y.append([random()*10])

regr = linear_model.LinearRegression()
regr.fit(x,y)

plt.scatter(x,y, color='red')
plt.plot(x,regr.predict(x),color='blue',linewidth=3)

#%%
diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data[:,np.newaxis,2]
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_Y_train = diabetes.target[:-20]
diabetes_Y_test = diabetes.target[-20:]

regr=linear_model.LinearRegression(copy_X=0)
regr.fit(diabetes_X_train,diabetes_Y_train)

print('Coefficiens : ',regr.coef_)
print('intercept: ',regr.intercept_)
print('MSE' , np.mean((regr.predict(diabetes_X_test)-diabetes_Y_test)**2))
print('Variance score', regr.score(diabetes_X_test,diabetes_Y_test))

plt.scatter(diabetes_X_test, diabetes_Y_test, color='red')
plt.plot(diabetes_X_test,regr.predict(diabetes_X_test),color='blue')


#%%
n = 15
iris = datasets.load_iris()
x = iris.data[:,:2]
y = iris.target 
h = 0.02

cmap_bold = ListedColormap(['#FF0000','#00FF00',"#0000FF"])
plt.scatter(x[:,0],x[:,1],c=y, cmap=cmap_bold)

#%%
clf = neighbors.KNeighborsClassifier(n,weights='uniform')
clf.fit(x,y)

clf

#%%
x_min , x_max = x[:,0].min()-1,x[:,0].max()+1
y_min , y_max = x[:,1].min()-1,x[:,1].max()+1

xx , yy =np.meshgrid(np.arange(x_min,x_max, h), np.arange(y_min,y_max,h))

xx[:2,:5] , yy[:2,:5]

#%%
xr = xx.ravel()
yr = yy.ravel()
xy = np.c_[xr,yr]
z = clf.predict(xy)
z = z.reshape(xx.shape)

cmap_light=ListedColormap(['#FFAAAA','#AAFFAA',"#AAAAFF"])
plt.pcolormesh(xx,yy,z,cmap=cmap_light)
cmap_bold = ListedColormap(['#FF0000','#00FF00',"#0000FF"])
plt.scatter(x[:,0],x[:,1],c=y, cmap=cmap_bold)
#%%
