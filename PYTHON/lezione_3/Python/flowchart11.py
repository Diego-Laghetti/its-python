#flowchart11
while True:
    n = float(input("Inserisci n: "))
    if n%1==0:
        if n%2 == 0 and n > 10:
            print("numero valido")
        else:
            print("numero non valido")
