
# coding: utf-8

# ## Boucles

# afficher les nombres de 1 à 10
# 
# afficher la somme des nombres pairs entre 2 et un entier saisi par l'utilisateur

# In[1]:

for i in range(1, 11):
    print(i)


# In[2]:

n=int(input('Entrez un nombre '))
som=0
for i in range (n+1):
    if i%2 == 0 : som=som+i
print(som)


# In[3]:

liste=[3, 4, 5]
print(len(liste))


# ## Fonctions

# ### Exercice

# Ecrire (et tester) les fonctions suivantes :
# - rechDoublons qui indique si des doublons sont présents dans le tableau tab
# - rechDoublonsVoisins qui indique si des doublons sont présents côte à côte dans le tableau tab

# In[6]:

def rechDoublonsVoisins(tab):
    for i in range(len(tab)-1):
        if tab[i]==tab[i+1]: return True
    return False

tab=[4, 5, 5]
print(rechDoublonsVoisins(tab))
tab=[4, 5,4]
print(rechDoublonsVoisins(tab))


# In[4]:

def rechDoublons(tab):
    for i in range(len(tab)):
        for j in range(i+1,len(tab)):
            if tab[i]==tab[j]: return True
    return False

tab=[4, 6, 5]
print(rechDoublons(tab))
tab=[6, 5,6]
print(rechDoublons(tab))


# In[7]:

def rechDoublonsV2(tab):
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i]==tab[j] and i!=j: return True
    return False

tab=[4, 6, 5]
print(rechDoublonsV2(tab))
tab=[6, 5,6]
print(rechDoublonsV2(tab))


# ## Timing de code 

# In[3]:

import random
def tabQq(n, min, max):      
    return [random.randint(min, max)  for i in range(n)]# liste en comprehension

def tabRange(n):      
    return [i for i in range(n)]# astuce python : liste en comprehension

def tabRange(n):
    res=[]
    for i in range(n):
        res.append(i)
    return res

def tabCr(n, min, max):
    liste = tabQq(n, min,max)
    liste.sort()
    return liste

print(tabQq(12, -10, 20))
print(tabRange(12))


# In[ ]:




# In[15]:

import time
print("rechDoublons sur tabSansDoub")
for taille in [100, 1000 , 10000]:
    tabSansDoub = tabRange(taille)
    start = time.time()
    # code à timer
    rechDoublons(tabSansDoub)
    #
    end=time.time()
    
    print('taille = ', taille, ' en ', end-start, 'sec')


# In[8]:

import time
print("rechDoublonsVoisins sur tabSansDoub")
for taille in [100, 1000 , 10000, 30000]:
    tabSansDoub = tabRange(taille)
    start = time.time()
    # code à timer
    rechDoublonsVoisins(tabSansDoub)
    #
    end=time.time()
    
    print('taille = ', taille, ' en ', end-start, 'sec')

 