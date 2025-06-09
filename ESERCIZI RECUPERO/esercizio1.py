lista_tuple: list[tuple] = [(0, "a"), (1, "b"), (2, "c")]

def esercizio1(lista: list[tuple]) -> dict:
    dizionario1: dict = {}
    for element in lista:
        key, value = element[0], element[1]
        if key in dizionario1:
            dizionario1[key] += value
        else:
            dizionario1[key] = value
    return dizionario1

