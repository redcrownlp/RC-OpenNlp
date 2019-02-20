#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Mohammad Modallal <m.modallal@redcrow.co> 
'''
This model used to traing Topic Identification system:
1) Read Features vector.
2) Read training dataset files.
3) Filling feature matrix.
4) Start traing Model using LogisticRegression classifier.
5) Save model To OurModel.pkl File.
'''
import XlsxFileFunctions 
import nltk
from nltk import ngrams
from nltk.collocations import *
import collections
from nltk.corpus import stopwords
import re
import regex
import string
import warnings
warnings.simplefilter("ignore")
from sklearn.ensemble import RandomForestClassifier
from numpy.core.umath_tests import inner1d
import numpy as np
import cPickle
import csv
from sklearn import svm
from numpy.core.umath_tests import inner1d
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

#from sklearn.model_selection import train_test_split
#X_train, X_test = train_test_split(data, test_size=0.5, random_state=int(time.time()))

def removeDuplicates(listofElements):
    
    # Create an empty list to store unique elements
    uniqueList = []
    
    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)
    
    # Return the list of unique elements        
    return uniqueList

def CheckLineContainStopwords(line,StopWords):
     '''
     fill feature vector for arabic text line: 
         if the feature exist in arabic text line then:
             append 1 to feature vector
         else: 
             append 1 to feature vector
     '''
     textValue=line.arabicTextValue
     textValue=' '+textValue+ ' '
     line_features=[]
     for word in StopWords:
         if word in textValue:
            line_features.append(1)  
         else:
            line_features.append(0) 
     return line_features

def ReadTrainingDataset():
	    lines0,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeld_Data/Labeled_Result_0_Rows9999.xlsx')
	    lines1,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeld_Data/Labeled_Result_1_Rows9999.xlsx')
	    lines2,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeld_Data/Labeled_Result_2_Rows9999.xlsx')
	    lines3,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeld_Data/Labeled_Result_3_Rows9999.xlsx')
	    lines4,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeld_Data/Labeled_Result_4_Rows9999.xlsx')
	    lines5,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeld_Data/Labeled_Result_5_Rows9999.xlsx')
            dialects_lines=lines0+lines1+lines2+lines3+lines4+lines5
            return dialects_lines

if __name__ == "__main__":
    ################################################################################################################################################################### 
    #1)Read Features vector
    print "1)Read Features vector."
    featureVector,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('Feature.xlsx')
    print "Number Of Features="+str(len(features))

    ################################################################################################################################################################### 
    #2)Read dataset file that will used for training the Model
    print "2)Read training dataset files."
    dialects_lines=ReadTrainingDataset()

    ################################################################################################################################################################### 
    #3) for each line in file find feature vector and store it in feature matrix
    print "3)Filling feature matrix."
    feature_matrix=[]
    labels=[]
    for line in dialects_lines:
       label=[]
       line_features=CheckLineContainStopwords(line,features)
       feature_matrix.append(line_features)
       label.append(line.arabicTextLabel)
       labels.append(label)
    print "End filling feature matrix" 
    ###################################################################################################################################################################
    #4) Start training model using RandomForest Classifier 
    print "4) Start traing Model using LogisticRegression classifier."
    clf= LogisticRegression()
    Trainclass=clf.fit(feature_matrix, labels)
    ################################################################################################################################################################### 
    #5)Save model To .pkl File
    print "5) Save model To OurModel.pkl File."
    with open('OurModel.pkl', 'wb') as fid:
       cPickle.dump(Trainclass, fid)   








