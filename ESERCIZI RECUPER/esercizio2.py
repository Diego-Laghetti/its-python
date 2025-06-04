def esercizio2 (lista: list [int|float]) -> dict[str, list[int|float]]:
    dizionario2: dict[str, list[int|float]] = {"positivi": [], "negativi": []}
    for numero in lista:
        if numero >= 0:
            dizionario2["positivi"].append(numero)
        else:
            dizionario2["negativi"].append(numero)
    return dizionario2

lista: list[int|float] = [1, 2, -4, 5, -7, 42, 78, -94]
print(esercizio2(lista))