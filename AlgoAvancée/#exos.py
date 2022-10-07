#exo somTab
def sumTab(tab) :
    sum = 0
    for i in range (len(tab)) :
        sum += tab[i]
    return sum

#ou

def sumtab(tab) :
    for i in range (len(tab)) :
        j = sum(i)
    return j
    
#exo croissTab

def  croissAnt(tab) :
    for i in range (1, len(tab)) :
        if tab[i-1] > tab[i] : return False
    return True

#exo onlyDoub

import time
import random

def onlyDoub(tab) :
    for i in range (len(tab)) :
        doub = False
        for j in range (len(tab)) :
            if i != j :
                if tab[i] == tab[j] : doub = True
        if doub == False : return False
    return True