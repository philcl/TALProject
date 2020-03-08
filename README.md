# TALProject
Liste des Commandes

Partie I
Q1
Translate : 
LIMA → PTB python script-translate-LIMA-to-PTB.py ../data/Data/pos_reference.txt.pos.lima
PTB → UNIV python script-translate-PTB-to-univ.py ../data/Data/pos_reference.txt.pos.lima.ptb

Q2
Extraction des phrases: python question2.py

Q3
LIMA: python faire_mot_etiquette.py ../data/Data/pos-test.txt.conllu
Stanford: python script-split-en-colonne.py ../data/Data/pos-test.txt.pos.stanford

NLTK: python nltk_pos_tagger.py

Q4 
LIMA : python script-translate-LIMA-to-PTB.py ../data/Data/pos_test.txt.pos.lima
python script-translate-PTB-to-univ.py ../data/Data/pos_test.txt.pos.lima.ptb
Stanford: python script-translate-PTB-to-univ.py ../data/Data/pos_test.txt.pos.stanford
NLTK: python script-translate-PTB-to-univ.py ../data/Data/pos_test.txt.pos.nltk

Partie II
Q1
Extraction des phrases: python extractCONLL.py
Q2
LIMA: python conllu_to_lima.py
Q3
LIMA: python lima_or_stanford_to_conll.py ../data/Data/ne_test.txt.ne.lima
Stanford: python lima_or_stanford_to_conll.py ../data/Data/ne_test.txt.ne.stanford
NLTK: python nltk_to_conll.py
