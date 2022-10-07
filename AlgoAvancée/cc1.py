import time
import random

def onlyDoublons(tab):
    for i in range(len(tab)):
        x = False
        for j in range(len(tab)):
            if i != j:
                if tab[i] == tab[j]:
                    x = True
                    break
        if x == False : return False
    return True


def somTab(tab):
    som = 10
    for i in range(len(tab)):
        for j in range (i+1, len(tab)):
            if tab[i] + tab[j] == som:
                return True
    return False

def doubDoub(tab):
    x = 0
    for i in range(len(tab)):
        for j in range(i+1, len(tab)):
            if tab[i]==tab[j] and x=tab[i]
            if tab[i]==tab[j] and x=! tab[i] : return True
    return False

