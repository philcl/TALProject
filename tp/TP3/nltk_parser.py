# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:37:07 2020

@author: chlob
"""

import nltk
import sys

with open(sys.argv[1]) as f:
    text = f.read()

fileOut = open("wsj_0010_sample.txt.chk.nltk",'w+')

#text = "learn php from guru99"
tokens = nltk.word_tokenize(text)
print(tokens)
tag = nltk.pos_tag(tokens)
print(tag)
grammar = "Compound: {<DT>?<JJ>*<NN>}"
cp  =nltk.RegexpParser(grammar)
result = cp.parse(tag)
print(result)
result.draw()
fileOut.write(str(result))
fileOut.close()
