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
           #Read Feature Vector
	   features_vector=XlsxFileFunctions.ReadFeaturesVectorFile('Features_Vector.xlsx')
	   map(unicode,features_vector)
	   #####################################################################
           print "##########################################################################################################" 
           print "################################ welcome to Arabic NLP Classifier ########################################"
           while True:

                print "##########################################################################################################"          
		#####################################################################
		#Read user Arabic text input
                text = raw_input("Please enter Arabic Language text(More than 100 Characters): ")
                #####################################################################
		#Remove non-Arabic text from the input text
		text=unicode(text, 'utf-8')
		text=RemoveNonArabicCharacters(text)
                if len(text)<100:
                      print "Error, Please Enter text contains more that 100 Arabic characters."
                      continue
                #####################################################################
                #print text after pre-processing
                print "########################################"
                print "Your input after pre-processing is: "
                print "		   "+text
                
                #####################################################################
                print "########################################"
                print "Choose on of the following classifiers"
                print "1) Egyptian Dialect Classifer."
                print "2) Gulf Dialect Classifer."
                print "3) Iraqi Dialect Classifer."
                print "4) Levant Dialect Classifer."
                print "5) Maghrebi Dialect Classifer."
                print "6) All Dialects Classifer."
                choiceNumber = raw_input("Enter number between 1 and 6: ")
                #####################################################################
		# Read NLP Model
		clf=[]
                #####################################################################
                with open('./Classifier_Models/All_Dialects_LogisticRegression_Model.pkl', 'rb') as fid:
		           clf = cPickle.load(fid)
                

		line_features=FindFeatureVectorForInputText(text,features_vector)
		result_label=clf.predict([line_features])
		classesResult_All=clf.predict_proba([line_features]) 

                #####################################################################
                if choiceNumber in '1':
		              with open('./Classifier_Models/Egypt_LogisticRegression_Model.pkl', 'rb') as fid:
		                            clf = cPickle.load(fid) 
                elif choiceNumber in '2':
		              with open('./Classifier_Models/Gulf_LogisticRegression_Model.pkl', 'rb') as fid:
		                            clf = cPickle.load(fid) 
                elif choiceNumber in '3':
		              with open('./Classifier_Models/Iraqi_LogisticRegression_Model.pkl', 'rb') as fid:
		                            clf = cPickle.load(fid) 
                elif choiceNumber in '4':
		              with open('./Classifier_Models/Levant_LogisticRegression_Model.pkl', 'rb') as fid:
		                            clf = cPickle.load(fid) 
                elif choiceNumber in '5':
		              with open('./Classifier_Models/Maghreb_LogisticRegression_Model.pkl', 'rb') as fid:
		                            clf = cPickle.load(fid) 
                elif choiceNumber in '6':
		              with open('./Classifier_Models/All_Dialects_LogisticRegression_Model.pkl', 'rb') as fid:
		                            clf = cPickle.load(fid) 
                else:
                      print "Error, Please Enter number between 1 and 6."
                      continue

                #####################################################################

		line_features=FindFeatureVectorForInputText(text,features_vector)
		result_label=clf.predict([line_features])
		classesResult=clf.predict_proba([line_features]) 
		labels=clf.classes_
                print "Dialect results:"
                if choiceNumber in '6':
		        print "		 Your Text is Egyptian dialect with Probability equal {0:.2f}%.".format(classesResult[0][0]*100)
		        print "		 Your Text is Gulf dialect with Probability equal {0:.2f}%.".format(classesResult[0][1]*100)
		        print "		 Your Text is Iraqi dialect with Probability equal {0:.2f}%.".format(classesResult[0][2]*100)
		        print "		 Your Text is Levant dialect with Probability equal {0:.2f}%.".format(classesResult[0][3]*100)
		        print "		 Your Text is Maghrebi dialect with Probability equal {0:.2f}%.".format(classesResult[0][4]*100)

                else:
                        if labels[0] in "Egypt/":
                            result= max(classesResult_All[0][0],classesResult[0][0])
                            print "		Your Text is Egyptian dialect with Probability equal {0:.2f}%.".format(result*100)
                        if labels[0] in "Gulf/":
                            result= max(classesResult_All[0][1],classesResult[0][0])
                            print "		Your Text is Gulf dialect with Probability equal {0:.2f}%.".format(result*100)
                        if labels[0] in "Iraqi/":
                            result= max(classesResult_All[0][2],classesResult[0][0])
                            print "		Your Text is Iraqi dialect with Probability equal {0:.2f}%.".format(result*100)
                        if labels[0] in "Levant/":
                            result= max(classesResult_All[0][3],classesResult[0][0])
                            print "		Your Text is Levant dialect with Probability equal {0:.2f}%.".format(result*100)
                        if labels[0] in "Maghreb/":
                            result= max(classesResult_All[0][4],classesResult[0][0])
                            print "		Your Text is Maghrebi dialect with Probability equal {0:.2f}%.".format(result*100)

