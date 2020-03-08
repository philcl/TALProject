# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 10:51:37 2020

@author: chlob
"""
import sys

for index in range(len(sys.argv)):                      # On parcours la liste des arguments
        if index != 0:                          # On ingnore le nom du script fourni en paramètre 0

		fileName = "../data/" + sys.argv[index]
		fileTranslate = open("../data/POSTags_PTB_Universal_Linux.txt",'r')
		fileInit = open(fileName,'r')        # On rajoute un tilde à la fin pour éviter d'écraser le fichier source en cas de bug
		fileOut = open(fileName + ".univ",'w+')        # On rajoute un tilde à la fin pour éviter d'écraser le fichier source en cas de bug

		dico = {}
		lignesTranslate = fileTranslate.readlines()
		for ligne in lignesTranslate:
		    word = ligne.split(' ')
		    dico[word[0]] = word[1]		    

		lignes = fileInit.readlines()               # On parcours les lignes du fichier source
		ligneSortie = ""
		for ligne in lignes:
		    if(ligne == "\n"):
		        ligneSortie += '\n'
		    else:
		        toReplace = ligne.split('\t')
			print(toReplace)
		        size =  len(toReplace[1])
			print(toReplace[1])
			if toReplace[1] == "''":
				replace = toReplace[1]
			else:
		        	replace = dico[toReplace[1][:size-1]]
		        ligneSortie += toReplace[0] + '\t' + replace
		    
		fileOut.write(ligneSortie)               # On écrit la nouvelle ligne dans le nouveau fichier       
		fileTranslate.close()
		fileInit.close()                     # Fermeture du fichier source
		fileOut.close()                    # Fermeture du fichier écrit
