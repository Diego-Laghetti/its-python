#flowchart2for
max= int(input("Leggi il valore massimo: "))
for i in range(3):
    n= int(input("Leggi il valore di n: "))
    if n>max:
        max=n
print(f"Il valore massimo è: {max}")
