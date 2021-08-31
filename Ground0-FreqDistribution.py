#!/usr/bin/env python
# coding: utf-8

import nltk
alice = nltk.corpus.gutenberg.words("carroll-alice.txt")
alice_fd = nltk.FreqDist(alice)
alice_fd

print("hatters : " , alice_fd["hatters"])

print("alice_fd.most_common(15) : ", alice_fd.most_common(15))
print("alice_fd.most_common(1) : ", alice_fd.most_common(1))

print("alice_fd.hapaxes() : ",alice_fd.hapaxes())

names = [("Group-A","Ross"),("Group-A","Ross"),("Group-A","Chandler"),("Group-A","Joey"),("Group-B","Monica"),("Group-B","Rachel"),("Group-B","Phoebe")]


print("\n-------------------------------")
print("names : ", names)
print("nltk.FreqDist(names) : ", nltk.FreqDist(names) )
print("nltk.ConditionalFreqDist(names) : ",nltk.ConditionalFreqDist(names))



