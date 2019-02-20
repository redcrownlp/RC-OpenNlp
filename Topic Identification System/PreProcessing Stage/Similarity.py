#!/usr/bin/python
# -*- coding: utf-8 -*-
# author: Mohammad Modallal <m.modallal@redcrow.co>

from difflib import SequenceMatcher

def similar(str1, str2):
    '''
          Description:
                 Find The similarity between  two strings (Str1 and Str2) 
          Input:
                 1)str1  - First string
                 2)str2  - Second strng
          Output:
                 float number between 0 and 1. This number represent the similarity between Str1 and Str2.
                 if (Str1 and Str2 are similar) Then:
                     The result is near 1
                 else:
                     The result is near 0  
        '''
    return SequenceMatcher(None, str1, str2).ratio()

