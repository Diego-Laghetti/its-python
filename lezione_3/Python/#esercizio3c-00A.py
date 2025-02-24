#esercizio3c-00A
n: int = int (input("Inserisci il numero di neonati: "))

match n:
    case 1:
        print("congratulazioni")
    
    case 2:
        print("wow!gemelli")
    
    case 3:
        print("wow!tre")
    
    case 4:
        print("mamma mia quattro!wow")
    
    case 5:
        print("incredibile!cinque!")
    
    case _:
        print(f"non ci credo!{n} bambini skibidi sus ")