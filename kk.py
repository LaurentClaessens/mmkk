#! /usr/bin/python3

import sys,os
import string
import codecs

HOME = os.path.expanduser("~")
NOM_LISTE = "~/.kk.lst"
NOM_COMMANDES = "~/.kk.liste"
WORKING_DIR=os.getcwd()

#print(WORKING_DIR)

ex_stdout=sys.stdout
sys.stdout=codecs.open(".kk.log","w",encoding="utf8")

associations = {}
f = open(NOM_LISTE.replace("~",HOME),"r")
for ligne in f.readlines():
    posAt=ligne.rfind("@")
    marque = ligne[0:posAt]
    #print(marque)
    rep = ligne[posAt+1:-1]
    associations[marque] = rep
f.close()

texte = sys.argv[1]
try :
        texte=unicode(texte,"utf8")
except:
        pass
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

print(aprinter)

###################################### Ancien en bash, qu'il fallait sourcer #################""

#source ~/.chemins.lst

#
#  Lire les lignes du fichier FICH_LIST et en tirer des marques et les noms de répertoires correspondantes
#

 
#while read ligne
#do 
#   rep=${ligne##*@}    
#   mark=${ligne%%@*}
#   if [[ $1 = "-l" ]]; then echo $mark "-->"   $rep; fi
#   if [[ $mark = $1 ]]; then
#      cd $rep                          # Pour que cette ligne-ci soit opérante, il faut sourcer le script au lieu de l'exécuter.
                                        # en pratique, il faut taper $ source kk et non $ kk. Pragmatiquement un alias
                                        # dans le .bashrc fait l'affaire.
#   fi
#done < $FICH_LIST                      # Le secret pour boucler le read dans le fichier donné, c'est ce < "kk.lst"


# La syntaxe de la condition sur le if vient de 
# http://www.tldp.org/LDP/abs/html/testconstructs.html#DBLBRACKETS
# Les manipulations obscures de chaines de caractères proviennent de la page
# http://abs.traduc.org/abs-3.7-fr/string-manipulation.html
