#flowchart9
while True:
    n = float(input("Inserisci n: "))
    if n > 0:
        if n % 1 == 0: 
            cont = 0
            i=0
            for i in range (10):
                x = int(input("Inserisci x: "))
                if x % n == 0:
                    cont+= 1
                i += 1
            print(cont)
            break
        else:
            print("n deve essere intero positivo")
    else:
        print(f"{n} deve essere positivo")

        
            
