#flowchart6
x=int(input("Leggi x: "))
somma = 0
if x > 0:
    i = 0
    while True:
        if i == 10:
            print(somma)
            break
        else:
            n=int(input("Leggi n: "))
            if x% 2 == 0:
                if n > x/2:
                    somma+=n
            else:
                if n<x:
                    somma=somma+n
        i+=1

else:
    print("Errore, x deve essere positivo")
    