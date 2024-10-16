# -*- coding: utf-8 -*-
"""
Løsningsforslag til konteeksamen V22
"""

#%% Oppgave 1a
import numpy as np

def volum(r1,  h1, r2, h2):
    volum_sylinder = np.pi*r1**2*h1
    volum_kjegle = 1/3*(np.pi*r2**2*h2)
    return volum_sylinder, volum_kjegle


#%% Oppgave 1b
rad = 7
h_sylinder = 18
h_kjegle = 12

v_sylinder, v_kjegle = volum(rad, h_sylinder, rad, h_kjegle)
v_total = v_sylinder + v_kjegle

print("Volumet ev en sylinder med radius", rad, "cm og høyde", h_sylinder, "cm er", round(v_sylinder,2), "cm3" )
print("Volumet ev en kjegle med radius", rad, "cm og høyde", h_kjegle, "cm er", round(v_kjegle,2), "cm3" )
print("Det totale volumet av figuren er", round(v_total,2), "cm3")

#%% Oppgave 1c
rad = 7
h_sylinder = 18
for h_kjegle in range(3,60+1,3):
    v_sylinder, v_kjegle = volum(rad, h_sylinder, rad, h_kjegle)
    v_total = v_sylinder + v_kjegle
    print("Når høyden av kjeglen er", h_kjegle, "cm blir volumet av figuren", round(v_total, 2), "cm3")
    

#%% Oppgave 2a    
resultat = np.array(['G', 'T', 'G', 'IG', 'G', 'G'])
std_nr   = np.array([26255, 26317, 26389, 26711, 27019, 28975])

for j in range(len(resultat)):
    if resultat[j] == 'IG':
        print(j)
        
#%% Oppgave 2b
def finn_ikke_godkjente(resultat, std_nr):
    for j in range(len(resultat)):
        if resultat[j] == 'T':
            print(std_nr[j])
        
finn_ikke_godkjente(resultat, std_nr)

#%% Oppgave 2c
index = 0
antall_G = 0
std_nr_grense = 27222

while index < len(resultat) and std_nr[index] <= std_nr_grense:
    if resultat[index] == 'G':
        antall_G += 1
    index += 1
        
print("Det er", antall_G, "godkjente studenter med studentnummer", std_nr_grense, "eller lavere")


#%% Oppgave 3
"""
Funksjonen f(x) fungerer som den skal. While-løkken vil øke x så lenge f(x) er større enn 0.
Siden f(-1.0) er et negativt tall vil den aldri kjøres og vi vil få skrevet ut at vi har et nullpunkt med x lik -0.1
Hadde man skrevet while f(x) <= 0 ville vi fått et nullpunkt i dette tilfellet     
"""

#%% Oppgave 4
import random as ra

#lager en funksjon for å regne ut tid ved gitt fart og avstand
def tid(fart, avstand):
    return avstand/fart

n = 10000
fordel_rute_2 = 0

tid_rute_1 = tid(20,5)
tid_rute_2_a_b = tid(10,2)

for i in range(n):
    tid_rute_2_b_c = tid(ra.randrange(70,86), 4)
    if tid_rute_2_a_b + tid_rute_2_b_c < tid_rute_1:
        fordel_rute_2 += 1

print("Sansynligheten for at rute 2 lønner seg er", round(fordel_rute_2/n,2) )

