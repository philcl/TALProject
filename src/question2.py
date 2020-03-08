# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 14:36:48 2020

@author: chlob
"""

import sys

#for index in range(len(sys.argv)):
#    if index!=0:
#        filename=


file = open(sys.argv[1],'r')  

#file = open("pos_reference.txt.lima", "r")

text = ""
for ligne in file:
    if len(ligne)==1:
        text=text[:len(text)-1]
        text+=" \n"
    else:
        word = ligne.split("\t")
        text+=word[0]+" "

#text = "learn php from guru99"

new_file = open("../data/ne_test.txt", "w") # Argh j'ai tout écrasé !
new_file.write(text)
new_file.close()
