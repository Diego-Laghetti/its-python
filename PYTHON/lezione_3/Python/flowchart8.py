#flowchart8
a = int(input(f"inserisci valore intero positivo a: "))
b = int(input(f"inserisci valore intero positivo b: "))
if a < b : 
    if a > 0 and b > 0 : 
        if a % 1 == 0 and b % 1 == 0 : 
            sum = 0 
            i = a 
            while i < b : 
                sum = sum + i 
                i = i + 1 
            print(f" la somma è {sum}")
        else : 
            print(f" A e B devono essere interi")
    else : 
        print (f"A e B devono essere positivi")
else : 
    print(f" A deve essere minore di B")

