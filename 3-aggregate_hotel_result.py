import csv
import glob
import ntpath
import os
import re
from collections import Counter

outpath = r'E:\Hina\MS\IR\output\*.csv'
finalOutputFile =r'E:\Hina\MS\IR\final\finalOutput.csv'
text = open(finalOutputFile, "w")
outputFiles = glob.glob(outpath)
header = "Hotel,flablel,nflabel\n"
text.write(header)
for name in outputFiles:
    with open(name, 'r') as file:
        reviews = list(csv.reader(file))
    def get_text(reviews, score):
        reviewArr =[]
        for r in reviews:
            if r[3] == score:
                reviewArr.append(r[0])
        return  reviewArr


    fake_text = get_text(reviews, "fake")
    not_fake_text = get_text(reviews, "not fake")
    # Generate word counts for negative tone.
    fake_counts = len(fake_text)
    # Generate word counts for positive tone.
    not_fake_counts = len(not_fake_text)
    hotelName =os.path.splitext(ntpath.basename(name))[0]
    row = hotelName + "," + str(fake_counts) +"," + str(not_fake_counts) + "\n"
    text.write(row)
