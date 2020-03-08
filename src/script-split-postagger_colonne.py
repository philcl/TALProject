# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:36:48 2020

@author: philc
"""

import sys
import os

fileName = sys.argv[1]
fileRead = open(fileName,'r')
new_file = open(fileName + ".split", "w") # Argh j'ai tout écrasé !

#file = open("pos_reference.txt.lima", "r")

lignes = fileRead.readlines()  # On parcours les lignes du fichier source
for ligne in lignes:
	words = ligne.split(' ')

	ligneSortie = ""
	cpt = 0
	txt = ""
	for word in words:
		txt += word

		if '_' in word:
			
			cpt += 1
			if cpt < len(words):
				toReplace = txt.split('_')
				ligneSortie += toReplace[0] + '\t' + toReplace[1] + '\n'
			else:
				ligneSortie += ".\t.\n\n"
			txt = ""
		else:
			txt += ' '
		
	new_file.write(ligneSortie)

new_file.close()
fileRead.close()

'''
fileRead = open(fileName + ".split", "r")
new_file = open(fileName, 'w')

lignes = fileRead.readlines()
ligneSortie = ""
for ligne in lignes:
	ligneSortie += ligne

new_file.write(ligneSortie)

new_file.close()
fileRead.close()

os.remove(fileName + ".split")
'''

