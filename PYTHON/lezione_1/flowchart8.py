#flowchart8
soglia= int(input("Leggi soglia: "))
cont = 0
for i in range(7):
    n= int(input("Leggi n: "))
    if n > soglia:
        print(f"{n} è maggiore della soglia {soglia}")
    cont+=1