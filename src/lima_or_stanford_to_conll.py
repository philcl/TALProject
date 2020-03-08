# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 12:20:23 2020

@author: chlob
"""

fileTranslate = open("../data/tags_conll.txt",'r')
fileInit = open("../data/Data/ne_test.txt.ne.stanford",'r')        # On rajoute un tilde à la fin pour éviter d'écraser le fichier source en cas de bug
fileOut = open("../data/Data/ne_test.txt.ne.stanford.conll",'w+')        # On rajoute un tilde à la fin pour éviter d'écraser le fichier source en cas de bug

dico = {}
lignesTranslate = fileTranslate.readlines()
for ligne in lignesTranslate:
    word = ligne.split(' ')
    dico[word[0]] = word[1]


lignes = fileInit.readlines()               # On parcours les lignes du fichier source
ligneSortie = ""
previousWord=""
for ligne in lignes:
    toReplace = ligne.split("\t")
    size =  len(toReplace[1])
    word=toReplace[1][:size-1]
    if word==previousWord and word!="O":
        word+="-I"
    
    replace = dico[word]
    ligneSortie += toReplace[0] + "\t" + replace 
    previousWord=toReplace[1][:size-1]

fileOut.write(ligneSortie)

fileTranslate.close()
fileInit.close()                     # Fermeture du fichier source
fileOut.close()                    # Fermeture du fichier écrit
