#flowchart2repeat
max= int(input("Leggi il valore massimo: "))
cont = 1
while True:
    n= int(input("Leggi il valore di n: "))
    if n > max:
        max=n
    cont=cont+1
    if cont == 4:
        break
print(max)
    

