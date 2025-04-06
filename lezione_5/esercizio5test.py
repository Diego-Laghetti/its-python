def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    list = []
    cont= 0
    risultato = 0
    for n in range(len(x)):
        risultato = x[cont] + y[cont]
        list.append(risultato)
        cont+=1
    return list

print(somma_elementi([1,1,1],[1,1,1]))
