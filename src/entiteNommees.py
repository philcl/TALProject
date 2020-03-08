# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 21:02:52 2020

@author: chlob
"""
from lxml import etree
from collections import Counter
import sys

FileOut = open(sys.argv[2], 'w')

#df = pd.DataFrame(columns=[c1, c2, c3, c4])

tree = etree.parse(sys.argv[1])
#for user in tree.xpath("/specific_entities/specific_entity/string"):
#print(user.text)

ligneSortie = ""
    
for p in tree.xpath("/specific_entities/specific_entity"):
    #s = p.find('string').text
	s=p.find('type').text
	pos=s.find('.')+1
    
	ligneSortie += (p.find('string').text) + "\t" + s[pos:] + '\n'


FileOut.write(ligneSortie)
