#esercizio3C-6
mammiferi:list =["cane", "gatto", "cavallo", "elefante", "leone", "balena", "delfino"]
rettili:list =["serpente", "lucertola", "tartaruga", "coccodrillo"]
uccelli:list =["aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
pesci:list =["squalo", "trota", "salmone", "carpa", "delfino"]
acqua: list =["squalo", "trota", "salmone", "carpa", "delfino"]
terra: list =["cane", "gatto", "cavallo", "elefante", "leone", "serpente", "lucertola", "tartaruga", "coccodrillo", "aquila", "pappagallo", "gufo", "falco", "cigno", "anatra", "gallina", "tacchino"]
aria: list =["aquila", "pappagallo", "gufo", "falco",  "anatra"]

animal_type = "Unknown"

animale= str(input("Inserisci animale "))
habitat= str(input("Inserisci habitat "))

match animale:
    case animale if animale in mammiferi:
        animal_type = "mammiferi"
    case animale if animale in rettili:
        animal_type = "rettili"
    case animale if animale in uccelli:
        animal_type = "uccelli"
    case animale if animale in pesci:
        animal_type = "pesci"
    case _:
        print("non va bene")

animale_info: dict ={"nome": animale, "tipo_animale": animal_type, "habitat": habitat}

match animale_info:
    case animale_info if animale_info["habitat"]=="terra" and animale_info["nome"] in terra and animale_info["tipo_animale"] == "mammiferi":
        print(f"{animale} è uno dei mammiferi che vive sulla terra")
    case animale_info if animale_info["habitat"]=="aria" and animale_info["nome"] in aria and animale_info["tipo_animale"] == "uccelli":
        print(f"{animale} è uno dei uccelli che vive in aria")
    case animale_info if animale_info["habitat"]=="acqua" and animale_info["nome"] in acqua and animale_info["tipo_animale"] == "pesci":
        print(f"{animale} è uno dei pesci che vive nell'acqua")
    case animale_info if animale_info["habitat"]=="terra" and animale_info["nome"] in terra and animale_info["tipo_animale"] == "rettili":
        print(f"{animale} è uno dei rettili che vive sulla terra")
    case animale_info if animale_info["habitat"]=="terra" and animale_info["nome"] in terra and animale_info["tipo_animale"] == "uccelli":
        print(f"{animale} è uno degli uccelli che vive sulla terra")
    case animale_info if animale_info["habitat"]=="acqua" and animale_info["nome"] in acqua and animale_info["tipo_animale"] == "mammiferi":
        print(f"{animale} è uno dei mammiferi che vive in acqua")
    case _:
        print("Non sono in grado di associare questo animale ad un habitat specifico")