def esercizio3(dizionario3: dict[str, float]) -> dict:
    dizionario: dict = {}
    for key, value in dizionario3.items():
        if value < 50:
            sconto = (value * 10) / 100
            prezzo_arrotondato = round(sconto, 2)
            dizionario[key] = prezzo_arrotondato
    return dizionario

dizionario3 = {"pane": 51, "cacca": 35, "pene": 79}
print(esercizio3(dizionario3))


