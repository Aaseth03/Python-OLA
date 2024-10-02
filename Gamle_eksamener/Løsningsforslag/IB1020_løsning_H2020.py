# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 10:33:13 2020
Eksamen 2020 løsningsforslag
@author: joakim
"""

#oppgave 1a
def trapes(a,b,h):
    return h*(a+b)/2

#oppgave 1b
sum = 0
for b in range(3,13):
    sum+=trapes(5,b,7)
    
#oppgave 2a
n = 3
sum = 0
for i in range(n+1):
    sum+=2**i
   
#oppgave 2b
n = 0
sum = 0
while sum < 8000:
    sum+=2**n
    n+=1

print(n)
    
#oppgave 2c
def f(a,n):
    sum = 0
    for i in range(n+1):
        sum+=a**i
    return sum

#oppgave 3
import numpy as np
n= 10000
gunstige = 0

for i in range(n):
    le = np.random.uniform(0,6)
    m = np.random.uniform(0,6)
    j = np.random.uniform(0,7.7)
    if le > m and m > j:
        gunstige+=1

print(round(gunstige/n, 2))

#oppgave 4
import numpy as np

def y(x):
    return x**2

def distance(x1, y1, x2, y2):
    return np.sqrt((x2-x1)**2 + (y2-y1)**2)

x1 = -1
min_dist = distance(x1, y(x1), 0, 2)

while x1 < 2:
    x1 += .01
    min_dist = min(min_dist, distance(x1, y(x1), 0, 2))
                    
print(round(min_dist,3))
    
