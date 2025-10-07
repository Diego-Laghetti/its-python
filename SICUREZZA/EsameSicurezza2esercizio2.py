'''Premessa: nell'RSA, per calcolare con python l'esponente privato nota la chave pubblica e noti i due numeri primi p e q, si utilizza la sequente funzione
d = inverse(e, phi) dove ph = (p-1)*(q-1).

Sia dato n (pari a p*q) = 51151902024533551
e siano
e (esponente pubblico) = 3
C=10002041662569686 il messaggio cifrato (l'originale è una parola di sette caratteri alfanumerici)
Decifrare il messaggio
NB: un attacco forza bruta su 7 caratteri ha un costo computazionale pari a 62^6 = 56.800.235.584 (infattibile in python)
NB: ma n=p*q e quindi se riuscissi a trovare i due numeri primi che fattorizzano n, allora potrei applicare euclide inverso (la funzione inverse) per trovare la chiave privata...'''
from Crypto.Util.number import inverse

n = 51151902024533551
p = None
q = None

#ciclo che prova tutti i numeri da 2 fino alla radice quadrata di n
for i in range(2, int(n**0.5) + 1):  
    #controlla se 'i' divide n senza resto
    if n % i == 0:  
        #se l'if èp vero allora i è un fattore primo
        p = i  
        #l'altro fattore q si ottiene dividendo n per p
        q = n // i  
        #fermo il ciclo
        break  

#printo p e q
print("p =", p)
print("q =", q)

#calcolo del modulo n
n = p*q

#calcolo della funzione di eulero
phi = (p-1)*(q-1)

#esponente pubblico(3)
e = 3

#messaggio cifrato intero
messcifr = 10002041662569686 

#calcolo chiave privata d come inverso modulo 
d = inverse(e, phi)

#decifratura del messaggio: messcifr^d mod n
messdec = pow(messcifr, d, n)

#printo il messaggio dcifrato
print(messdec)

#conversione dell'intero decifrato in byte
#messdec.bit_length() restituisce il numero di bit che servono per rappresentare messdec in binario
#lunghezza in byte, il +7 arrotonda per eccesso, diviso 8 perchè ogni byte sono 8 bit
length = (messdec.bit_length() + 7) // 8 
#messdec.to_bytes(length, 'big') converte l’intero messdec in una sequenza di byte di lunghezza length
#'big' = il byte più significativo viene messo all’inizio
messbyte = messdec.to_bytes(length, 'big')

#conversione dei byte in stringa utf-8
messdectext = messbyte.decode('utf-8')

#stampa il messaggio decifrato leggibile
print(f"risultato: {messdectext}")

