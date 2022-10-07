import time
import random
"""
#EXO 1
for x in range (1,11) :
    print(x)

y = int(input('entrez un nombre: '))
a = 1
for z in range (1,y+1) :
    if z%2 == 0 : a += z
print(a)
"""
#EXO 2
def rechDoublons(tab) :
    for i in range (len(tab)) :
        for j in range (i+1,len(tab)) :
            if tab[i] == tab[j] : return True
    return False

def rechDoublonsVoisins(tab) :
    for i in range(1,len(tab)) :
        if tab[i-1] == tab[i] : return True
    return False
"""
tab = [2,3,4,2]
print(rechDoublons(tab))
print(rechDoublonsVoisins(tab))
tab = [2,3,4]
print(rechDoublons(tab))
tab = [3,2,2,4]
print(rechDoublonsVoisins(tab))
"""
#EXO 3
for taille in [100,1000,10000,30000] :

    tab = []
    for i in range(taille) :
        tab.append(i)

    start = time.time()
    x = rechDoublons(tab)
    end = time.time()
    print('Pour rechDoublon d une taille ', taille,', resultat = ', x, 'en ', end-start, 'sec')

    start = time.time()
    x = rechDoublonsVoisins(tab)
    end = time.time()
    print('Pour rechDoublonVoisin d une taille ', taille,', resultat = ', x, 'en ', end-start, 'sec')