# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 10:17:34 2018

@author: Safelink
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:54:18 2018

@author: Safelink
"""
import pickle
import numpy
from sklearn import cross_validation
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import f_classif, SelectPercentile

def preprocess(word_data = "word_data.pkl", writers = "writers.pkl"):
    
    """
        1. perform data extraction
        2. Carry out sklearn cross validation for data split
        3. Carry out TfidVectorization protocol
        4. Perform Feature Selection algorithm
        5. Print out the data for both parties.
        6. return training, Testing samples and corresponding labels.
    
    """
    
    writers=[]
    words_data=[]
    file = open("words_data.txt","r", errors='ignore')
    file_w = open("Writers.txt","r", errors='ignore')
    for line in file.readlines():
        for word in line.split():
            words_data.append(word)
        #print(line)
    for line in file_w.readlines():
        for word in line.split():
            writers.append(word)
        #print(line)

    #Data split using cross-validation 
    features_train, features_test, label_train, label_test = cross_validation.train_test_split(words_data, writers, test_size=0.1, random_state = 42)
    
    #Tfidfvectorization protocol
    vectorizer = TfidfVectorizer(sublinear_tf =True, max_df = 0.5, stop_words="english")
    features_train_transformed = vectorizer.fit_transform(features_train)
    features_test_transformed = vectorizer.transform(features_test)
    
    #Perform feature selection
    selection = SelectPercentile(f_classif, percentile=1)
    selection.fit(features_train_transformed, label_train)
    features_train_transformed = selection.transform(features_train_transformed).toarray()
    features_test_transformed = selection.transform(features_test_transformed).toarray()
    
    
    
    return features_train_transformed, label_train, features_test_transformed, label_test


def postprocess(Word, label_test):
    
    """
        1. perform data extraction
        2. Carry out sklearn cross validation for data split
        3. Carry out TfidVectorization protocol
        4. Perform Feature Selection algorithm
        5. Print out the data for both parties.
        6. return training, Testing samples and corresponding labels.
    
    """
    
    
    Word_test = []
    Word_test.append(Word)
    
    #Tfidfvectorization protocol
    vectorizer = TfidfVectorizer(sublinear_tf =True)
    Word_test = vectorizer.fit_transform(Word_test).toarray()
    
    #Perform feature selection
    
    
    
    return Word_test