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
import warnings
warnings.simplefilter("ignore")
from numpy.core.umath_tests import inner1d
import numpy as np
import cPickle
import pyarabic.araby as araby
import pyarabic.number as number
def RemoveNonArabicCharacters(text):
    '''
          Description:
               Remove Non-Arabic Characters fr
          Input:
               Arabic text contains non-arabic characters
          Output:
               Text contains only arabic characters   
    '''
    #remove Tashkeel
    text= araby.strip_tashkeel(text)
    exclude = set(string.punctuation)
    text= "".join(re.findall(ur'[\u0620-\u06CF ]', text, re.UNICODE)) #remove non-Arabic characters
    text= ''.join(ch for ch in text if ch not in exclude)#remove: ?;.،
    text=re.sub(' +',' ',text)
    return text

def FindFeatureVectorForInputText(line,features_vector):
     '''
     fill feature vector for arabic text line: 
         if the feature exist in arabic text line then:
             append 1 to feature vector
         else: 
             append 0 to feature vector
     '''
     textValue=line
     textValue=' '+textValue+ ' '
     line_features=[]
     for word in features_vector:
         if word in textValue:
            line_features.append(1)  #line contains this feature 
         else:
            line_features.append(0)  #line not contains this feature 
     return line_features

###################################################################################################################################################################
if __name__ == "__main__":
           #####################################################################
           #Read Feature Vector
	   features_vector=XlsxFileFunctions.ReadFeaturesVectorFile('Features_Vector.xlsx')
	   map(unicode,features_vector)
           Features_Vector_93k=XlsxFileFunctions.ReadFeaturesVectorFile('Features_Vector_93k.xlsx')
	   map(unicode,Features_Vector_93k)
           Features_Vector_75k=XlsxFileFunctions.ReadFeaturesVectorFile('Features_Vector_75k.xlsx')
	   map(unicode,Features_Vector_75k)
	   #####################################################################
           print "##########################################################################################################" 
           print "################################ welcome to Arabic NLP Classifier ########################################"
           while True:

                print "##########################################################################################################"          
		#####################################################################
		#Read user Arabic text input
                text = raw_input("Please enter Arabic Language text(More than 100 Characters): ")
                #####################################################################
		#Remove non-Arabic text from the input text
		text=unicode(text, 'utf-8')
		text=RemoveNonArabicCharacters(text)
                if len(text)<100:
                      print "Error, Please Enter text contains more that 100 Arabic characters."
                      continue
                #####################################################################
                #print text after pre-processing
                print "########################################"
                print "Your input after pre-processing is: "
                print "		   "+text
                #####################################################################
                print "########################################"
                print "Choose on of the following classifiers"
                print "1) Egyptian Dialect Classifer."
                print "2) Gulf Dialect Classifer."
                print "3) Iraqi Dialect Classifer."
                print "4) Levant Dialect Classifer."
                print "5) Maghrebi Dialect Classifer."
                print "6) All Dialects Classifer."
                choiceNumber = raw_input("Enter number between 1 and 6: ")
                ############################################################################################################################################################  
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                #################################################                      Single Dialects                         #############################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
		# Read NLP Model
		clf=[]
                #####################################################################
                with open('./Classifier_Models/Egypt_LogisticRegression_Model.pkl', 'rb') as fid:
		           clf = cPickle.load(fid)
		line_features=FindFeatureVectorForInputText(text,features_vector)
                result_label=clf.predict([line_features])
		classesResult=clf.predict_proba([line_features]) 
		labels=clf.classes_
                Single_Dialect_Egyptian=classesResult[0][0]*100
                ############################################################################################################################################################
		# Read NLP Model
		clf=[]
                #####################################################################
                with open('./Classifier_Models/Gulf_LogisticRegression_Model.pkl', 'rb') as fid:
		           clf = cPickle.load(fid)
                result_label=clf.predict([line_features])
		classesResult=clf.predict_proba([line_features]) 
		labels=clf.classes_
                Single_Dialect_Gulf=classesResult[0][0]*100
                ############################################################################################################################################################
		# Read NLP Model
		clf=[]
                #####################################################################
                with open('./Classifier_Models/Iraqi_LogisticRegression_Model.pkl', 'rb') as fid:
		           clf = cPickle.load(fid)
                result_label=clf.predict([line_features])
		classesResult=clf.predict_proba([line_features]) 
		labels=clf.classes_
                Single_Dialect_Iraqi=classesResult[0][0]*100

                ############################################################################################################################################################
		# Read NLP Model
		clf=[]
                #####################################################################
                with open('./Classifier_Models/Levant_LogisticRegression_Model.pkl', 'rb') as fid:
		           clf = cPickle.load(fid)
                result_label=clf.predict([line_features])
		classesResult=clf.predict_proba([line_features]) 
		labels=clf.classes_
                Single_Dialect_Levant=classesResult[0][0]*100

                ############################################################################################################################################################
		# Read NLP Model
		clf=[]
                #####################################################################
                with open('./Classifier_Models/Maghreb_LogisticRegression_Model.pkl', 'rb') as fid:
		           clf = cPickle.load(fid)
                result_label=clf.predict([line_features])
		classesResult=clf.predict_proba([line_features]) 
		labels=clf.classes_
                Single_Dialect_Maghrebi=classesResult[0][0]*100  

                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ####################################################      2-grams /Six dialect Togathers                     ############################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
		# Read NLP Model
		clf=[]
                #####################################################################
                with open('./Classifier_Models/Six_LogisticRegression_Model_3.pkl', 'rb') as fid:
		           clf = cPickle.load(fid)

		line_features=FindFeatureVectorForInputText(text,Features_Vector_75k)
		result_label=clf.predict([line_features])
		classesResult=clf.predict_proba([line_features]) 
		labels=clf.classes_
                Two_gram_Six_Dilects_Egyptian=classesResult[0][0]*100
                Two_gram_Six_Dilects_Gulf=classesResult[0][1]*100
                Two_gram_Six_Dilects_Iraqi=classesResult[0][2]*100
                Two_gram_Six_Dilects_Levant=classesResult[0][3]*100
                Two_gram_Six_Dilects_Maghrebi=classesResult[0][4]*100
                Two_gram_Six_Dilects_ModernStandard=classesResult[0][5]*100
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ####################################################                2-grams ModernStandard/Non_ModernStandard      #########################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
		# Read NLP Model
		clf=[]
                #####################################################################
                with open('./Classifier_Models/Six_LogisticRegression_Model_1.pkl', 'rb') as fid:
		           clf = cPickle.load(fid)

		line_features=FindFeatureVectorForInputText(text,Features_Vector_75k)
		result_label=clf.predict([line_features])
		classesResult=clf.predict_proba([line_features]) 
		labels=clf.classes_
                Two_gram_Modern=classesResult[0][0]*100
                Two_gram_Not_Modern=classesResult[0][1]*100
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ####################################################                Algorthim for Single                           #########################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                print "#####################################################################"
                if choiceNumber in '1':
                               other= Single_Dialect_Gulf+ Single_Dialect_Iraqi+Single_Dialect_Levant+Single_Dialect_Maghrebi 
                               Egyptian_Result=max(Two_gram_Six_Dilects_Egyptian,Single_Dialect_Egyptian)
                               ModernStandard_Result=max(Two_gram_Modern,Two_gram_Six_Dilects_ModernStandard)
                               Other_Result=other
                               if (Other_Result>100):
                                  Other_Result=max(Single_Dialect_Gulf,Single_Dialect_Iraqi, Single_Dialect_Levant,Single_Dialect_Maghrebi)

                               if Egyptian_Result > 75:
                                       if ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2

                                       Other_Result=Other_Result/2

		                       Egyptian_Result=100 - (ModernStandard_Result+Other_Result)
                               elif Egyptian_Result > 50:
                                       Egyptian_Result=Egyptian_Result/1.5
		                       if ModernStandard_Result > 40:
	                                        ModernStandard_Result=ModernStandard_Result/2
		                       else:
                                                ModernStandard_Result=ModernStandard_Result
                                       Other_Result=100 - (ModernStandard_Result+Egyptian_Result)
                               elif Egyptian_Result > 20:    
                                       if ModernStandard_Result > 95:
                                            ModernStandard_Result=ModernStandard_Result-Egyptian_Result
                                       elif ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                            Egyptian_Result=Egyptian_Result/2
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2
                                            Egyptian_Result=Egyptian_Result/2
                                       Other_Result=100 - (ModernStandard_Result+Egyptian_Result)
                               else:
                                       if ModernStandard_Result > 95 and Other_Result<60:
                                            ModernStandard_Result=ModernStandard_Result-Egyptian_Result
                                       elif ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2
                                       Other_Result=100 - (ModernStandard_Result+Egyptian_Result) 
                               if Egyptian_Result<0 or ModernStandard_Result<0 or (100-(Egyptian_Result+ModernStandard_Result))<0:
		                       print "		Your Text is Egyptian dialect with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_Egyptian)
				       print "		Your Text is Modern standard Arabic with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_ModernStandard)
				       print "		Your Text is other dialects with Probability equal {0:.2f}%.".format(100-(Two_gram_Six_Dilects_Egyptian + Two_gram_Six_Dilects_ModernStandard))  
                               else:
		                       print "		Your Text is Egyptian dialect with Probability equal {0:.2f}%.".format(Egyptian_Result)
				       print "		Your Text is Modern standard Arabic with Probability equal {0:.2f}%.".format(ModernStandard_Result)
				       print "		Your Text is other dialects with Probability equal {0:.2f}%.".format(100-(Egyptian_Result+ModernStandard_Result))  
                #####################################################################
                elif choiceNumber in '2':
                               other= Single_Dialect_Egyptian+ Single_Dialect_Iraqi+Single_Dialect_Levant+Single_Dialect_Maghrebi 
                               Gulf_Result=max(Two_gram_Six_Dilects_Gulf,Single_Dialect_Gulf)
                               ModernStandard_Result=max(Two_gram_Modern,Two_gram_Six_Dilects_ModernStandard)
                               Other_Result=other
                               if (Other_Result>100):
                                  Other_Result=max(Single_Dialect_Egyptian,Single_Dialect_Iraqi, Single_Dialect_Levant,Single_Dialect_Maghrebi)

                               if Gulf_Result > 75:
                                       if ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2

                                       Other_Result=Other_Result/2

		                       Gulf_Result=100 - (ModernStandard_Result+Other_Result)
                               elif Gulf_Result > 50:
                                       Gulf_Result=Gulf_Result/1.5
		                       if ModernStandard_Result > 40:
	                                        ModernStandard_Result=ModernStandard_Result/2
		                       else:
                                                ModernStandard_Result=ModernStandard_Result
                                       Other_Result=100 - (ModernStandard_Result+Gulf_Result)
                               elif Gulf_Result > 20:    
                                       if ModernStandard_Result > 95:
                                            ModernStandard_Result=ModernStandard_Result-Gulf_Result
                                       elif ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                            Gulf_Result=Gulf_Result/2
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2
                                            Gulf_Result=Gulf_Result/2
                                       Other_Result=100 - (ModernStandard_Result+Gulf_Result)
                               else:
                                       if ModernStandard_Result > 95 and Other_Result<60:
                                            ModernStandard_Result=ModernStandard_Result-Gulf_Result
                                       elif ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2
                                       Other_Result=100 - (ModernStandard_Result+Gulf_Result) 
                               if Gulf_Result<0 or ModernStandard_Result<0 or (100-(Gulf_Result+ModernStandard_Result))<0:
		                       print "		Your Text is Gulf dialect with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_Gulf)
				       print "		Your Text is Modern standard Arabic with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_ModernStandard)
				       print "		Your Text is other dialects with Probability equal {0:.2f}%.".format(100-(Two_gram_Six_Dilects_Gulf + Two_gram_Six_Dilects_ModernStandard))  
                               else:
		                       print "		Your Text is Gulf dialect with Probability equal {0:.2f}%.".format(Gulf_Result)
				       print "		Your Text is Modern standard Arabic with Probability equal {0:.2f}%.".format(ModernStandard_Result)
				       print "		Your Text is other dialects with Probability equal {0:.2f}%.".format(100-(Gulf_Result+ModernStandard_Result))
                #####################################################################
                elif choiceNumber in '3':
                               other= Single_Dialect_Gulf+ Single_Dialect_Egyptian+Single_Dialect_Levant+Single_Dialect_Maghrebi 
                               Iraqi_Result=max(Two_gram_Six_Dilects_Iraqi,Single_Dialect_Iraqi)
                               ModernStandard_Result=max(Two_gram_Modern,Two_gram_Six_Dilects_ModernStandard)
                               Other_Result=other
                               if (Other_Result>100):
                                  Other_Result=max(Single_Dialect_Gulf,Single_Dialect_Egyptian, Single_Dialect_Levant,Single_Dialect_Maghrebi)

                               if Iraqi_Result > 75:
                                       if ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2

                                       Other_Result=Other_Result/2

		                       Iraqi_Result=100 - (ModernStandard_Result+Other_Result)
                               elif Iraqi_Result > 50:
                                       Iraqi_Result=Iraqi_Result/1.5
		                       if ModernStandard_Result > 40:
	                                        ModernStandard_Result=ModernStandard_Result/2
		                       else:
                                                ModernStandard_Result=ModernStandard_Result
                                       Other_Result=100 - (ModernStandard_Result+Iraqi_Result)
                               elif Iraqi_Result > 20:    
                                       if ModernStandard_Result > 95:
                                            ModernStandard_Result=ModernStandard_Result-Iraqi_Result
                                       elif ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                            Iraqi_Result=Iraqi_Result/2
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2
                                            Iraqi_Result=Iraqi_Result/2
                                       Other_Result=100 - (ModernStandard_Result+Iraqi_Result)
                               else:
                                       if ModernStandard_Result > 95 and Other_Result<60:
                                            ModernStandard_Result=ModernStandard_Result-Iraqi_Result
                                       elif ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2
                                       Other_Result=100 - (ModernStandard_Result+Iraqi_Result) 
                               if Iraqi_Result<0 or ModernStandard_Result<0 or (100-(Iraqi_Result+ModernStandard_Result))<0:
		                       print "		Your Text is Iraqi dialect with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_Iraqi)
				       print "		Your Text is Modern standard Arabic with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_ModernStandard)
				       print "		Your Text is other dialects with Probability equal {0:.2f}%.".format(100-(Two_gram_Six_Dilects_Iraqi + Two_gram_Six_Dilects_ModernStandard))  
                               else:
		                       print "		Your Text is Iraqi dialect with Probability equal {0:.2f}%.".format(Iraqi_Result)
				       print "		Your Text is Modern standard Arabic with Probability equal {0:.2f}%.".format(ModernStandard_Result)
				       print "		Your Text is other dialects with Probability equal {0:.2f}%.".format(100-(Iraqi_Result+ModernStandard_Result))  
                #####################################################################
                elif choiceNumber in '4':
                               other= Single_Dialect_Gulf+ Single_Dialect_Iraqi+Single_Dialect_Egyptian+Single_Dialect_Maghrebi 
                               Levant_Result=max(Two_gram_Six_Dilects_Levant,Single_Dialect_Levant)
                               ModernStandard_Result=max(Two_gram_Modern,Two_gram_Six_Dilects_ModernStandard)
                               Other_Result=other
                               if (Other_Result>100):
                                  Other_Result=max(Single_Dialect_Gulf,Single_Dialect_Iraqi, Single_Dialect_Egyptian,Single_Dialect_Maghrebi)

                               if Levant_Result > 75:
                                       if ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2

                                       Other_Result=Other_Result/2

		                       Levant_Result=100 - (ModernStandard_Result+Other_Result)
                               elif Levant_Result > 50:
                                       Levant_Result=Levant_Result/1.5
		                       if ModernStandard_Result > 40:
	                                        ModernStandard_Result=ModernStandard_Result/2
		                       else:
                                                ModernStandard_Result=ModernStandard_Result
                                       Other_Result=100 - (ModernStandard_Result+Levant_Result)
                               elif Levant_Result > 20:    
                                       if ModernStandard_Result > 95:
                                            ModernStandard_Result=ModernStandard_Result-Levant_Result
                                       elif ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                            Levant_Result=Levant_Result/2
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2
                                            Levant_Result=Levant_Result/2
                                       Other_Result=100 - (ModernStandard_Result+Levant_Result)
                               else:
                                       if ModernStandard_Result > 95 and Other_Result<60:
                                            ModernStandard_Result=ModernStandard_Result-Levant_Result
                                       elif ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2
                                       Other_Result=100 - (ModernStandard_Result+Levant_Result) 
                               if Levant_Result<0 or ModernStandard_Result<0 or (100-(Levant_Result+ModernStandard_Result))<0:
		                       print "		Your Text is Levant dialect with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_Levant)
				       print "		Your Text is Modern standard Arabic with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_ModernStandard)
				       print "		Your Text is other dialects with Probability equal {0:.2f}%.".format(100-(Two_gram_Six_Dilects_Levant + Two_gram_Six_Dilects_ModernStandard))  
                               else:
		                       print "		Your Text is Levant dialect with Probability equal {0:.2f}%.".format(Levant_Result)
				       print "		Your Text is Modern standard Arabic with Probability equal {0:.2f}%.".format(ModernStandard_Result)
				       print "		Your Text is other dialects with Probability equal {0:.2f}%.".format(100-(Levant_Result+ModernStandard_Result))  
                #####################################################################
                elif choiceNumber in '5':
                               other= Single_Dialect_Gulf+ Single_Dialect_Iraqi+Single_Dialect_Levant+Single_Dialect_Egyptian 
                               Maghrebi_Result=max(Two_gram_Six_Dilects_Maghrebi,Single_Dialect_Maghrebi)
                               ModernStandard_Result=max(Two_gram_Modern,Two_gram_Six_Dilects_ModernStandard)
                               Other_Result=other
                               if (Other_Result>100):
                                  Other_Result=max(Single_Dialect_Gulf,Single_Dialect_Iraqi, Single_Dialect_Levant,Single_Dialect_Egyptian)

                               if Maghrebi_Result > 75:
                                       if ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2

                                       Other_Result=Other_Result/2

		                       Maghrebi_Result=100 - (ModernStandard_Result+Other_Result)
                               elif Maghrebi_Result > 50:
                                       Maghrebi_Result=Maghrebi_Result/1.5
		                       if ModernStandard_Result > 40:
	                                        ModernStandard_Result=ModernStandard_Result/2
		                       else:
                                                ModernStandard_Result=ModernStandard_Result
                                       Other_Result=100 - (ModernStandard_Result+Maghrebi_Result)
                               elif Maghrebi_Result > 20:    
                                       if ModernStandard_Result > 95:
                                            ModernStandard_Result=ModernStandard_Result-Maghrebi_Result
                                       elif ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                            Maghrebi_Result=Maghrebi_Result/2
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2
                                            Maghrebi_Result=Maghrebi_Result/2
                                       Other_Result=100 - (ModernStandard_Result+Maghrebi_Result)
                               else:
                                       if ModernStandard_Result > 95 and Other_Result<60:
                                            ModernStandard_Result=ModernStandard_Result-Maghrebi_Result
                                       elif ModernStandard_Result > 30:
                                            ModernStandard_Result=ModernStandard_Result/4
                                       else:
                                            ModernStandard_Result=ModernStandard_Result/2
                                       Other_Result=100 - (ModernStandard_Result+Maghrebi_Result) 
                               if Maghrebi_Result<0 or ModernStandard_Result<0 or (100-(Maghrebi_Result+ModernStandard_Result))<0:
		                       print "		Your Text is Maghrebi dialect with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_Maghrebi)
				       print "		Your Text is Modern standard Arabic with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_ModernStandard)
				       print "		Your Text is other dialects with Probability equal {0:.2f}%.".format(100-(Two_gram_Six_Dilects_Maghrebi + Two_gram_Six_Dilects_ModernStandard))  
                               else:
		                       print "		Your Text is Maghrebi dialect with Probability equal {0:.2f}%.".format(Maghrebi_Result)
				       print "		Your Text is Modern standard Arabic with Probability equal {0:.2f}%.".format(ModernStandard_Result)
				       print "		Your Text is other dialects with Probability equal {0:.2f}%.".format(100-(Maghrebi_Result+ModernStandard_Result)) 
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ####################################################                Algorthim for All dialects                     #########################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                ############################################################################################################################################################
                elif choiceNumber in '6':

                        max_Egyptian=max(Two_gram_Six_Dilects_Egyptian,Single_Dialect_Egyptian)
                        max_Gulf=max(Two_gram_Six_Dilects_Gulf,Single_Dialect_Gulf)                
                        max_Iraqi=max(Two_gram_Six_Dilects_Iraqi,Single_Dialect_Iraqi)  
                        max_Levant=max(Two_gram_Six_Dilects_Levant,Single_Dialect_Levant)    
                        max_Maghrebi=max(Two_gram_Six_Dilects_Maghrebi,Single_Dialect_Maghrebi) 
                        total_result=0
                        total=max_Egyptian + max_Gulf + max_Iraqi + max_Levant + max_Maghrebi
                        if total>100:
                                total=(total+10)/100
		                max_Egyptian=max_Egyptian/total
                                print max_Egyptian
		                max_Gulf=max_Gulf/total                
		                max_Iraqi=max_Iraqi/total  
		                max_Levant=max_Levant/total    
		                max_Maghrebi=max_Maghrebi/total 

                        if max_Egyptian > 95:
                             egyptian_result=max_Egyptian-(Two_gram_Modern/2+max_Gulf+max_Iraqi+max_Levant+max_Maghrebi)
                             total_result=total_result+egyptian_result
                        else:
                             egyptian_result=max_Egyptian
                             total_result=total_result+max_Egyptian

                        if max_Gulf > 95:
                             gulf_result=max_Gulf-(Two_gram_Modern/2+max_Egyptian+max_Iraqi+max_Levant+max_Maghrebi)
                             total_result=total_result+gulf_result
                        else:
			     gulf_result=max_Gulf
                             total_result=total_result+gulf_result

                        if max_Iraqi > 95:
		             iraqi_result=max_Iraqi-(Two_gram_Modern/2+max_Gulf+max_Egyptian+max_Levant+max_Maghrebi)
                             total_result=total_result+iraqi_result
                        else:
			     iraqi_result=max_Iraqi
                             total_result=total_result+iraqi_result

                        if max_Levant > 95:
		             levant_result=max_Levant-(Two_gram_Modern/2+max_Gulf+max_Iraqi+max_Egyptian+max_Maghrebi)
                             total_result=total_result+levant_result
                        else:
			     levant_result=max_Levant
                             total_result=total_result+levant_result

                        if max_Maghrebi > 95:
		             maghrebi_result=max_Maghrebi-(Two_gram_Modern/2+max_Gulf+max_Iraqi+max_Levant+max_Egyptian)
                             total_result=total_result+maghrebi_result
                        else:
			     maghrebi_result=max_Maghrebi
                             total_result=total_result+maghrebi_result

                        if egyptian_result<0 or gulf_result<0 or iraqi_result<0 or levant_result<0 or maghrebi_result<0 or 100-total_result<0:
				print "		 Your Text is Egyptian dialect with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_Egyptian)
				print "		 Your Text is Gulf dialect with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_Gulf)
		                print "		 Your Text is Iraqi dialect with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_Iraqi)
				print "		 Your Text is Levant dialect with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_Levant)
				print "		 Your Text is Maghrebi dialect with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_Maghrebi)
				print "		 Your Text is ModernStandard dialect with Probability equal {0:.2f}%.".format(Two_gram_Six_Dilects_ModernStandard)
                        else:
				print "		 Your Text is Egyptian dialect with Probability equal {0:.2f}%.".format(egyptian_result)
				print "		 Your Text is Gulf dialect with Probability equal {0:.2f}%.".format(gulf_result)
		                print "		 Your Text is Iraqi dialect with Probability equal {0:.2f}%.".format(iraqi_result)
				print "		 Your Text is Levant dialect with Probability equal {0:.2f}%.".format(levant_result)
				print "		 Your Text is Maghrebi dialect with Probability equal {0:.2f}%.".format(maghrebi_result)
				print "		 Your Text is ModernStandard dialect with Probability equal {0:.2f}%.".format(100-total_result)

                #####################################################################
                else:
		              print "Error, Please Enter number between 1 and 6."
		              continue
             
