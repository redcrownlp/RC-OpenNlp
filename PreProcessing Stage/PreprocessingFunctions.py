#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Mohammad Modallal <m.modallal@redcrow.co> 
from XlsxFileFunctions import DataInput
import re
import Similarity 
import regex
import string
def RemoveNonArabicCharacters(text):
    '''
          Description:
               Remove Non-Arabic Characters fr
          Input:
               Arabic text contains non-arabic characters
          Output:
               Text contains only arabic characters   
    '''
    exclude = set(string.punctuation)
    text= "".join(re.findall(ur'[\u0620-\u06CF ]', text, re.UNICODE)) #remove non-Arabic characters
    text= ''.join(ch for ch in text if ch not in exclude)#remove: ?;.،
    text=re.sub(' +',' ',text)
    return text

def RemoveNonArabicCharactersFromListOfLines(lines):
    '''
          Description:
               Remove Non-Arabic Characters from list of lines
          Input:
               list of Arabic lines contains non-arabic characters
          Output:
               list of Arabic lines contains only arabic characters   
    '''
    result=[]
    for line in lines:
            textValue=RemoveNonArabicCharacters(line.arabicTextValue)
            resultLine=DataInput(textValue)
            result.append(resultLine)
    return result

def RemoveSimilarLines(lines):
    	'''
          Description:
               delete lines with similarty < 80%
          Input:
               List of Lines
          Output:
               List of Lines   
        '''

        count=0
        i=1
        for line1 in lines:
             if i%500==0:
                 print i
             j=1
             for line2 in lines[i:]:
                    x=Similarity.similar(line1.arabicTextValue, line2.arabicTextValue)
		    if(x>0.8):
                        del lines[j+i-1]
                        count=count+1
		    else:    
                      j=j+1
             i=i+1
        return lines
