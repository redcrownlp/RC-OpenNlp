#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Mohammad Modallal <m.modallal@redcrow.co> 
'''
This model used to read/write data from/to .xlsx files
'''
from xlrd import open_workbook
import xlwt
import re
import sys, getopt, codecs, os
from itertools import izip
import csv
from openpyxl import Workbook

########################################################################################## 
class DataInput(object):
    '''
       Class DataInput Description:
              This class represent lines that will read from .xlsx file.
       Fields:
              1)ArabicTextValue:
                                This field include Arabic string.   
              2)ArabicTextLabel:          
                                This field include Arabic text labels. For example: Maghreb, Gulf, Egyptian, Iraqi and Levant.
    '''
    def __init__(self, arabicTextValue, arabicTextLabel):
        self.arabicTextValue = ' '+arabicTextValue+' '
        self.arabicTextLabel = arabicTextLabel

    def __str__(self):
        return("DataInput object:\n"
               "  arabicTextValue = {0}\n"
               "  arabicTextLabel = {1}"
               .format(self.arabicTextValue, self.arabicTextLabel))

########################################################################################## 
def ReadFile(fileName):
	'''
          Description:
                 ReadFile function used to read .xlsx files that contains Arabic sentences with labels.
          Input:
                 fileName - Input File name.
          Output:
                 lines - List of DataInput objects that represent Arabic strings with labels.

        '''
        wb = open_workbook(fileName)                        #Open xlsx file which contains Arabic text with labels
	lines = []                                          #List of DataInput objects                           
	NofRowsList=[]                                      #List of sheets number_of_columns
        NofColumnsList=[]                                   #List of sheets number_of_rows
	for sheet in wb.sheets():                           #read file sheet by sheet
    		number_of_rows = sheet.nrows                #number of rows in sheet
                NofRowsList.append(number_of_rows)
    		number_of_columns = sheet.ncols             #number of columns in sheet
                NofColumnsList.append(number_of_columns)
    		rows = []
                for row in range(1, number_of_rows):
                   values = []
		   for col in range(number_of_columns):
                       value  = (sheet.cell(row,col).value)
                       try:
                          value = str(int(value))
                       except ValueError:
                          pass
                       finally:
                           values.append(value)
                   line = DataInput(*values)
                   lines.append(line)
        return lines

########################################################################################## 
def ReadFeaturesVectorFile(fileName):
        '''
          Description:
                 ReadFeaturesVectorFile function used to read .xlsx files that contains features.
          Input:
                 fileName - Input File name.
          Output:
                 lines - List of features.

        '''
        wb = open_workbook(fileName)                        #Open xlsx file
	lines = []                                          #List of DataInput objects                           
	for sheet in wb.sheets():                           #read file sheet by sheet
    		number_of_rows = sheet.nrows                #number of rows in sheet

    		number_of_columns = sheet.ncols             #number of columns in sheet

    		rows = []
                lines.append("")
                for row in range(1, number_of_rows):
                   values = []
		   for col in range(number_of_columns):
                       value  = (sheet.cell(row,col).value)
                       try:
                          value = str(int(value))
                       except ValueError:
                          pass
                       finally:
                           values.append(value)
                   line = values[0]
                   lines.append(line)                      
        return lines
