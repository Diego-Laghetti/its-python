'''Crittografia

Sia dato il messaggio cifrato (convertito in numero intero in base 10): 

204751668535
Il messaggio cifrato è stato ottenuto cifrando il messaggio originale con algoritmo RSA senza padding con n=514948966453 e esponente pubblico (e) pari a 3
Provare a decifrare il messaggio cifrato
NB: il messaggio originale è una parola di cinque lettere maiuscole e minuscole.
NB: Quando il problema sembra arduo, allora un approccio brutale potrebbe essere quello vincente.'''

messcifr = 204751668535
m = 514948966453

#alfabeto prima da A-Z e poi a-z
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

#cifro con la brute force tutte le parole di 5 lettere
trovato: bool = False

for p1 in alphabet:
    if trovato:
        break
    for p2 in alphabet:
        if trovato:
            break
        for p3 in alphabet:
            if trovato:
                break
            for p4 in alphabet:
                if trovato:
                    break
                for p5 in alphabet:
                    if trovato:
                        break
                    plain_text = p1+p2 +p3+p4+p5                    
                    try:
                        #plain_text.encode("utf-8") trasforma la stringa in una sequenza di byte usando la codifica utf-8
                        #.hex() trasforma i byte in una rappresentazione esadecimale come stringa
                        #int( ,16) trasforma la stringa esadecimale in un intero decimale
                        plain_text2 = int(plain_text.encode("utf-8").hex(), 16)
                        cifrato = pow(plain_text2, 3, m)

                        if cifrato == messcifr:
                            #printo il risultato
                            print("risultato:", plain_text) 
                            trovato = True

                    except:
                        continue

