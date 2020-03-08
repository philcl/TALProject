# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:51:37 2020

@author: chlob
"""

fileTranslate = open("POSTags_PTB_Universal_Linux.txt",'r')
fileInit = open("wsj_0010_sample.pos.ref",'r')        # On rajoute un tilde à la fin pour éviter d'écraser le fichier source en cas de bug
fileOut = open("wsj_0010_sample.pos.ref.univ",'w+')        # On rajoute un tilde à la fin pour éviter d'écraser le fichier source en cas de bug

dico = {}
lignesTranslate = fileTranslate.readlines()
for ligne in lignesTranslate:
    word = ligne.split(' ')
    print(ligne)
    dico[word[0]] = word[1]


    

lignes = fileInit.readlines()               # On parcours les lignes du fichier source
ligneSortie = ""
for ligne in lignes:
    toReplace = ligne.split('\t')
    size =  len(toReplace[1])
    replace = dico[toReplace[1][:size-1]]
    ligneSortie += toReplace[0] + '\t' + replace
    
fileOut.write(ligneSortie)               # On écrit la nouvelle ligne dans le nouveau fichier       
fileTranslate.close()
fileInit.close()                     # Fermeture du fichier source
fileOut.close()                    # Fermeture du fichier écrit
