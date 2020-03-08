# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 13:51:16 2020

@author: chlob
"""
""" Ce script sert à créer le fichier ne_test.txt.ne.lima cad le mot associé à son EN"""
file = open("../data/Data/ne_test.txt.conllu", "r")

text = ""
lignes = file.readlines()
cpt=0
for ligne in lignes:
    if(len(ligne.split("\t"))>1 and ligne[0]!="#"):
       ligne = ligne.split("\t")
       column = ligne[9]
       word = ligne[1]
       if "NE" in column:
           NE = column[3:].split("|")[0].split(".")[1]
           text+=word+"\t"+NE+"\n"
       else: 
           text+=word+"\t"+"O\n"
          

new_file = open("../data/Data/ne_test.txt.ne.lima", "w") 
new_file.write(text)
new_file.close()
        
