# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:32:45 2021

@author: rahikhan
"""

import nltk

ww2Text = open("example.txt").read()

ww2Text_tag = nltk.pos_tag(nltk.word_tokenize(ww2Text))

ww2Text_ch = nltk.ne_chunk(ww2Text_tag)

for chunk in ww2Text_ch:
    if hasattr(chunk, 'label'):
        print(chunk.label(), " : ".join(c[0] for c in chunk.leaves()))
        