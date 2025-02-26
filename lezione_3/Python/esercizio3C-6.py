#esercizio3C-6
mammiferi:list =["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili:list =["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list =["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci:list =["squalo", "trota", "salmone", "carpa"]
acqua: list =["squalo", "trota", "salmone", "carpa"]
terra: list =["cane", "gatto", "cavallo", "elefante", "leone", "serpente", "lucertola", "tartaruga", "coccodrillo", "aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
aria: list =["aquila", "pappagallo", "gufo", "falco",  "anatra"]

animal_type = "Unknown"

animale= str(input("Inserisci animale "))
habitat= str(input("Inserisci habitat "))

match animale:
    case animale if animale in mammiferi:
        animal_type == "mammiferi"
    case animale if animale in rettili:
        animal_type == "rettili"
    case animale if animale in uccelli:
        animal_type == "uccelli"
    case animale if animale in pesci:
        animal_type == "pesci"
    case _:
        print("non va bene")

animale_info: dict ={"nome": animale, "tipo_animale": animal_type, "habitat": habitat}

match animale_info:
    case animale_info if animale_info["habitat"]=="terra" and animale_info["nome"] in terra and animale_info["tipo_animale"] == "mammiferi":
        print(f"{animale} è uno dei mammiferi che vive sulla terra")