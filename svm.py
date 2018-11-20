# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 19:29:31 2018

@author: safelink
"""


import numpy as np
from time import time
from Data_Preprocess import preprocess, postprocess
import matplotlib.pyplot as plt

### features_train and features_test are the featuraes for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train,labels_train, features_test, labels_test = preprocess()





#########################################################
### your code goes here ###

from sklearn import svm

clf = svm.SVC(kernel='rbf', C=10)
t = time()
clf.fit(features_train, labels_train)
print(time() - t)
#pred = clf.predict(features_test)
#Name = input("Enter Word: ")
#test = postprocess(Name, labels_test)
#pred = clf.predict(test)
pred_1 = clf.predict(features_test)
print(pred_1)
score = clf.score(features_test, labels_test)
print(score)
