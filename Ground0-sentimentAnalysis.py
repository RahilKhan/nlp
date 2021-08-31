# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:51:20 2021

@author: rahikhan
"""

import nltk
import csv
import numpy as np


negWords = []
with open("resources\words_negative.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        negWords.append(row)

print("negWords - 10 : ", negWords[:10])

posWords = []
with open("resources/words_positive.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        posWords.append(row)

print("posWords - 10 : ", posWords[:10])


def sentiments(text):
    #print("text : ", text)
    temp = []
    text_sent = nltk.sent_tokenize(text)
    #print("text_sent : ", text_sent)
    
    for sentence in text_sent:
        p_count, n_count = 0, 0
        sent_words = nltk.word_tokenize(sentence)
        #print("sent_words : ", sent_words)
    
        for word in sent_words:
            for item in posWords:
                if(word == item[0]):
                    p_count += 1
            for item in negWords:
                if(word == item[0]):
                    n_count += 1

    if(p_count > 0 and n_count == 0):
        print(" + : ", sentence)
        temp.append(1)
    elif(n_count%2 > 0 ):
        print(" - : ", sentence)
        temp.append(-1)
    elif(n_count%2 == 0 and n_count > 0):
        print(" + : ", sentence)
        temp.append(1)
    else:
        print(" ?  : ", sentence )
        temp.append(0)
        
    return temp

sentiments("This was a terrible idea")        
sentiments("Idea was not bad")        
sentiments("It was a terribly good")  
sentiments("This is about something")  


comments = []
with open("resources/reviews.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        comments.append(row)

print("comments : ", comments)

for review in comments:
    print("\n")
    print("average sentiments ", np.average(sentiments(str(review))))
    print("review : ", review)
      
        
        