# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 12:12:21 2020

@author: chlob
"""
"""Ce script sert à formater correctement le fichier ne_test.txt.ne.nltk.conll afin d'obtenir: mot tabulation EN"""
with open('../data/Data/ne_test.txt.ne.nltk.conll', 'r') as file:
    text = file.readlines()
    


for ligne in text:
    words = ligne.split(' ')

cpt = 0
finalText = ""

while cpt < len(words)-2:
    word = words[cpt]
    
    conllValue = words[cpt+2]
    
    wordPos1 = word.find('(\'')+2
    wordPos2 = word.find('\',')

    
    if word.find('\',\',')==1:
        word=","
    elif word.find('"\'s"')==1:
        word="'s"
    else:
        word = word[wordPos1:wordPos2]
    
    conllValuePos1 = conllValue.find('\'')+1
    conllValuePos2 = conllValue.find('\')')
    conllValue = conllValue[conllValuePos1:conllValuePos2]
    
    finalText+=word+"\t"+conllValue+"\n"
    cpt += 3

finalFile = open("../data/Data/ne_test_split.txt.ne.nltk.conll", "w") 
finalFile.write(finalText)
    
