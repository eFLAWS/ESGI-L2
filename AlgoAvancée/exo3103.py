import time
import random
from xmlrpc.client import FastMarshaller
#EXO 1
def index(tab) :
    for i in range (len(tab)) :
        x = False
        for j in range (len(tab)) :
            if tab[j] == i : x = True
        if x == False : return False
    return True

print (index([2,1,0,3]))
print (index([2,1,0,15]))
#EXO 2
def toto(tab) :
    for i in range (len(tab)) :
        x = False
        for j in range (len(tab)) :
            if (tab[j] == tab[i]+1) | (tab[j] == tab[i]-1) : x = True
        if x == False : return False
    return True

print (toto([1,2,5,4,6]))
print (toto([1,2,3,5]))