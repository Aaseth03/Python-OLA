

#%% oppgave 1a
import numpy as np

def kule(r):
    overflate = 4*np.pi*r**2
    volum = (4/3)*np.pi*r**3
    return overflate, volum

#%% oppgave 1b

radier = np.arange(150,5-1, -5)

for r in radier:
    overflate, volum = kule(r)
    print("For en kule med radius", r, "er overflaten", round(overflate,2), "og volumet", round(volum,2))
    
    
#%% oppgave 2a
#skriver ut alle indekser hvor elementet er 3

arr1 = np.random.randint(1,4,size=500)

for i in range(len(arr1)):
    if arr1[i] == 3:
        print(i)
        
#%% oppgave 2b

enere = 0 
toere = 0 
treere = 0

for tall in arr1:
    if tall == 1:
        enere += 1
    elif tall == 2:
        toere += 1
    else:
        treere += 1
        
print("Det var", enere, "enere,", toere, "toere og", treere, "treere")
        

#%% oppgave 2c

import matplotlib.pyplot as plt
navn = np.array(["enere", "toere", "treere"])
fordeling = np.array([enere, toere, treere])
plt.bar(navn, fordeling)

#%% oppgave 2d
def to_treere(arr):
    funnet = False
    i = 0
    while i < len(arr)-1 and funnet == False:
        if arr[i] == 3 and arr[i+1] == 3:
            funnet = True
        i += 1
        
    if funnet == True:
        print("I arr1 finnes det to påfølgende elementer som begge har verdi 3")   
    else:
        print("I arr1 finnes det ikke to påfølgende elementer som begge har verdi 3")   
        
to_treere(arr1)

#%% oppgave 3

sample_space  = np.linspace(1,  2178, 2178)

n = 100000 #antall  forsøk
gunstige = 0

for i in range(n):
    
    tall = np.random.choice(sample_space,  2, False)
    
    if (tall[0] >= 2000 and tall[1] >= 2000):
        gunstige +=1

print('Sannsynligheten (i prosent) er', (gunstige/n)*100)        
        


#%% oppgave 4

xvals = np.linspace(0.5, 4.0, 1000)
yvals = np.log(xvals)
minste_avstand = np.inf

for i in range(len(xvals)):
    avstand = np.sqrt(xvals[i]**2 + yvals[i]**2)
    if avstand < minste_avstand:
        minste_avstand = avstand
        
print("minste avstand er", minste_avstand)

