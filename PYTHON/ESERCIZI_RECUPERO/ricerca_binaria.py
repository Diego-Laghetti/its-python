'''Implementa una funzione che effettua la ricerca binaria in una lista di numeri interni ordinati e ritorna True se il numero è all’interno del della lista,
 altrimenti False.'''

def RicercaBinaria(num: int, lista: list[int]) -> bool:
    lista2 = sorted(set(lista)) 
    low  = 0 # indice minore
    high = len(lista2) - 1 # indice maggiore
    while low <= high:
        meta = (low + high) // 2 #metà
        hogrider = lista2[meta] # elemento centrale
        if hogrider == num: #trovato
            return True
        elif hogrider < num: #cerca nella metà destra
            low = meta + 1
        else: #cerca nella metà sinistra
            high = meta - 1
    return False 

        


        


