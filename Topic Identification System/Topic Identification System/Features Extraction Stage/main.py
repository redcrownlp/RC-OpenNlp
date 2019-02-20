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
import WordNGramFeatures as WordNGramFeatures
import CharNGramFeatures as CharNGramFeatures


def removeDuplicates(listofElements):
    '''
          Description:
                 removeDuplicates function: This function remove duplicated item in the input List.
          Input:
                 -List of strings with duplicates.
          Output:
                 -List of strings without duplicates.
    '''
    # Create an empty list to store unique elements
    uniqueList = []
    
    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
    for elem in listofElements:
        if elem not in uniqueList:
            uniqueList.append(elem)
    
    # Return the list of unique elements        
    return uniqueList


def FindFeatures(dialect_name,dialect_lines,WordNGramThreshold,CharNGramThreshold):
    '''
          Description:
                 FindFeatures function: This function find Word n-grams and Characters n-grams features.
          Input:
                 1)dialect_name: used to named output file.
                 2)dialect_lines: string input.
                 3)WordNGramThreshold 
                 4)CharNGramThreshold
          Output:
                 -Store the features in separate files.
    '''
    resultLines=""
    for line in dialect_lines:
	    resultLines=resultLines+' '+line.arabicTextValue
    ###################################################
    #Word n-grams
    #Find Word uni-gram features:
    WordNGramFeatures.Find_Word_Uni_gram_Features('./Features/Word_N_Grams/'+dialect_name+'_Word_OneGram_Features.xlsx',resultLines,WordNGramThreshold)
    #find Word 2-gram features:
    WordNGramFeatures.Find_Word_2_gram_Features('./Features/Word_N_Grams/'+dialect_name+'_Word_TwoGram_Features.xlsx',resultLines,WordNGramThreshold)
    #find Word 3-gram features:
    WordNGramFeatures.Find_Word_3_gram_Features('./Features/Word_N_Grams/'+dialect_name+'_Word_ThreeGram_Features.xlsx',resultLines,WordNGramThreshold)


################################################################################################################################## 
def SaveFeaturesToOneFile():
    '''
          Description:
                 This function read n-grams features and store it in one file called "Features.xlsx".
    '''    
    #1)Read Features for each dialects
    Sport_OneGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Sport_Word_OneGram_Features.xlsx')
    Sport_TwoGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Sport_Word_TwoGram_Features.xlsx')
    Sport_ThreeGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Sport_Word_ThreeGram_Features.xlsx')

    Religion_OneGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Religion_Word_OneGram_Features.xlsx')
    Religion_TwoGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Religion_Word_TwoGram_Features.xlsx')
    Religion_ThreeGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Religion_Word_ThreeGram_Features.xlsx')

    Culture_OneGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Culture_Word_OneGram_Features.xlsx')
    Culture_TwoGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Culture_Word_TwoGram_Features.xlsx')
    Culture_ThreeGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Culture_Word_ThreeGram_Features.xlsx')

    Economy_OneGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Economy_Word_OneGram_Features.xlsx')
    Economy_TwoGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Economy_Word_TwoGram_Features.xlsx')
    Economy_ThreeGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Economy_Word_ThreeGram_Features.xlsx')

    Politics_OneGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Politics_Word_OneGram_Features.xlsx')
    Politics_TwoGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Politics_Word_TwoGram_Features.xlsx')
    Politics_ThreeGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Politics_Word_ThreeGram_Features.xlsx')

    Health_OneGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Health_Word_OneGram_Features.xlsx')
    Health_TwoGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Health_Word_TwoGram_Features.xlsx')
    Health_ThreeGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Health_Word_ThreeGram_Features.xlsx')
   
    #######################################################################
    #Concatenate features in one vector, remove duplicates and store it in .xlsx file
    featureVector=Sport_OneGram_lines + Sport_TwoGram_lines + Sport_ThreeGram_lines + Religion_OneGram_lines + Religion_TwoGram_lines + Religion_ThreeGram_lines + Culture_OneGram_lines + Culture_TwoGram_lines + Culture_ThreeGram_lines + Economy_OneGram_lines + Economy_TwoGram_lines + Economy_ThreeGram_lines + Politics_OneGram_lines + Politics_TwoGram_lines + Politics_ThreeGram_lines + Health_OneGram_lines + Health_TwoGram_lines + Health_ThreeGram_lines 
    features=[]
    for feature in featureVector:
        features.append(feature.arabicWord);

    #remove duplicated
    features=removeDuplicates(features)
    
    #Store features to .xlsx file to used it in testing 
    XlsxFileFunctions.Write_FeaturesVector_ToFile("Features.xlsx",features)

if __name__ == "__main__":
    print "1)Separate dataset by labels ..."
    #Distinct Labeled Dataset by Dialects
    Distinct_Labeled_Dataset_by_Dialects()
    
    #Read .xlsx File 
    print "2)Read training dataset ..."
    Sport_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeled_Dataset/Sport_Dataset.xlsx')
    Religion_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeled_Dataset/Religion_Dataset.xlsx')
    Culture_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeled_Dataset/Culture_Dataset.xlsx')
    Economy_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeled_Dataset/Economy_Dataset.xlsx')
    Politics_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeled_Dataset/Politics_Dataset.xlsx')
    Health_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeled_Dataset/Health_Dataset.xlsx')

    #find features for each dialects
    print "3)Find n-grams features..."
    CharNGramThreshold=90
    WordNGramThreshold=5
    FindFeatures('Sport',Sport_lines,WordNGramThreshold,CharNGramThreshold)
    FindFeatures('Religion',Religion_lines,WordNGramThreshold,CharNGramThreshold)
    FindFeatures('Culture',Culture_lines,WordNGramThreshold,CharNGramThreshold)
    FindFeatures('Economy',Economy_lines,WordNGramThreshold,CharNGramThreshold)
    FindFeatures('Politics',Politics_lines,WordNGramThreshold,CharNGramThreshold)
    FindFeatures('Health',Health_lines,WordNGramThreshold,CharNGramThreshold)

    #Save Features in Features .xlsx file
    print "4)Save features vector to 'Features.xlsx' file ..."
    SaveFeaturesToOneFile()
    




