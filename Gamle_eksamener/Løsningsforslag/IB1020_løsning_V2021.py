
import numpy as np


#Oppgave1a)
def areal_skravert(r):
    
    return (2*r)**2 - np.pi*r**2



#Oppgave1b)

r = 2

areal = areal_skravert(r)

while areal <= 100:
    r = r + 1
    areal = areal_skravert(r)

print(r)


#oppgave2
import numpy as np

x = np.array([9, 17, 5, -3, 2])
sum = 0
for i in range(len(x)):
    sum += x[i]
gx = sum/len(x)

print('Gjennomsnittet er', gx)

vx = 0
for i in range(len(x)):
    vx += (x[i]-gx)**2
    
print('Variansen er', vx/len(x))



#oppgave 3
import random as ra

numberOfSamples = 100000
favourable = 0

for i in range(numberOfSamples):
    siffer1 = ra.randint(1,9)
    siffer2 = ra.randint(1,9) #Vi bruker aldri siffer2 så vi trenger egentlig ikke å trekke det
    siffer3 = ra.randint(1,9)
    if siffer1 == siffer3:
        favourable += 1

print('Sansynligheten for å få et symetrisk tall er ', favourable/numberOfSamples)



#oppgave 4a
def area(x,y):
    return x*y

x = 0.1
y = 19.8
maxX = 0
maxY = 0

while x < 10:   
    if area(x,y) > area(maxX, maxY):
        maxX = x
        maxY = y
    x += 0.1
    y -= 0.2
    
print('Det største arealet får man når x er', round(maxX,2), 'og y er', round(maxY,2))
print('Arealet er da', round(area(maxX, maxY),2))


#oppgave 4b
import numpy as np
import matplotlib.pyplot as plt

xvals = np.linspace(0.1, 9.9, 99)
areaVals = np.zeros(99)
for i in range(99):
    areaVals[i] = area(xvals[i], 20-2*xvals[i])
    
plt.plot(xvals,areaVals)

