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
def onlyDoub(tab) :
    doud = []
    doud.append(tab[0])

    for i in range (len(tab)) :
        for j in range (len(tab)) :
            if (tab[i] != doud[j]) & (j == (len(doud)-1)) : doud.append(tab[i])
            else : break

    time = [0]*len(doud)

    for i in range (len(tab)) :
        for j in range (len(doud)) :
            if tab[i] == doud[j] : time[j] += 1
            
    for i in range (len(time)) :
        if time[i] < 2 : return False

    return True
    


print(onlyDoub([2, 5, 2, 2, 5]))
print(onlyDoub([2, 5, 2, 2]))


