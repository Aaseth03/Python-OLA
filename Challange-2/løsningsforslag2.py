"""
oppg. 1
Hvilken type telefon har Thea?
Bruk register.py som en modul og hent ut informasjonen i en annen fil.
Ikke se i register.py, bruk coden under for å begynne"

Hint: Telefon typen ligger skrevet under "TLF"
"""
import register

print(register.Klasseliste)

Thea_TLF = register.Thea["TLF"]
print(f"Thea har {Thea_TLF} telefon.")


"""
Løkker er ikke en del av pensum før uke 40. Prøv alikevel å lese deg opp på strukturen til ei løkke og se om oppgaven lar seg løses!
Skjekk Loops.py for hint til løkke strukturen.
"""

"""
oppg.2

Lag et program som bruker ei for-løkke til å summere de N første 2-er
potensene, dvs summen:
2^1 + 2^2 + 2^3+ . . . +2^N

(N>0 er et positivt heltall, for eksempel kan N=28, og det siste tallet i summen
blir da 2^28).
"""
N = 28
Sum = 0
for x in range(N):
    Sum += 2**(x+1) #NB! Oppgaven spesifiserer at hver eksponent er >0 dette fører til (x+1) siden x vil begynne på 0. 

print(f"Summen av de {N} første 2'er potensene er {Sum}")

"""
oppg.3

Lag et program som bruker ei while-løkke til å summere de N første 2-er
potensene, dvs summen:
2^1 + 2^2 + 2^3 + . . . +2^N

Hvor mange itterasjoner trengs for at summen er over 8000? Hva blir summen?
(N>0 er et positivt heltall, for eksempel kan N=28, og det siste tallet i summen
blir da 2^28).
"""
N2 = 0
sum2 = 0
while (sum2 < 8_000):
    N2 += 1
    sum2 += 2**N2

print(f"For at summen skal overstige 8.000 må N være høyere enn {N2}. N = {N2} gir sum = {sum2}")