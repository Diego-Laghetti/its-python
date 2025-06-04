def esercizio5(lista: list[int], threshold: int = 5) -> int:
    ris = 1
    for elemento in lista:
        if elemento < threshold:
            ris *= elemento
    return ris

lista = [2, 3, 4, 2, 5, 6, 7]
print(esercizio5(lista))
