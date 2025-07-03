from string import punctuation

def count_unique_words(s: str) -> dict[str, int]:
    d: dict[str, int] = {} #Dizionario per memorizzare le parole con lunghezza dispari e la loro frequenza
    s = s.split(" ") #Divide la stringa in parole usando lo spazio come separatore
    for token in s:
        token_lower: str = token.lower()#Converte la parola in minuscolo per uniformità
        clean_token: str = token_lower.strip(punctuation) #Rimuove la punteggiatura dai bordi della parola
        if not clean_token or (len(clean_token) % 2 == 0): #Salta se la parola è vuota o ha lunghezza pari
            continue
        if clean_token in d: #Se la parola è già nel dizionario
            d[clean_token] += 1 #Incrementa il conteggio
        else:
            d[clean_token] = 1 #Altrimenti la inserisce con valore iniziale 1
    return d #Restituisce il dizionario risultante

