# -*- coding: utf-8 -*-

#%% Oppgave 1a

def panteautomat(a, b):
    pant_liten = 2
    pant_stor = 3
    return a * pant_liten + b * pant_stor


#oppgave 1b
små_flasker =  12
for store_flasker in range(5, 23+1, 2):
    print(panteautomat(små_flasker, store_flasker))
    
#%%Oppgave 2a
import numpy as np

def sorter(arr):
    #sjekker om de ligger i feil rekkefølge
    if(arr[0] < arr[1]):
        tmp = arr[0]
        arr[0] = arr[1]
        arr[1] = tmp
    return arr
    
#oppgave 2b

# Denne trenger dere ikke å lage, men om dere vil teste programmet kan
#man få et array med 1000 tilfeldige tall mellom 1 og 5 med denne linja
arr2 = np.random.default_rng().uniform(low=1.0, high=5.0, size=(1000))

sum = 0
grense = 850
indeks = 0

while(sum <= grense):
    sum += arr2[indeks]
    indeks += 1

#Det siste tallet vi la til ligger på plass index - 1 siden det siste vi gjør i 
#while-løkka var å legge til 1
print("Tallet som medførte at summen gikk over", grense, "er", arr2[indeks-1])


#oppgave 2c
"""
Vi vet at vi har 1000 tall og den minste verdien de kan ha er 1.0.
Summen av alle tallene må være minimum 1000*1.0 = 1000
"""

#%% oppgave 2d
def finn_element(x, arr):
    indeks = -1
    for element in arr:
        indeks += 1
        if(element == x):
            print("Elementet", element, "ligger på plass", indeks, "i arrayet" )



#%% oppgave 3
import random as ra

n = 10000
gunstige = 0

for i in range(n):
    #trekker tre tall
    tall1 = ra.randint(0, 4)
    tall2 = ra.randint(0, 4)
    tall3 = ra.randint(0, 4)
    
    if tall1 + tall2 + tall3 == 0:
        gunstige += 1

print("Sansynlgheten for at du vinner 100 kroner er", gunstige/n)

#%% oppgave 4
"""
 Vi må først regne ut hva b må vøre for at arealer skal vøre 10
 Areal = a*b/2 = 10
         a*b = 20
         b = 20/a
"""
import numpy as np

def hypotenus(katet1, katet2):
    return np.sqrt(katet1**2 + katet2**2)

def omkrets(a, b):
    return a + b + hypotenus(a,b)


a_vals = np.linspace(0.01, 2000, 100000)
minste_omkrets = np.inf
beste_a = 0

for a in a_vals:
    omkr = omkrets(a, 20/a)
    if(omkr < minste_omkrets):
        minste_omkrets = omkr
        beste_a = a


print("minste omkretst er", minste_omkrets, "når a er", beste_a, "og b er", 20/beste_a)






















