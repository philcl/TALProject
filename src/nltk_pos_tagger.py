# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 09:24:27 2020

@author: chlob
"""

from nltk import pos_tag
from nltk.tokenize import word_tokenize
import sys

with open(sys.argv[1]) as f:
    text = f.read()

word_tokenize(text)  


print("After Split:",text)
tokens_tag = pos_tag(word_tokenize(text))

mon_fichier = open(sys.argv[1] + ".ne.nltk", "w") # Argh j'ai tout écrasé !
#stringTest = str(tokens_tag).split(')')

for s in tokens_tag:
    test=str(s)
    posFin1 = test.find(', ')-1
    posDeb2 = posFin1+4
    mot1 = test[2:posFin1]
    mot2 = test[posDeb2:test.find(')\n')-1]
    mon_fichier.write( mot1 + "\t" + mot2 + "\n")
    

#mon_fichier.write()
mon_fichier.close()
