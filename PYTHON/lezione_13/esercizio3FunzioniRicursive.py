#esercizio3FunzioniRicursive
def recursiveSumInRange(a:int, b:int) -> int:
    if a > b:
        temp:int = a
        a = b
        b = temp 
    if b == a:
        return int(a)
    else:
        return int(b + recursiveSumInRange(a, b-1))
    
print(recursiveSumInRange(10,5))