#flowchart13
x = int(input(f"inserisci valore x "))
y = int(input(f"inserisci valore y "))
z = int(input(f"inserisci valore z "))
if x % 1 == 0 and x > 0 : 
    if y % 1 == 0 and y > 0 : 
        if z % 1 == 0 and z > 0 : 
            if (x + y + z) % 2 == 0 and x % 3 == 0 and y % 5 == 0 and z % 7 == 0 :
                print(f"regole rispettate")
            else : 
                print(f"regole non rispettate")
        else : 
            print(f"z deve essere intero e positivo")
    else : 
        print(f"y deve essere intero e positivo")
else : 
    print(f"x deve essere intero e positivo")
