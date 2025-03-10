#esercizio8-14
def make_car(brand, type, color, tow):
    
    return f"{brand}, modello {type}, colore {color}, tow_package {tow}"

profilo = {"brand": "porsche", "modello": "911", "colore": "rosa", "tow_package": "presente"}


auto = make_car(profilo["brand"], profilo["modello"], profilo["colore"], profilo["tow_package"])

print(auto)