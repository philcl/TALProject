import sys

fileRead = open(sys.argv[1],'r')
fileOut = open(sys.argv[1] + ".split",'w')

lignes = fileRead.readlines()  # On parcours les lignes du fichier source
ligneSortie = ""
for line in lignes:
	if '(' in line:
		entity = line.split('(')
		if ' ' in entity[1]:
			entity = entity[1].split(' ')
			print(entity[1])
			word = entity[1].split('/')
			if entity[0] != "GPE":
				ligneSortie += word[0] + '\t' + entity[0] + '\n'
			else:
				ligneSortie += word[0] + '\t' + "O" + '\n'
	else:
		word = line.split(' ')
		word = word[2].split('/')
		ligneSortie += word[0] + '\t' + "O" + '\n'


fileOut.write(ligneSortie)
fileRead.close()
fileOut.close()
