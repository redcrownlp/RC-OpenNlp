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

def FindFeatureVectorForInputText(line,StopWords):
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
     for word in StopWords:
         if word in textValue:
            line_features.append(1)  #line contains this feature 
         else:
            line_features.append(0)  #line not contains this feature 
     return line_features
def ReadTestingDataset():
	lines6,NofRowsList,NofColumnsList=ReadXlsxFile.ReadFile('./Testing_Dataset/Labeled_Result_6_Rows9999.xlsx')
	lines7,NofRowsList,NofColumnsList=ReadXlsxFile.ReadFile('./Testing_Dataset/Labeled_Result_7_Rows9999.xlsx')
	lines8,NofRowsList,NofColumnsList=ReadXlsxFile.ReadFile('./Testing_Dataset/Labeled_Result_8_Rows9999.xlsx')
	lines9,NofRowsList,NofColumnsList=ReadXlsxFile.ReadFile('./Testing_Dataset/Labeled_Result_9_Rows8062.xlsx')
        dialects_lines=lines6+lines7+lines8+lines9
        return dialects_lines

if __name__ == "__main__":
	########################################################################################## 
	# Read NLP Model
	print "1)Read NLP Model ..."
	clf=[]
	with open('OurModel.pkl', 'rb') as fid:
	       clf = cPickle.load(fid) 
	########################################################################################## 
	#Read Features Vector
	print "2)Read Features Vector ..."
	features=XlsxFileFunctions.ReadFeaturesVectorFile('Features.xlsx')
	features=features
	print "Number Of features =" + str(len(features))
	map(unicode,features)
	########################################################################################## 
	#Read Test Dataset 
	print "3)Read Testing Dataset ..."
	dialects_lines=ReadTestingDataset()

	########################################################################################## 
	#Testing Model 
	print "4)Testing Model ..."
	T_count=0.0
	F_count=0.0
	for line in dialects_lines:
	    real_label=[]
	    text=RemoveNonArabicCharacters(line.arabicTextValue)
	    line_features=FindFeatureVectorForInputText(text,features)
	    result_label=clf.predict([line_features])
	    real_label.append(line.arabicTextLabel)
	    map(unicode,real_label)
	    if result_label[0] == real_label[0]:
	       T_count=T_count+1
	    else:
	       F_count=F_count+1
	########################################################################################## 
	#Print Accuracy Result
	print "5)System Accuracy:"+ str((T_count / (T_count + F_count))*100)+"%"

