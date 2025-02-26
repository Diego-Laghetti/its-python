#esercizio3C-4
Mammiferi:list =["cane", "gatto", "cavallo", "elefante", "leone"]
Rettili:list =["serpente", "lucertola", "tartaruga", "coccodrillo"]
Uccelli:list =["aquila", "pappagallo", "gufo", "falco"]
Pesci:list =["squalo", "trota", "salmone", "carpa"]

animale= str(input("Inserisci animale "))

match animale:
    case animale if animale in Mammiferi:
        print(f"{animale} appartiene alla categoria dei Mammiferi!")
    case animale if animale in Rettili:
        print(f"{animale} appartiene alla categoria dei Rettili!")
    case animale if animale in Uccelli:
        print(f"{animale} appartiene alla categoria dei Uccelli!")
    case animale if animale in Pesci:
        print(f"{animale} appartiene alla categoria dei Pesci!")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}!")



