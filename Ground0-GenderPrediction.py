# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 17:12:34 2021

@author: rahikhan
"""

import nltk
import random

from nltk.corpus import names


print("names.fileids() : ", names.fileids())

import matplotlib
import matplotlib.pyplot as plt
matplotlib.style.use("ggplot")
#%matplotlib inline



# for fileid in names.fileids():
#     print(" fileid : ", fileid)
#     for name in names.words(fileid):
#         print(fileid ," : ", name)


name_cfd = nltk.ConditionalFreqDist((fileid,name[-2:]) for fileid in names.fileids() for name in names.words(fileid))
plt.figure(figsize = (50,10))
name_cfd.plot()

def name_features(name):
    return {"pair" : name[-2:]}

name_list = [(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')] 
#print("name_list : ", name_list)

for name in name_list:
    if name[0] == 'Rahil' or name[0] == 'Raine' or name[0] == 'Aamir':
        print("name : ", name)
        
random.shuffle(name_list)
features = [(name_features(name),gender) for (name,gender) in name_list]
#print("features : ", features)

half = len(features)/2
print("half : ", half)

training_set = features[:3972]
testing_set  = features[3972:]

classifier = nltk.NaiveBayesClassifier.train(training_set)
#male_names = names.words("male.txt")

print('Raina  : ', classifier.classify(name_features('Raina')))
print('Rahil  : ', classifier.classify(name_features('Rahil')))
print('Manha  : ', classifier.classify(name_features('Manha')))
print('Ayaana : ', classifier.classify(name_features('Ayaana')))
print('Saman : ', classifier.classify(name_features('Saman')))


print("\n testing_set accuracy : ", nltk.classify.accuracy(classifier, testing_set))
