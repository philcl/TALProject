# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:08:53 2020

@author: chlob
"""

import sys


fileName = sys.argv[1]
fileRead = open(fileName, "r")

text = ""
lignes = fileRead.readlines()
for ligne in lignes:
    
    test = ligne.split("\t")
    if(len(test)>1 and ligne[0]!="#"):
        text+=test[1]+"_"+test[3]
	if(test[1]=="."):
            text+="\n"
        else:
            text+=" "		

new_file = open(sys.argv[2], "w") 
new_file.write(text)
new_file.close()
fileRead.close()
        
    
    

