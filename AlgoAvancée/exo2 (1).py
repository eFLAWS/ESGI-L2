import time
import random
from xmlrpc.client import MAXINT

#EXO 1
def uniformTab(tab) :
    for i in range (0, len(tab)-1) :
        if tab[i] != tab[i+1] : return False
    return True

print(uniformTab ([2, 5, 7, 11]))
print(uniformTab ([2, 2, 2, 2])) 

#EXO 2
def rechDoublons(tab) :
    x = False
    for i in range (0, len(tab)-1) :
        for j in range (i+1,len(tab)) :
            if i != j :
                if tab[i] == tab[j] :
                    if x == False : x  = True
                    else : return False
                    break
    if x == True : return True
    return False

print(rechDoublons ([-3, 1, 5, 9, 13, 17, 21]))
print(rechDoublons ([1, 5, 9, 1, 1, 21])) 
print(rechDoublons ([1, 5, 9, 1, 5, 21])) 
print(rechDoublons ([1, 5, 9, 1, 21])) 

#EXO 3
def rechDoublonsProches(tab) :
    x = len(tab)
    for i in range (len(tab)) :
        for j in range (len(tab)) :
            if i != j :
                if tab[i] == tab[j] :
                    if abs(i-j) < x : x = abs(i-j)
                    break
    if x == len(tab) : return 0
    return x

print(rechDoublonsProches ([3, 4, 5, 1, 9, 3, 6, 1, 4, 3]))
print(rechDoublonsProches ([3, 4, 5, 1, 9, 6]))

#EXO 4
def rechMinDoub(tab) :
    x = MAXINT
    for i in range (len(tab)) :
        for j in range (len(tab)) :
            if i != j :
                if tab[i] == tab[j] :
                    if tab[i] < x : x = tab[i]
                    break
    if x == MAXINT : return -1
    return x

print(rechMinDoub ([2, 3, 4, 13, 9, 2, 13, 17, 21]))
print(rechMinDoub ([3, 4, 5, 1, 9, 6]))
 
#EXO 5
def rechPremDoublons(tab) :
    x = 0
    y = len(tab)
    for i in range (len(tab)) :
        for j in range (i,len(tab)) :
            if i != j :
                if tab[i] == tab[j] :
                    if j < y : 
                        x = tab[j]
                        y = j
                    break 
    if y == len(tab) : return -1
    return x

print(rechPremDoublons ([3, 6, 2, 7, 2, 3, 3, 6, 1]))
print(rechPremDoublons ([3, 4, 5, 1, 9, 6]))