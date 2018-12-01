#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Mohammad Modallal <m.modallal@redcrow.co> 

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
from numpy.core.umath_tests import inner1d
import numpy as np
import cPickle
def RemoveNonArabicCharacters(text):
    '''
          Description:
               Remove Non-Arabic Characters
          Input:
               Arabic text contains non-arabic characters
          Output:
               Text contains only arabic characters   
    '''
    exclude = set(string.punctuation)
    text= "".join(re.findall(ur'[\u0620-\u06CF ]', text, re.UNICODE)) #remove non-Arabic characters
    text= ''.join(ch for ch in text if ch not in exclude)#remove punctuation
    text=re.sub(' +',' ',text) #Remove spaces
    return text

def FindFeatureVectorForInputText(line,features_vector):
     '''
     fill feature vector for arabic text line: 
         if the feature exist in arabic text line then:
             append 1 to feature vector
         else: 
             append 0 to feature vector
     '''
     textValue=line
     textValue=' '+textValue+ ' '
     line_features=[]
     for word in features_vector:
         if word in textValue:
            line_features.append(1)  #line contains this feature 
         else:
            line_features.append(0)  #line not contains this feature 
     return line_features

###################################################################################################################################################################
if __name__ == "__main__":
                #####################################################################
		# Read NLP Model
		clf=[]
		with open('LogisticRegression_Model.pkl', 'rb') as fid:
		       clf = cPickle.load(fid) 
                #####################################################################
		#Read Feature Vector
		features_vector=XlsxFileFunctions.ReadFeaturesVectorFile('Features_Vector.xlsx')
		map(unicode,features_vector)
		#####################################################################
		#Read user Arabic text input
		text="حاجة بسيطة كده يسطا عورتله ايدة بس ✌ https://t.co/Gowq62bw5t"
		#####################################################################
		#Remove non-Arabic text from the input text
		text=unicode(text, 'utf-8')
		text=RemoveNonArabicCharacters(text)
                print "Your input: "
                print "		   "+text
                #####################################################################
		line_features=FindFeatureVectorForInputText(text,features_vector)
		result_label=clf.predict([line_features])
		classesResult=clf.predict_proba([line_features]) 
		labels=clf.classes_
                print "Dialect results:"
		print "		"+labels[0] + " dialect with Accuracy equal {0:.2f}%.".format(classesResult[0][0]*100)
		print "		"+labels[1] + " dialect with Accuracy {0:.2f}%.".format(classesResult[0][1]*100)
		print "		"+labels[2] + " dialect with Accuracy {0:.2f}%.".format(classesResult[0][2]*100)
		print "		"+labels[3] + " dialect with Accuracy {0:.2f}%.".format(classesResult[0][3]*100)
		print "		"+labels[4] + " dialect with Accuracy {0:.2f}%.".format(classesResult[0][4]*100)

