#flowchart5
n=int(input("Leggi n: "))
if n % 1 == 0 and n > 0:
    sum = 0
    i = 0
    while True:
        if i > n:
            print(sum)
            break
        else:
            sum = sum + i*i
            i = i +1
else:
    print("Errore, n deve essere positivo")

    

