#flowchart2for
max= int(input("Leggi il valore massimo: "))
i = 0
for i in range(3):
    i=i+1
    n= int(input("Leggi il valore di n: "))
    if n>max:
        max=n
    else:
        continue
print(f"Il valore massimo è: {max}")
