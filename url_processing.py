###### Run this on a 3.5 Python environment
import numpy
import pandas as pd
import json

def process_file (path , file):    #This function handles each file. It creates a Panda data frame of every row.
    allDataFrames = []
    with open(path+file) as f:
        for line in f:
            lineDataFrame = pd.DataFrame(json.loads(line) , index=[0])
            allDataFrames.append(lineDataFrame)
    result = pd.concat(allDataFrames)
    return result

#Example, working with the downloaded files using Pandas.
Afghanistan_File_0 = process_file('./results/' , 'domain-gov.af-0')
print (Afghanistan_File_0.dtypes)   #Shows the columns
print (Afghanistan_File_0.head(1))  #Shows the first row of the pandas dataframe
print (Afghanistan_File_0.url)      #Shows just the column of your interest e.g. url
