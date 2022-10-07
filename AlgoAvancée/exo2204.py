from operator import truediv
import time
import random
"""
def variationsTab(tab) :
    result = -1
    for i in range(len(tab)-1) :
        if result == -1 :
            if (tab[i] < tab[i+1]) : result = 0
            elif (tab[i] > tab[i+1]): result = 1
            elif (tab[i] == tab[i+1]): result = 2
        else :
            if (tab[i] <= tab[i+1]) and (result == 0) : continue
            elif (tab[i] >= tab[i+1]) and (result == 1) : continue
            elif (tab[i] == tab[i+1]) and (result == 2) : continue
            else : result = 3
    if result == 0 : print('Tri croissant')
    elif result == 1 : print('Tri décroissant')
    elif result == 2 : print('Tableau identique')
    else : print('Tableau non trié')

variationsTab([1,2,3,4])
variationsTab([1,2,3,3,4])
variationsTab([4,3,2,1])
variationsTab([4,3,2,2,1])
variationsTab([1,1,1,1])
variationsTab([2,7,4,5,3,8])
"""

def doubDoublons(tab) :
    x = False
    y = 0
    for i in range(len(tab)-1) :
        for j in range(i+1,len(tab)) :
            if tab[i] == tab[j] :
                if x == False and y == 1 : x = True
                else : y = 1
                break
    if x == True : return x
    return False

print(doubDoublons([2, 4, 2, 6, 4, 7, 4]))
print(doubDoublons([2, 4, 12, 6, 4, 7, 4]))