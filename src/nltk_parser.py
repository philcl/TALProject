# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:37:07 2020

@author: chlob
"""

import nltk
import sys

with open(sys.argv[1]) as f:
    text = f.read()

fileOut = open(sys.argv[1] + ".nltk",'w+')

#text = "learn php from guru99"
tokens = nltk.word_tokenize(text)
tag = nltk.pos_tag(tokens)
grammar = "Compound: {<DT>?<JJ>*<NN>}"
cp  =nltk.RegexpParser(grammar)
result = cp.parse(tag)
result.draw()
fileOut.write(str(result))
fileOut.close()
