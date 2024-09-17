"""
Created on Wed Sep  4 14:55:58 2024

@author: christofferaaseth
"""

"""
Oppg.1 *
Lag en funksjon som konverterer grader til radianer.
**Bonus om svaret er uttrykt som ne brøk med pi**
"""
from fractions import Fraction

def grad_conv(grad):
    rad = Fraction(grad,180)
    print(f"{grad} grader er pi * {rad} radianer")
    return 0

grad_conv(60)


"""
Oppg.2 **
Lag en funksjon som regner ut arealet av en trapes.
Funksjonen skal ha inn parameterene a,b,h. h er høyden, a og b er lengdene på sidekantene
"""

def A_trap(a,b,h):
    A = ((a+b)*h)/2
    print(f"Arealet av et trapes med a = {a}, b = {b}, h = {h} er A = {A}")
    return 0

A_trap(2,3,5)


"""
Oppg.3 ***
Lag en funksjon som faktoriserer en 2.grads likning ved bruk av ABC-formelen.
Funksjonen tar inn argumentene a,b,c. Når y = a*x^2 + b*x + c => (x - x_1)(x - x_2)
"""
import numpy as np

def factorize(a,b,c):
    x_1 = (-b + np.sqrt(b**2 - 4*a*c))/2*a
    x_2 = (-b - np.sqrt(b**2 - 4*a*c))/2*a
    
    print(f"{a}x^2 + {b}x + c = (x - {x_1})(x - {x_2})")
    
    return 0

factorize(1,2,1)