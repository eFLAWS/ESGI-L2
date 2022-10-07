import time
import random

#exo suite de valeurs

def index(tab) :
    copy = []
    for i in range (len(tab)) :
        copy.append(tab[i])
    for i in range (len(tab)) :
        ind = False
        for j in range (len(copy)) :
            if tab[i] == copy[j] : ind = True
        if ind == False : return False
    return True

#correction
def index(tab) :
    for i in range (len(tab)) :
        ind = False
        for j in range (len(tab)) :
            if tab[j] == i : ind = True
        if ind == False : return False
    return True

#exo n-1 n+1

def follow(tab) :
    for i in range (len(tab)) :
        fol = False
        for j in range (len(tab)) :
            if tab[i] == tab[j] + 1 : fol = True
            if tab[i] == tab[j] - 1 : fol = True
        if fol == False : return False
    return True

#exo identiques

def uniform(tab) :
    for i in range (len(tab)) :
        uni = False
        for j in range (len(tab)) :
            if tab[i] == tab[j] : uni = True
        if uni == False : return False
    return False

#exo exact double

def searchDup(tab) :
    





    

    