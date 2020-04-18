#! /usr/bin/python3

import sys
import os
from pathlib import Path
import string
import codecs

HOME="lolo"
MAIN_DIR = Path(sys.argv[1]).resolve()
LIST_FILE = MAIN_DIR / ".kk.lst"

ex_stdout=sys.stdout
sys.stdout=codecs.open(".kk.log","w",encoding="utf8")

associations = {}
f = open(LIST_FILE, "r")
for ligne in f.readlines():
    posAt=ligne.rfind("@")
    marque = ligne[0:posAt]
    rep = ligne[posAt+1:-1]
    associations[marque] = rep
f.close()

texte = sys.argv[2]
jusque = texte
supplement = u""
if "/" in texte :
    jusque = texte[:texte.find("/")]
    supplement = texte.replace(jusque+"/","")

print("supplement",type(supplement))
print(supplement)
print("associations",type(associations[jusque]))
print(associations[jusque])
aprinter=associations[jusque].replace("~",HOME)+"/"+supplement
print("aprinter",type(aprinter))
print(aprinter)
sys.stdout=ex_stdout

# This print is the only one in stdout
print(aprinter)
