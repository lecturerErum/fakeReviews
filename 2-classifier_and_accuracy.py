# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from sklearn.model_selection import train_test_split

dataset_url = 'PATH/hotel_100507.csv'
data = pd.read_csv(dataset_url)
data.head()
print(data)

y = data.label
X = data.content
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3)
print(X.head())
print(y.head())

print ("\nX_train:\n")
print(X_train.head())
print (X_train.shape)

print ("\nY_train:\n")
print(y_train.head())
print(y_train.shape)

print ("\nX_test:\n")
print(X_test.head())
print (X_test.shape)

print ("\nY_test:\n")
print(y_test.head())
print (y_test.shape)


from sklearn.feature_extraction.text import CountVectorizer
count_vect = CountVectorizer()

X_train_counts = count_vect.fit_transform(X_train)
X_train_counts.shape

from sklearn.feature_extraction.text import TfidfTransformer
tfidf_transformer = TfidfTransformer()

X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
X_train_tfidf.shape

print(X_train_tfidf)


from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, y_train)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(X_train, y_train)
labels = model.predict(X_test)


# calculate accuracy
from sklearn import metrics
print("Accuracy")
print(metrics.accuracy_score(y_test, labels))


