def recorsiva(lista):   
    if len(lista) == 0:
        return
    print(lista[-1])
    recorsiva(lista[:-1])

recorsiva((1,2,3,4,5))