import time
import random

# Exercices Page 20 poly récurcive

# Exercice 1 sum

def sum(a, b):
    if b == 0 : return a
    return sum(a+1, b-1)

#Exercice 2 factoriel

def fact(n):
    if n==0 : return 1
    return n*fact(n-1)

#Exercice 7

def iterRec(n):
    if n == 0 : return
    print("bonjour")
    iterRec(n-1)

def parTab(tab, k):
    if k == len(tab) : return
    print(tab[k])
    parTab(tab, k+1)

def parTab2(tab,k):
    if k == len(tab) : return
    parTab2(tab, k+1)
    print(tab[k])

def sumRec (tab, x):
    if x == len(tab) : return 0
    return tab[x]+sumRec(tab, x+1)

#Exercice 11












