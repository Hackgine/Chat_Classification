
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 18:07:27 2018

@author: Safelink
"""

import pickle
from sklearn import cross_validation
#file = open("../tools/word_data.pkl", "rb")
#authors = pickle.load(file)
#for lines in range(len(authors)):
#    print(authors[lines])

#file_size =sum(1 for line in open("words_data.txt", errors='ignore'))
#print(file_size)    
#pickle_out = open("writers.pkl", "wb")
#pickle.dump("Writers.txt", pickle_out)
#pickle_out.close()
#
words_data = open("words_data.txt", "r", errors='ignore')
words = []
for line in words_data.readlines():
    # words.append(line)
    for word in line.split():
        print(word)
        words.append(word)
    
#
#writers_pkl = open("writers.pkl", "rb")
#writers = pickle.load(writers_pkl)
#writers_pkl.close()
#
print(len(words))

#words_data_pkl = open("word_data.pkl", "rb")
#words_data = pickle.load(words_data_pkl)
#words_data_pkl.close()
#    
#    
#writers_pkl = open("writers.pkl", "rb")
#writers = pickle.load(writers_pkl)
#writers_pkl.close()

#writers=[]
#words=[]
#file = open("words_data.txt","r", errors='ignore')
#file_w = open("Writers.txt","r", errors='ignore')
#for line in file.readlines():
#    words.append(line)
#    #print(line)
#for line in file_w.readlines():
#    writers.append(line)
#    #print(line)
#
##writers = numpy.reshape(writers, 1))
##words_data = numpy.reshape(words_data, (len(words_data),1))
#
##Data split using cross-validation 
#features_train, features_test, label_train, label_test = cross_validation.train_test_split(words, writers, test_size=0.1, random_state = 42)
#
#print(features_train, features_test,label_train,label_test)
##print(words)