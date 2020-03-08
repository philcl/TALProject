# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:45:08 2020

@author: chlob
"""

from nltk import pos_tag, ne_chunk
from nltk.chunk import tree2conlltags
from nltk.tokenize import word_tokenize
import sys

with open(sys.argv[1]) as f:
    text = f.read()


tokens_tag = pos_tag(word_tokenize(text))
namedEnt = ne_chunk(tokens_tag)
iob_tagged= tree2conlltags(namedEnt)
#print("After Token:",tokens_tag)

mon_fichier = open(sys.argv[1] + ".ne.nltk.conll", "w") # Argh j'ai tout écrasé !
#stringTest = str(tokens_tag).split(')')
mon_fichier.write(str(iob_tagged))

#for s in tokens_tag:
#    test=str(s)
#    posFin1 = test.find(', ')-1
#    posDeb2 = posFin1+4
#    mot1 = test[2:posFin1]
#    mot2 = test[posDeb2:test.find(')')-1]
#    print(mot2)
#    mon_fichier.write( mot1 + "\t" + mot2 + "\n")
#    

#mon_fichier.write()
mon_fichier.close()
