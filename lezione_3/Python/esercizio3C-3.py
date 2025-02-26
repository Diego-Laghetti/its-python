#esercizio3c-3
oggetti = []

while len(oggetti) < 3:
    x=str(input("Inserisci oggetto "))
    oggetti.append(x)

match oggetti:
    case ["penna", "matita", "quaderno"]:
        print("Materiale scolastico")
    case ["pane","latte","uova"]:
        print("Prodotti alimentari")
    case ["sedia", "tavolo", "armadio"]:
        print("Mobili")
    case ["telefono", "computer", "tablet"]:
        print("Dispositivi elettronici")
    case _:
        print("Categoria sconosciuta")