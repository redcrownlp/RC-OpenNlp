#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Mohammad Modallal <m.modallal@redcrow.co> 
'''
This model used to find word n-gram features
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
from XlsxFileFunctions import TextFreq

#Arabic StopWords
stopWords = set(stopwords.words('arabic'))

def Find_Word_Uni_gram_Features(file_name,dialect_As_one_line,WordNGramThreshold):
    '''
          Description:
                 Find Word 1_gram Features.
          Input:
                 -file_name: Output .xlsx File name.
                 -dialect_As_one_line: Arabic Text.
                 -WordNGramThreshold: This constant is counter threshold, the items with count less than the threshold will ignored. 
          Output:
                 -Store the Word 1-grams to .xlsx file.
    '''
    oneGramList= ngrams(dialect_As_one_line.split(), 1)
    result = collections.Counter(oneGramList)
    resultWords=[]
    for item, count in sorted(result.iteritems()): 
		if count> WordNGramThreshold and len(item[0])>1 and item[0] not in stopWords:
		  output=TextFreq(item[0],count)   
		  resultWords.append(output)
    XlsxFileFunctions.Write_Feature_Freq_ToFile(file_name,resultWords)

def Find_Word_2_gram_Features(file_name,dialect_As_one_line,WordNGramThreshold):   
    '''
          Description:
                 Find Word 2_gram Features.
          Input:
                 -file_name: Output .xlsx File name.
                 -dialect_As_one_line: Arabic Text.
                 -WordNGramThreshold: This constant is counter threshold, the items with count less than the threshold will ignored. 
          Output:
                 -Store the Word 2-grams to .xlsx file.
    '''
    twoGramList= ngrams(dialect_As_one_line.split(), 2)
    result = collections.Counter(twoGramList)
    resultWords=[]
    for item, count in sorted(result.iteritems()): 
       if count> WordNGramThreshold:
	 output=TextFreq(item[0] +" "+item[1],count)  
	 resultWords.append(output)
    XlsxFileFunctions.Write_Feature_Freq_ToFile(file_name,resultWords)

def Find_Word_3_gram_Features(file_name,dialect_As_one_line,WordNGramThreshold):  
    '''
          Description:
                 Find Word 3_gram Features.
          Input:
                 -file_name: Output .xlsx File name.
                 -dialect_As_one_line: Arabic Text.
                 -WordNGramThreshold: This constant is counter threshold, the items with count less than the threshold will ignored. 
          Output:
                 -Store the Word 3-grams to .xlsx file.
    '''
    threeGramList= ngrams(dialect_As_one_line.split(), 3)
    result = collections.Counter(threeGramList)
    resultWords=[]
    for item, count in sorted(result.iteritems()): 
           if count> WordNGramThreshold:
                 output=TextFreq(item[0] +" "+item[1]+" "+item[2],count) 
		 resultWords.append(output)
    XlsxFileFunctions.Write_Feature_Freq_ToFile(file_name,resultWords)

