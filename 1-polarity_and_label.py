import glob
import errno
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
import os
import random
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import numpy as np
from os import listdir
from os.path import isfile, join
import ntpath
import csv
import re
from collections import Counter

path = r'E:\Hina\MS\IR\sample\*.txt' #note C:
corpus = []
i=0
files = glob.glob(path)
outpath = r'E:\Hina\MS\IR\output'
for name in files:
    with open(name,encoding='ascii',errors='ignore') as f:
        folderName = outpath + '/' + os.path.splitext(ntpath.basename(name))[0]
        csv = open(folderName+'.csv', "w")
        columnTitleRow = "content,rating,polarity,label\n"
        csv.write(columnTitleRow)
        for line in f:
            if "<Content>" in line:
                content = line.split("<Content>")[1]
                content=content.replace(',','').replace("\n", "")
            if "<Overall>" in line:
                rating = line.split("<Overall>")[1].replace("\n", "")
                sid = SentimentIntensityAnalyzer()
                ss = sid.polarity_scores(content)
                for k in ss:
                    #print('{0}: {1}, '.format(k, ss[k]))
                    if (ss['neg'] < ss['pos'] and  ss['pos'] > 0.1 ):
                        polarity = 1
                    else:
                        polarity = 0
                    #print(polarity)
                fileContent =[]
                if(rating <= '3.5' and polarity == 0):
                    result = "not fake";
                elif (rating <= '3.5' and polarity == 1):
                    result  = "fake"
                elif(rating > '3.5' and polarity == 1):
                    result = "not fake"
                elif(rating > '3.5' and polarity == 0):
                    result = "fake"

                #fileContent.append(content)
                #fileContent.append(rating)
                #fileContent.append(polarity)
                #fileContent.append(result)


                #for item in fileContent:
                 #   s.write("%s\n" % item)
                #s.close()
                row = content + "," + rating +"," + str(polarity) +"," + str(result) + "\n"
                csv.write(row)
                i+=1




