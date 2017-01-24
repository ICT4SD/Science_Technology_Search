# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 16:57:37 2017

@author: Yi Luo
"""
import pandas as pd
import json
import glob

def process_file (file_path):    #This function handles each file. It creates a Panda data frame of every row.
    allDataFrames = []
    with open(file_path) as f:
        for line in f:
            lineDataFrame = pd.DataFrame(json.loads(line) , index=[0])
            allDataFrames.append(lineDataFrame)
    result = pd.concat(allDataFrames)
    return result

#read all the URL-FETCH files at one time
files_names = glob.glob('C:/Users/tradingroom/result3/prefix-https%3A--www.ted.com-*')

#create Panda dataframe for each file
for name in files_names:
    name_pd = name+"_pdFile"
    name_pd = process_file(name)
    name_pd_output = name +'.txt'
   
    with open(name_pd_output,'a') as f2:
        f2.write(str(name_pd.url))
    f2.close()
    

