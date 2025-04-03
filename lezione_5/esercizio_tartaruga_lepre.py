#esercizio_tartaruga_lepre
import random
posizione_iniziale = 1
percorso_lunghezza = 70
energia_iniziale = 100
ostacoli = {15: -3, 30: -5, 45: -7}
bonus = {10: 25, 25: 3, 50: 10}

energia_tartaruga = energia_iniziale
energia_lepre = energia_iniziale
l = posizione_iniziale 
t = posizione_iniziale
print("BANG!!!!!!!!!!!!AND THEY'RE OFF!!!!!!!!!!!!!!!\n")

def mosse_tart():
    numero = input(random(1,11))
    if numero >= 1 and numero <= 5:
        t *= 3
    elif numero == 6 or numero == 7:
        t -= 6
    else:
        t+= 1

def mosse_lepre():
    numero2 = input(random(1,11))
    if numero2 == 1 or numero2==2:
        l = 0
    elif numero2 == 3 or numero2 == 4:
        l += 9
    elif numero2 == 5:
        l -= 9
    elif numero2 >=6 and numero2 <= 8:
        l += 1
    else:
        l -= 2


def stampa_pista(percorso_lunghezza, pista):
        pista = ["_"] * percorso_lunghezza
        print(pista)
        
while l or t == 70:
    stampa_pista(70, "_")
    print(l)
    print(t)
    mosse_lepre()
    mosse_tart()





    




