#!/usr/bin/env python
# coding: utf-8

import nltk
from nltk.corpus import inaugural


inaugural.fileids()


for speech in inaugural.fileids():
    words_total = len(inaugural.words(speech))
    print (words_total, speech)


import pandas as pd
data = pd.DataFrame([int(speech[:4]),speech, len(inaugural.words(speech))/len(inaugural.sents(speech))] 
                   for speech in inaugural.fileids())


data.columns = ["Year","speech","WPS"]
data


import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
data.plot("speech", figsize=(20,5))
data.plot("Year", figsize=(20,5))





