#esercizio3C-8
frase = str(input("Inserisci la frase: "))

match frase:
    case frase if frase[-1] == "?" and len(frase) % 2 == 0:
        print("Si")
    case frase if frase[-1] == "?" and len(frase) % 2 == 1:
        print("No")
    case frase if frase[-1] == "!":
        print("Wowo!")
    case _:
        print(f"Tu dici {frase}")