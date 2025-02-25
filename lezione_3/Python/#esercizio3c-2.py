#esercizio3c-2
voto: int = int (input("Inserisci voto: "))
match voto:
    case voto if voto <= 110 and voto >= 106:
        print("Gpa: 4.0")
    case voto if voto <= 105 and voto >= 101:
        print("Gpa: 3.7")
    case voto if voto <= 100 and voto >= 96:
        print("Gpa: 3.3")
    case voto if voto <= 95 and voto >= 91:
        print("Gpa: 3.0")
    case voto if voto <= 90 and voto >= 86:
        print("Gpa: 2.7")
    case voto if voto <= 85 and voto >= 81:
        print("Gpa: 2.3")
    case voto if voto <= 80 and voto >= 76:
        print("Gpa: 2.0")
    case voto if voto <= 75 and voto >= 70:
        print("Gpa: 1.7")
    case voto if voto <= 69 and voto >= 66:
        print("Gpa: 1.0")
    case _:
        print("Voto non valido")