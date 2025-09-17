xor = 57
frase = input("Dammi un input: ")
lista = []
lista1 = []

for c in frase:
    r = ord(c) ^ xor
    print (f"{ord(c)} XOR {xor} = {r}")
    lista.append(r)

print(lista)

for n in lista:
    r2 = chr(n ^ xor)
    print (f"{n} XOR {xor} = {n}")
    lista1.append(r2)

print(lista1)