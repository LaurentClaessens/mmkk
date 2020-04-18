#! /usr/bin/python3
# -*- coding: utf8 -*-

import sys, os

HOME = os.path.expanduser("~")
NOM_LISTE = "~/.kk.lst"

rep_cour = os.getcwd()
rep_cour_mod = rep_cour.replace(HOME,"~")

marque = sys.argv[1]

ligne = marque+"@"+rep_cour_mod+"\n"
#print ligne

filename=NOM_LISTE.replace("~",HOME)
with open(filename,'a') as f:
    f.write(ligne)

# Création du raccourcis dans konqueror
texte=open(HOME+'/script/bureau/generic.desktop',"r").read()
nouveau=texte.replace("KKK",marque).replace("RRR",rep_cour)

filename=".local/share/kservices5/searchproviders/"+marque+".desktop"
filepath=os.path.join(HOME,filename)

with open(filepath,'w') as f:
    f.write(nouveau)
