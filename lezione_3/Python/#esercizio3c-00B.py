#esercizio3c-00B
#esercizio3c-00A
n: str = str (input("Inserire nome: "))
g: str = str (input("Inserire gender. Digitare m per maschio e f per femmina: "))

match g:
    case "m":
        print(f"Nome: {n}\nGenere: Maschio")
    
    case "f":
        print(f"Nome: {n}\nGenere: Femmina")
 
    case _:
        print(f"Mi dispiace {n}, non è possibile provedere con la generazione di un documento di identita")