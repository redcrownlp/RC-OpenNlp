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
    ###################################################
    #Char n-grams
    #Find Char 6-gram features:
    resultLines=re.sub(' +',' ',resultLines)
    n=6
    CharNGramFeatures.Find_Char_n_gram_Features('./Features/Char_N_Grams/'+dialect_name+'_Char_'+str(n)+'_Features.xlsx',resultLines,n,CharNGramThreshold)
    #find Char 7-gram features:
    n=7
    CharNGramFeatures.Find_Char_n_gram_Features('./Features/Char_N_Grams/'+dialect_name+'_Char_'+str(n)+'_Features.xlsx',resultLines,n,CharNGramThreshold)
    #find Char 8-gram features:
    n=8
    CharNGramFeatures.Find_Char_n_gram_Features('./Features/Char_N_Grams/'+dialect_name+'_Char_'+str(n)+'_Features.xlsx',resultLines,n,CharNGramThreshold)

def Distinct_Labeled_Dataset_by_Dialects():  
    '''
          Description:
                 This function Distinct Labeled Dataset by labels.
    '''  
    #Read .xlsx File 
    lines0,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile("./Labeled_Dataset/Labeled_Result_0_Rows9999.xlsx")
    lines1,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile("./Labeled_Dataset/Labeled_Result_1_Rows9999.xlsx")
    lines2,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile("./Labeled_Dataset/Labeled_Result_2_Rows9999.xlsx")
    lines3,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile("./Labeled_Dataset/Labeled_Result_3_Rows9999.xlsx")
    lines4,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile("./Labeled_Dataset/Labeled_Result_4_Rows9999.xlsx")
    lines5,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile("./Labeled_Dataset/Labeled_Result_5_Rows9999.xlsx")
    lines6,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile("./Labeled_Dataset/Labeled_Result_6_Rows9999.xlsx")
    lines7,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile("./Labeled_Dataset/Labeled_Result_7_Rows9999.xlsx")
    lines8,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile("./Labeled_Dataset/Labeled_Result_8_Rows9999.xlsx")
    lines9,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile("./Labeled_Dataset/Labeled_Result_9_Rows8062.xlsx")
    linesList=lines0+lines1+lines2+lines3+lines4+lines5+lines6+lines7+lines8+lines9
    EgyptResult=[]
    GulfResult=[]
    MaghrebResult=[]
    LevantResult=[]
    IraqiResult=[]
    for line in linesList:
       
	#Egypt?
        if line.arabicTextLabel=="Egypt/":
                EgyptResult.append(line)
	#Gulf?
	elif line.arabicTextLabel=="Gulf/":
                GulfResult.append(line)
	#Maghreb?
	elif line.arabicTextLabel=="Maghreb/":
                MaghrebResult.append(line)
	#Levant?
	elif line.arabicTextLabel=="Levant/":
                LevantResult.append(line)
	#Iraqi?
	elif line.arabicTextLabel=="Iraqi/":
                IraqiResult.append(line)

    #Write to File
    XlsxFileFunctions.WriteToFile('./Labeled_Dataset_distinct_by_Dialects/Egypt_Dataset.xlsx',EgyptResult)
    XlsxFileFunctions.WriteToFile('./Labeled_Dataset_distinct_by_Dialects/Gulf_Dataset.xlsx',GulfResult)
    XlsxFileFunctions.WriteToFile('./Labeled_Dataset_distinct_by_Dialects/Maghreb_Dataset.xlsx',MaghrebResult)
    XlsxFileFunctions.WriteToFile('./Labeled_Dataset_distinct_by_Dialects/Levant_Dataset.xlsx',LevantResult)
    XlsxFileFunctions.WriteToFile('./Labeled_Dataset_distinct_by_Dialects/Iraqi_Dataset.xlsx',IraqiResult)


