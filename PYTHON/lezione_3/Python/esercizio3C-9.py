#esercizio3C-9
x = int(input("Inserisci la coordinata X: "))
y = int(input("Inserisci la coordinata Y: "))
punto = (x, y)
match punto:
    case (0, 0):
        print(f"Il punto {punto} si trova nell'origine.")
    case (x, 0):
        print(f"Il punto {punto} si trova sull'asse X.")
    case (0, y):
        print(f"Il punto {punto} si trova sull'asse Y.")
    case (x, y) if x > 0 and y > 0:
        print(f"Il punto {punto} si trova nel primo quadrante.")
    case (x, y) if x < 0 and y > 0:
        print(f"Il punto {punto} si trova nel secondo quadrante.")
    case (x, y) if x < 0 and y < 0:
        print(f"Il punto {punto} si trova nel terzo quadrante.")
    case _:
        print(f"Il punto {punto} si trova nel quarto quadrante.")
