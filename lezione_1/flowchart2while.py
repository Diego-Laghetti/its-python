#flowchart2while
max= int(input("Leggi il valore massimo: "))
cont = 1
while cont < 4:
    cont = cont + 1
    n= int(input("Leggi il valore di n: "))
    if n > max:
        max = n
    else:
        continue

print(max)        