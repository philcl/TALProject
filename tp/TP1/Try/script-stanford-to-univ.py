# -*- coding: utf-8 -*-
import sys

if len(sys.argv) != 0:  # On ingnore le nom du script fourni en paramètre 0
    fileTranslate = open(sys.argv[1], 'r')
    fileStanford = open(sys.argv[2], 'r')  # On rajoute un tilde à la fin pour éviter d'écraser le fichier source en cas de bug
    fileOut = open(sys.argv[3], 'w')  # On rajoute un tilde à la fin pour éviter d'écraser le fichier source en cas de bug

    dict = {}
    lignesTranslate = fileTranslate.readlines()
    print("debut creation dictionnaire")
    for ligne in lignesTranslate:
        print(ligne)
        word = ligne.split(' ')
        print(word[0])
        dict[word[0]] = word[1]

    lignes = fileStanford.readlines()  # On parcours les lignes du fichier source
    print("debut remplacement")
    for ligne in lignes:
        words = ligne.split(' ')

        ligneSortie = ""
        cpt = 0
        for word in words:
            print(word)
            cpt += 1
            if cpt < len(words):
                toReplace = word.split('_')
                #print(toReplace[1])
                replace = dict[toReplace[1]]
                ligneSortie += toReplace[0] + '_' + replace + ' '

        print(ligneSortie)
        fileOut.write(ligneSortie)  # On écrit la nouvelle ligne dans le nouveau fichier

    fileTranslate.close()
    fileStanford.close()  # Fermeture du fichier source
    fileOut.close()  # Fermeture du fichier écrit
