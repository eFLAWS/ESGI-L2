from operator import truediv
import time
import random
"""
#EXO 1
def somTab(tab) :
    y = 0
    for i in range (len(tab)) :
        y += tab[i]
    return y

print(somTab([2, 5, 7, 11])) 

#EXO 2
def  croissTab(tab) :
    for i in range (1, len(tab)) :
        if tab[i-1] > tab[i] : return False
    return True

print(croissTab ([2, 5, 7, 11]))
print(croissTab ([2, 7, 5, 11]))
"""
#EXO 3
def onlyDoub(tab) :
    for i in range (len(tab)) :
        x = False
        for j in range (len(tab)) :
            if i != j :
                if tab[i] == tab[j] :
                    x = True
                    break
        if x == False : return False
    return True
    
print(onlyDoub([2, 5, 2, 2, 5]))
print(onlyDoub([2, 5, 2, 2]))