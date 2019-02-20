#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Mohammad Modallal <m.modallal@redcrow.co> 
#######################################################################
import string
import re
import pyarabic.araby as araby
def normalize_arabic(text):
    temp=""
    for i in range(len(text)):
       if ord(text[i]) == 1573 or ord(text[i]) ==1571 or ord(text[i]) ==1649 or ord(text[i]) == 1570: ##  "إأٱآ" , "ا"
          temp=temp+u'ا'
       elif  ord(text[i]) ==1609   :#"ى", "ي"
          temp=temp+u'ي'
       elif  ord(text[i]) ==1572   :#"ؤ", "ء"
          temp=temp+u'ء'
       elif  ord(text[i]) ==1574   :#"ئ", "ء"
          temp=temp+u'ء'
       elif  ord(text[i]) ==1577   :#"ة", "ه"
          temp=temp+u'ه'
       elif  ord(text[i]) ==1711   :#"گ", "ك"
          temp=temp+u'ك'
       else:
          temp=temp+text[i]
    text=temp
    return text
#######################################################################
def remove_punctuations(text):
    exclude = set(string.punctuation)
    text = ''.join(ch for ch in text if ch not in exclude)
    return text

#######################################################################
def remove_repeating_char(text):
    return re.sub(r'(.)\1+', r'\1', text)

#######################################################################
def remove_tashkeel(text):
    text= araby.strip_tashkeel(text)
    return text

#######################################################################
def RemoveNonArabicCharacters(text):
    text = re.sub(r'[\w\s]',' ',text)
    text = re.sub(r'[#]',' ',text)
    text = re.sub(r'[?]',' ',text)
    text = re.sub(r'[$]',' ',text)
    text= "".join(re.findall(ur'[\u0620-\u06CF ]', text, re.UNICODE)) #remove non-Arabic characters
    return text


#######################################################################
def Arabic_Text_Processing(text):
    text=normalize_arabic(text)
    text=remove_punctuations(text)
    text=RemoveNonArabicCharacters(text)
    text=remove_tashkeel(text)
    text=re.sub(' +',' ',text)
    return text
