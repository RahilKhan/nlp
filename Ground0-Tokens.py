# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 20:44:03 2021

@author: rahil khan
"""

import nltk
from nltk.util import ngrams

text = "It might rain today or drizzle tomorrow!!! Eitherway it's going to be a good day."
tokens = nltk.word_tokenize(text)
print("\n len-tokens", len(tokens),"\n tokens : ", tokens)

tokens_sent = nltk.sent_tokenize(text)
print("\n len-tokens", len(tokens_sent),"\n tokens : ", tokens_sent)

print("\n\n")
bigrams = nltk.bigrams(tokens)
for item in bigrams:
    print("item : ", item)


trigrams = nltk.trigrams(tokens)
for item in trigrams:
    print("item : ", item)
    
print("\n")    
ngrams2 = ngrams(tokens,2)
for item in ngrams2:
    print("ngrams2-item : ", item)

print("\n")    
ngrams5 = ngrams(tokens,5)
for item in ngrams5:
    print("ngrams5-item : ", item)    
    
def n_grams(text, ngms):
    tokens = nltk.word_tokenize(text)
    ngrams_x = ngrams(tokens, ngms)
    print("\n")
    for item in ngrams_x:
        print('ngrams_',ngms,'-item : ', item)    
        

n_grams(text,7)


alice_sent = nltk.corpus.gutenberg.sentence("carroll-alice.txt")
#print("\n alice_sent : ", alice_sent)   

