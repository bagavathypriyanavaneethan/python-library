# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 20:06:02 2020

@author: Bagavathi Priya
"""

from sklearn import svm
from sklearn import datasets
iris=datasets.load_iris()
type(iris) 
iris.data
iris.feature_names
iris.target
iris.target_names
x=iris.data[:,2]
y=iris.target
 
#from sklearn.crossvalidation import train_test_split
'''NOTE:Try substituting cross_validation to model_selection'''
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=4)



xtrain2d=xtrain.reshape(-1,1)
xtest2d=xtest.reshape(-1,1)
ytrain2d=ytrain.reshape(-1,1)
ytest2d=ytest.reshape(-1,1)


model=svm.SVC(kernel='linear')
model.fit(xtrain2d,ytrain2d)

from sklearn.metrics import accuracy_score
acc=model.score(xtest2d,ytest2d)

ypred=model.predict(xtest2d)
a=accuracy_score(ytest2d,ypred)