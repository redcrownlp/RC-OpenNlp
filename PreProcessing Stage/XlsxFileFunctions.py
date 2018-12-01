#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Mohammad Modallal <m.modallal@redcrow.co> 

from xlrd import open_workbook
import xlwt
import re
import sys, getopt, codecs, os
import csv
from itertools import izip

class DataInput(object):
    '''
       Class DataInput Description:
              This class represent lines that will read from .xlsx file.
       Fields:
              1)ArabicTextValue:
                                This field include Arabic string.   
              2)ArabicTextLabel:          
                                This field include Arabic text label. For example: Modern Standard Arabic, Gulf, Egyptian, Iraqi and Levantine
    '''
    def __init__(self, arabicTextValue):
        self.arabicTextValue = arabicTextValue

    def __str__(self):
        return("DataInput object:\n"
               "  arabicTextValue = {0}"
               .format(self.arabicTextValue))


def ReadFile(fileName):
	'''
          Description:
                 ReadFile function used to read .xlsx files that contains Arabic sentences with labels
          Input:
                 1)fileName - File name with .Xlsx extension
          Output:
                 1) lines - List of DataInput objects that represent Arabic strings with labels
                 2) NofRowsList- List of number of rows in each sheet in the file.
                 3) NofColumnsList- List of number of columns in each sheet in the file.
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
        return lines,NofRowsList,NofColumnsList

def WriteToFile(fileName,lines):
    from openpyxl import Workbook
    wb = Workbook()
    ws = wb.active
    # Rows can also be appended
   
    for line in lines:
        textValue=re.sub(r'[?a-zA-Z\w]', '',line.arabicTextValue) 
        ws.append([textValue])
    wb.save(fileName)
