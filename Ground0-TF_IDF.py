# -*- coding: utf-8 -*- .
"""
Created on Mon Aug 30 13:50:09 2021

@author: rahikhan
"""

import nltk
from nltk.corpus import inaugural
import math

dataset = {}

"""
for speech in inaugural.fileids():
    print(speech)
    dataset[speech] = inaugural.words(speech)
"""

dataset["tfidf_1.txt"] = open(r"resources\tfidf\tfidf_1.txt", encoding="utf8").read()
dataset["tfidf_2.txt"] = open(r"resources\tfidf\tfidf_1.txt", encoding="utf8").read()
dataset["tfidf_3.txt"] = open(r"resources\tfidf\tfidf_3.txt").read()
dataset["tfidf_4.txt"] = open(r"resources\tfidf\tfidf_4.txt").read()
dataset["tfidf_5.txt"] = open(r"resources\tfidf\tfidf_5.txt").read()
dataset["tfidf_6.txt"] = open(r"resources\tfidf\tfidf_6.txt").read()
dataset["tfidf_7.txt"] = open(r"resources\tfidf\tfidf_7.txt").read()
dataset["tfidf_8.txt"] = open(r"resources\tfidf\tfidf_8.txt").read()
dataset["tfidf_9.txt"] = open(r"resources\tfidf\tfidf_9.txt").read()
dataset["tfidf_10.txt"] = open(r"resources\tfidf\tfidf_10.txt").read()

# print("dataset : ", len(dataset) )
# print("dataset[2009-Obama.txt] : ", dataset['2009-Obama.txt'])


def tf(dataset, filename):
    text = dataset[filename]
    tokens = nltk.word_tokenize(text)
    fd = nltk.FreqDist(tokens)
    return fd


def idf(dataset, term):
    count = [term in dataset[file_name] for file_name in dataset]
    # print("count : ", count)
    # print("term - {0} : len(count) - {1}".format(term, len(count)))
    # print("sum(count) : ", sum(count))
    """
    if count == 0 or sum(count) ==0 or len(count):
        return 0
    """
    inv_df = math.log(len(count)/sum(count))
    return inv_df


war_idf = idf(dataset, "war")
print("war_idf : ", war_idf)

# android_idf = idf(dataset, "android")
# print("android_idf : ", android_idf)


def tfidf(dataset, file_name, count):
    term_scores = {}
    file_fd = tf(dataset, file_name)
    for term in file_fd:
        if term.isalpha():
            idf_val = idf(dataset, term)
            tf_val = tf(dataset, file_name)[term]
            tfidf_val = idf_val*tf_val
            term_scores[term] = round(tfidf_val, 2)
    return sorted(term_scores.items(), key=lambda x: -x[1])[:count]

# print("tfidf(dataset,'tfidf_1.txt',5) : ", tfidf(dataset,'tfidf_1.txt',3))


for filename in dataset:
    print("filename : ", filename)
    print("{0}: \n {1} \n ".format(filename, tfidf(dataset, filename, 10)))

