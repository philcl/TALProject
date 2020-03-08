# -*- coding: utf-8 -*-
import sys
 
for index in range(len(sys.argv)):                      # On parcours la liste des arguments
        if index != 0:                          # On ingnore le nom du script fourni en paramètre 0
            print("index " + index)
            fileTranslate = open(sys.argv[index],'r')
            fileStanford = open(sys.argv[index],'r')        # On rajoute un tilde à la fin pour éviter d'écraser le fichier source en cas de bug
            fileOut = open(sys.argv[index],'w+')        # On rajoute un tilde à la fin pour éviter d'écraser le fichier source en cas de bug

            dict = {}
            lignesTranslate = fileTranslate.readline()
            for ligne in lignesTranslate:
                word = ligne.split('  ')
                dict[word[0]] = word[1]

            lignes = fileStanford.readlines()               # On parcours les lignes du fichier source
            for ligne in lignes:
                words = ligne.split(' ')
                ligneSortie = ""
                for word in words:
                    toReplace = word.split('_')
                    replace = dict[toReplace[1]]
                    ligneSortie += toReplace[0] + '_' + replace + ' '

                fileOut.write(ligneSortie)               # On écrit la nouvelle ligne dans le nouveau fichier
            
            fileTranslate.close()
            fileStanford.close()                     # Fermeture du fichier source
            fileOut.close()                    # Fermeture du fichier écrit