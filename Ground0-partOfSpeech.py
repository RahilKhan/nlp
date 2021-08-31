# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 22:21:37 2021

@author: rahil khan
"""

import nltk

text = "I walked to cafe to buy coffee before work"
tokens = nltk.word_tokenize(text)
print("nltk.pos_Tag(tokens) :: ", nltk.pos_tag(tokens))
#md = nltk.corpus.gutenberg.

nltk.help.upenn_tagset()


def posTag(text):
    token = nltk.word_tokenize(text)
    pos_tag = nltk.pos_tag(token)
    print("pos_tag : ", pos_tag )

desert = "I will have desert."
posTag(desert)

desert2 =  "They will desert us."
posTag(desert2)
    
desert3 = "The are ought to deserting us"
posTag(desert3)

md = nltk.corpus.gutenberg.words("melville-moby_dick.txt")
md_norm = [word.lower() for word in md if word.isalpha()]
md_tags = nltk.pos_tag(md_norm, tagset = "universal")
print("\n md_tags : ", md_tags[:15])

md_nouns = [word[0] for word in md_tags if word[1] == "NOUN"]
print("md_nouns : ", md_nouns[:10])

md_nouns_fd = nltk.FreqDist(md_nouns)
print("md_nouns - most_comman : ", md_nouns_fd.most_common(10))

md_noun_cfd = nltk.ConditionalFreqDist(md_tags)
print("md_noun_cfd : ", md_noun_cfd)

md_noun_cfd

print('md_noun_cfd["over"] : ', md_noun_cfd["over"])
print('md_noun_cfd["spoke"] : ', md_noun_cfd["spoke"])
print('md_noun_cfd["answer"] : ', md_noun_cfd["answer"])

















