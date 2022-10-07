from operator import truediv
import time
import random
import MAXINT

#exo uniformity
def tabUniform(tab) :
    valeurUniform = tab[0]
    for i in range (len(tab)) :
        if tab[i] != valeurUniform : return False
    return True

print(tabUniform ([7, 8, 10, 15]))
print(tabUniform ([8, 8, 8, 8])) 

#correction
def uniformTab(tab) :
    for i in range (len(tab)) :
           if tab[i] != tab[j] : return False
    return True

#exo duplicate
def duplicate(tab) :
    diff = False
    for i in range (1, len(tab)-1) :
        for j in range (i+1,len(tab)) :
            if i != j :
                if tab[i] == tab[j] :
                    if diff == False : diff  = Tru
                    else : return False
                    break
    if diff == True : return True
    return False

print(duplicate ([-7, -1, 7, 17, 25, 31]))
print(duplicate ([5, 5, 8, 9, 7, 5])) 
print(duplicate ([5, 9, 8, 8, 5, 7, 7])) 

#correction
def oneDup(tab) :
    c = 0
    for i in range (len(tab)) :
        for j in range (len(tab)) :
           if tab[i] == tab[j] : c += 1 and i != j :
                if c > 1 : return True

#exo close duplicate
def closeDup(tab) :
    x = 0
    y = MAXINT
    for i in range (len(tab)) :
        for j in range (i,len(tab)) :
            if i != j :
                if tab[i] == tab[j] :
                    if j < y : 
                        x = tab[j]
                        y = j
                    break
    if y == MAXINT : return False

print(closeDup ([4, 6, 7, 1, 10, 4, 7, 2, 4, 3]))
print(closeDup ([3, 4, 5, 1, 9, 6]))

#correction
def pprochDup(tab) :
    min = len(tab)
    for i in range (len(tab)) :
        for j in range (i+1,len(tab)) :
            if tab[i] == tab[j] and j-i < min : 
                    min = j-i
        if min == len(tab) : return 0
    return min


#exo smallest duplciate
def smallDup(tab) :
    x = 0
    y = MAXINT
    for i in range (len(tab)) :
        for j in range (i,len(tab)) :
            if i != j :
                if tab[i] == tab[j] :
                    if j < y : 
                        x = tab[j]
                        y = j
                    break
    if y == MAXINT : return -1
    return x

print(smallDup ([2, 3, 4, 13, 9, 2, 13, 17, 21]))
print(smallDup ([3, 4, 5, 1, 9, 6]))

#correction
def ppetitDub(tab) :
    min = -1
    for i in range (len(tab)) :
        for j in range (i+1,len(tab)) :
            if tab[i] == tab[j] and i != j and tab[i] < min: 
                    return True
        return min

#exo first duplicate
def firstDup(tab) :
    y = MAXINT
    for i in range (len(tab)) :
        for j in range (i,len(tab)) :
            if i != j :
                if tab[i] == tab[j] :
                    if j < y : 
                        y = j
                    break

print(firstDup ([3, 6, 2, 7, 2, 3, 3, 6, 1]))
print(firstDup ([3, 4, 5, 1, 9, 6]))

#correction
def premsDup(tab) :
    min = len(tab)
    for i in range (len(tab)) :
        for j in range (i+1,len(tab)) :
            if tab[i] == tab[j] :
                    if j < min:
                        y = min
    if min==len(tab) : return -1
    return tab[min]