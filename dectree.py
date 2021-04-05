'''
Assume df is a pandas dataframe object of the dataset given
'''
import numpy as np
import pandas as pd
import random
eps = np.finfo(float).eps
from numpy import log2 as log
'''Calculate the entropy of the enitre dataset'''
	#input:pandas_dataframe
	#output:int/float/double/large

def get_entropy_of_dataset(df):
        Class = df.keys()[-1]
        entropy = 0
        values = df[Class].unique()
        for value in values:
                fraction = df[Class].value_counts()[value]/len(df[Class])
                entropy += -fraction*np.log2(fraction)
        return entropy



'''Return entropy of the attribute provided as parameter'''
	#input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
	#output:int/float/double/large
def get_entropy_of_attribute(df,attribute):
        Class = df.keys()[-1]
        target_variables = df[Class].unique()
        variables = df[attribute].unique()
        entropy_of_attribute = 0
	
        for variable in variables:
                entropy = 0
                for target_variable in target_variables:
                        num = len(df[attribute][df[attribute]==variable][df[Class] ==target_variable])
                        den = len(df[attribute][df[attribute]==variable])
                        fraction = num/(den+eps)
                        entropy += -fraction*log(fraction+eps)
                fraction2 = den/len(df)
                entropy_of_attribute += -fraction2*entropy
        return abs(entropy_of_attribute)



'''Return Information Gain of the attribute provided as parameter'''
	#input:pandas_dataframe,str
	#output:int/float/double/large
def get_information_gain(df,attribute):
	information_gain = 0
	information_gain = get_entropy_of_dataset(df)- get_entropy_of_attribute(df,attribute)
	return information_gain



''' Returns Attribute with highest info gain'''  
	#input: pandas_dataframe
	#output: ({dict},'str')     
def get_selected_attribute(df):
   
	information_gains={}
	selected_column=''
	for key in df.keys()[:-1]:
                information_gains[key]= get_information_gain(df,key)
    
    
	'''
	Return a tuple with the first element as a dictionary which has IG of all columns 
	and the second element as a string with the name of the column selected

	example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')'''
    #selected_column = 
	return (information_gains,max(information_gains, key= lambda x: information_gains[x]))



'''
------- TEST CASES --------
How to run sample test cases ?

Simply run the file DT_SampleTestCase.py
Follow convention and do not change any file / function names

'''
