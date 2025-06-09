'''Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati e ritorna True se il numero è all’interno del della lista,
 altrimenti False.'''

def RicercaBinaria(nummero: int, lista: list[int]) -> bool:
    lista2 = sorted(set(lista)) # HO IL PASS ROYALE
    low  = 0 # indice minore
    high = len(lista2) - 1 # indice maggiore
    while low <= high:
        meta = (low + high) // 2 #metà
        hogrider = lista2[meta] # elemento centrale

        if hogrider == nummero: #trovato
            return True
        elif hogrider < nummero: #cerca nella metà destra
            low = meta + 1
        else: #cerca nella metà sinistra
            high = meta - 1
    return False 

        


        


