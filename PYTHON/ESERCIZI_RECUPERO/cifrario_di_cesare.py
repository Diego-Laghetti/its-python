'''Cifrario di Cesare
Il cifrario di Cesare è un antico metodo crittografico che rende alcune informazioni nascoste a chi non possiede la chiave per decifrarle.
Immagina l’alfabeto come una lista ordinata di lettere (puoi importare la lista delle lettere dell’alfabeto minuscole scrivendo from string import ascii_lowercase
Ogni lettera ha una posizione in questa lista:
● a è 1 ● b è 2 ● j è 10 ● e così via…
Il cifrario di Cesare nasconde l’informazione utilizzando una chiave, che è un numero intero positivo, da sommare alla posizione della lettera originale: il risultato 
ottenuto corrisponde alla posizione della lettera cifrata.
● a con key = 2 diventa c
Se la chiave porta oltre la fine dell’alfabeto, si ricomincia dal principio:
● a con key = 28 diventa c
Per decriptare (o “decifrare”) il messaggio, si applica la stessa procedura ma muovendosi all’indietro nell’alfabeto. Devi fornire le funzioni:
caesar_cypher_encrypt(s, key)
caesar_cypher_decrypt(s, key)
dove:
● s è una stringa (lettera, parola, frase, ecc.).
● key è un numero intero positivo, la chiave del cifrario di Cesare.
La tua implementazione deve trasformare soltanto le lettere ASCII maiuscole e minuscole.
Caratteri speciali, numeri e lettere accentate non devono essere modificati.
Le funzioni non devono stampare nulla a schermo, ma restituire la stringa cifrata o decifrata.'''

from string import ascii_lowercase

def ceasar_cypher_encrypt (s: str, key: int) -> str:
    risultato = ''
    key = key % 26 #il numero se supera il 26 riparte da 1
    for carattere in s:
        if carattere in ascii_lowercase: #se il carattere è compreso nin ascii_lowercase
            x = ascii_lowercase.index(carattere) #prende la posizione del carattere nella lista con .index()
            nuovocarattere = ascii_lowercase[(x + key) % 26] #valore del nuovo carattere
            risultato += nuovocarattere #aggiunge il nuovo carattere al risultato
        else: #se il carattere non è compreso in ascii_lowercase 
            risultato += carattere 
    return risultato

def ceasar_cypher_decrypt (s: str, key: int) -> str:
    return ceasar_cypher_encrypt(s, -key) #richiama la funzione di prima al contrario


criptato = ceasar_cypher_encrypt("ciao belli de casa forza lazio", 26)
print("Criptato:", criptato)

decriptato = ceasar_cypher_decrypt(criptato, 26)
print("Decriptato:", decriptato)