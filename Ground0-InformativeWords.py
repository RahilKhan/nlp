# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 20:08:58 2021

@author: rahil khan
"""

import nltk
import re

store = nltk.corpus.gutenberg
print("store :", store)


print("\n\n\n")
alice = nltk.corpus.gutenberg.words("carroll-alice.txt")
alice_fd = nltk.FreqDist(alice)
alice_fd_100 = alice_fd.most_common(200)
print("alice_fd_100 : ", alice_fd_100)

print("\n\n\n")
moby = nltk.corpus.gutenberg.words("melville-moby_dick.txt")
moby_fd = nltk.FreqDist(moby)
moby_fd_100 = moby_fd.most_common(200)
print("moby_fd_100 : ", moby_fd_100)

print("\n\n\n")
paradise = nltk.corpus.gutenberg.words("milton-paradise.txt")
paradise_fd = nltk.FreqDist(paradise)
paradise_fd_100 = paradise_fd.most_common(200)
print("paradise_fd_100 : ", paradise_fd_100)


alice_100 = [word[0] for word in alice_fd_100]
print("\n\n alice_100 : ", alice_100)

moby_100 = [word[0] for word in moby_fd_100]
print("\n\n moby_100 : ", moby_100)

paradise_100 = [word[0] for word in paradise_fd_100]
print("\n\n paradise_100 : ", paradise_100)

infWords = set(alice_100) - set(moby_100)  - set(paradise_100)
print("\n\n infWords : ", infWords)


w_ful = set([word for word in alice if re.search("ful$",word)])
print("\n w_ful : ", w_ful)    

vowel_words = set([word for word in alice if re.search("^[aeiou]c.+y",word)])
print("\n vowel_words : ", vowel_words)    



#alice_sent = nltk.corpus.gutenberg.sentence("carroll-alice.txt")
#print("\n alice_sent : ", alice_sent)    












