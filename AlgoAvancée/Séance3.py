import truediv
import time
import random

"""
Ecriture de code
Exercice 1 Test de variation

Ecrire une fonction variationsTab qui prend en entrée un tableau d’entiers, qui ne renvoie rien et qui affiche :

le tableau est croissant (sur [2, 5, 7, 11] ou [2, 7, 7, 11] )
le tableau est décroissant
le tableau est constant
le tableau est non trié
"""
def variationsTab(tab) :
    x = 0
    y = 0
    for i in range (len(tab)-1) :
        if tab[i] < tab[i+1] : x += 1
        if tab[i] > tab[i+1] : y += 1
    if x == 0 and y == 0 : print("le tableau est constant")
    elif x == 0 and y == 1 : print("le tableau est décroissant")
    elif x == 1 and y == 0 : print("le tableau est croissant")
    else : print("le tableau est non trié")

"""
Exercice 2 

Recherche de 2 doublons au moins On cherche à écrire une fonction doubDoub qui permet de déterminer
    si le tableau en paramètre contient au moins 2 doublons, c'est-à-dire 2 valeurs qui se répètent chacune au moins 2 fois.

Par exemple,

sur le tableau tab=[2, 4, 2, 6, 4, 7, 4] la fonction doit renvoyer true et 

sur le tableau tab = [2, 4, 12, 6, 4, 7, 4] la fonction doit renvoyer false
"""
def doubleDup(tab) :
    valDup  = None
    for i in range (len(tab)) :
        for j in range (i+1,len(tab)) :
            if tab[i] == tab[j] :
                if valDup == None : valDup = tab[i]
                else : return True


""
"""
Exercice 3

Valeur la plus fréquente On cherche à écrire une fonction mostFreq qui permet de déterminer l'élément le plus fréquent dans un tableau. En cas d'égalité, 
    renvoyer l'élément qui apparait en premier dans le tableau (le plus à gauche) sur le tableau tab=[2, 4, 2, 6, 4, 7, 4] 
        la fonction doit renvoyer 4 (qui apparait 3 fois) sur le tableau tab=[2, 4, 2, 2, 4, 7, 4] la fonction doit renvoyer 2 (qui apparait aussi 3 fois mais qui est plus à
"""

