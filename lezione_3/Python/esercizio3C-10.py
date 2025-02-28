#esercizio3C-10
g= int(input("Inserisci numero giorno: "))
m= str(input("Inserisci mese: "))

data=(g,m)
match data:
    case data if g == 1 and m == "gennaio":
        print("Capodanno")
    case data if g == 14 and m == "febbraio":
        print("San Valentino")
    case data if g == 2 and m == "giugno":
        print("Festa della Repubblica Italiana")
    case data if g == 8 and m == "giugno":
        print("Festa PlayDido")
    case data if g == 15 and m == "agosto":
        print("Ferragosto")
    case data if g == 31 and m == "ottobre":
        print("Halloween")
    case data if g == 25 and m == "dicembre":
        print("Natale")
    case _:
        print("Nessuna festività importante in questa data")