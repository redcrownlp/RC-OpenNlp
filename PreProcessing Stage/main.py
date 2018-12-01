#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Mohammad Modallal <m.modallal@redcrow.co> 

''' 
This model used for pre-pocessing Arabic texts as following:
1) Read dataset .xlsx file.
2) Remove non-arabic characters(this include removing links, other langauges characters, special characters, digits,spaces,...etc).
3) delete lines with similarty < 80%
4) Store Dataset after Preprocessing to .xlsx file
'''

import XlsxFileFunctions
import PreprocessingFunctions

if __name__ == "__main__":

    #Read .xlsx File 
    print "1) Read dataset .xlsx file ..."
    lines,NofRowsList,NofColumnsList=XlsxFileFunctions.ReadFile("Dataset_before_Preprocessing.xlsx")
    #Remove non-Arabic characters
    print "2) Remove non-arabic characters ..."
    lines=PreprocessingFunctions.RemoveNonArabicCharactersFromListOfLines(lines);
    #Remove duplicate lines in file.
    print "3) delete lines with similarty < 80% ..."
    lines=PreprocessingFunctions.RemoveSimilarLines(lines)
    #Write to File
    print "4) Store Dataset after Preprocessing to .xlsx file"
    XlsxFileFunctions.WriteToFile('Dataset_after_Preprocessing.xlsx',lines)

