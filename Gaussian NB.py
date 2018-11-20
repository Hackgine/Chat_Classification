# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:09:24 2018

@author: Safelink
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

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
t = time()
clf.fit(features_train, labels_train)
print(time() - t)
#pred = clf.predict(features_test)
Name = input("Enter Word: ")
test = postprocess(Name, labels_test)
pred = clf.predict(test)
pred_1 = clf.predict(features_test)
print(pred, pred_1)
score = clf.score(features_test, labels_test)
print(score)
#print(pred)
#
#try:
#    plt.plot(features_train, clf.predict(features_train), color="r")
#except NameError:
#    pass
#plt.scatter(features_train, labels_train)
#plt.show()

#########################################################


