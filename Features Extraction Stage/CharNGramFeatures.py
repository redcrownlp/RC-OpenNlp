#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Mohammad Modallal <m.modallal@redcrow.co> 
'''
This model used to find Characters n-gram features: 1-grams, 2-grams and 3-grams
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

#Arabic StopWords List
stopWords = set(stopwords.words('arabic'))


def Convert_List_of_Characters_To_String(List_of_Characters):
    '''
          Description:
                 Convert List of Characters to String.
          Input:
                 -List of Characters
          Output:
                 -String.
    '''
    result=""
    for item in List_of_Characters: 
        result=result+item
    return result

def Find_Char_n_gram_Features(file_name,dialect_As_one_line,n,countThreshold):
    '''
          Description:
                 Find Char n_gram Features.
          Input:
                 -file_name: Output .xlsx File name.
                 -dialect_As_one_line: Arabic Text.
                 -countThreshold: This constant is counter threshold, the items with count less than the threshold will ignored. 
          Output:
                 -Store the characters n-grams to .xlsx file.
    '''
    nGramList= ngrams(dialect_As_one_line, n)
    result = collections.Counter(nGramList)
    resultWords=[]
    for item, count in sorted(result.iteritems()): 
                ngram_item=Convert_List_of_Characters_To_String(item)
		if ngram_item not in stopWords and count >countThreshold:
		  output=TextFreq(ngram_item,count)   
		  resultWords.append(output)
    XlsxFileFunctions.Write_Feature_Freq_ToFile(file_name,resultWords)