################################################################################################################################## 
def SaveFeaturesToOneFile():
    '''
          Description:
                 This function read n-grams features and store it in one file called "Features.xlsx".
    '''    
    #1)Read Features for each dialects
    Egypt_OneGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Egypt_Word_OneGram_Features.xlsx')
    Egypt_TwoGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Egypt_Word_TwoGram_Features.xlsx')
    Egypt_ThreeGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Egypt_Word_ThreeGram_Features.xlsx')

    Gulf_OneGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Gulf_Word_OneGram_Features.xlsx')
    Gulf_TwoGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Gulf_Word_TwoGram_Features.xlsx')
    Gulf_ThreeGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Gulf_Word_ThreeGram_Features.xlsx')

    Maghreb_OneGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Maghreb_Word_OneGram_Features.xlsx')
    Maghreb_TwoGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Maghreb_Word_TwoGram_Features.xlsx')
    Maghreb_ThreeGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Maghreb_Word_ThreeGram_Features.xlsx')

    Levant_OneGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Levant_Word_OneGram_Features.xlsx')
    Levant_TwoGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Levant_Word_TwoGram_Features.xlsx')
    Levant_ThreeGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Levant_Word_ThreeGram_Features.xlsx')

    Iraqi_OneGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Iraqi_Word_OneGram_Features.xlsx')
    Iraqi_TwoGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Iraqi_Word_TwoGram_Features.xlsx')
    Iraqi_ThreeGram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Word_N_Grams/Iraqi_Word_ThreeGram_Features.xlsx')
   
    Egypt_6Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Egypt_Char_6_Features.xlsx')
    Egypt_7Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Egypt_Char_7_Features.xlsx')
    Egypt_8_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Egypt_Char_8_Features.xlsx')

    Gulf_6Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Gulf_Char_6_Features.xlsx')
    Gulf_7Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Gulf_Char_7_Features.xlsx')
    Gulf_8Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Gulf_Char_8_Features.xlsx')

    Maghreb_6Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Maghreb_Char_6_Features.xlsx')
    Maghreb_7Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Maghreb_Char_7_Features.xlsx')
    Maghreb_8Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Maghreb_Char_8_Features.xlsx')

    Iraqi_6Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Iraqi_Char_6_Features.xlsx')
    Iraqi_7Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Iraqi_Char_7_Features.xlsx')
    Iraqi_8Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Iraqi_Char_8_Features.xlsx')

  
    Levant_6Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Levant_Char_6_Features.xlsx')
    Levant_7Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Levant_Char_7_Features.xlsx')
    Levant_8Gram_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFeaturesFile('./Features/Char_N_Grams/Levant_Char_8_Features.xlsx')
    ################################################################################################################################################################### 
    #Concatenate features in one vector, remove duplicates and store it in .xlsx file
    featureVector=Egypt_OneGram_lines + Egypt_TwoGram_lines + Egypt_ThreeGram_lines + Gulf_OneGram_lines + Gulf_TwoGram_lines + Gulf_ThreeGram_lines + Maghreb_OneGram_lines + Maghreb_TwoGram_lines + Maghreb_ThreeGram_lines + Levant_OneGram_lines + Levant_TwoGram_lines + Levant_ThreeGram_lines + Iraqi_OneGram_lines + Iraqi_TwoGram_lines + Iraqi_ThreeGram_lines +Egypt_6Gram_lines+Egypt_7Gram_lines+Egypt_8_lines +\
                   Gulf_6Gram_lines+Gulf_7Gram_lines+Gulf_8Gram_lines +\
                   Maghreb_6Gram_lines+Maghreb_7Gram_lines+Maghreb_8Gram_lines +\
                   Levant_6Gram_lines+Levant_7Gram_lines+Levant_8Gram_lines +\
                   Iraqi_6Gram_lines+Iraqi_7Gram_lines+Iraqi_8Gram_lines
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
    Egypt_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeled_Dataset_distinct_by_Dialects/Egypt_Dataset.xlsx')
    Gulf_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeled_Dataset_distinct_by_Dialects/Gulf_Dataset.xlsx')
    Maghreb_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeled_Dataset_distinct_by_Dialects/Maghreb_Dataset.xlsx')
    Levant_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeled_Dataset_distinct_by_Dialects/Levant_Dataset.xlsx')
    Iraqi_lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile('./Labeled_Dataset_distinct_by_Dialects/Iraqi_Dataset.xlsx')

    #find features for each dialects
    print "3)Find n-grams features..."
    CharNGramThreshold=90
    WordNGramThreshold=5
    FindFeatures('Egypt',Egypt_lines,WordNGramThreshold,CharNGramThreshold)
    FindFeatures('Gulf',Gulf_lines,WordNGramThreshold,CharNGramThreshold)
    FindFeatures('Maghreb',Maghreb_lines,WordNGramThreshold,CharNGramThreshold)
    FindFeatures('Levant',Levant_lines,WordNGramThreshold,CharNGramThreshold)
    FindFeatures('Iraqi',Iraqi_lines,WordNGramThreshold,CharNGramThreshold)


    #Save Features in Features .xlsx file
    print "4)Save features vector to 'Features.xlsx' file ..."
    SaveFeaturesToOneFile()
    




