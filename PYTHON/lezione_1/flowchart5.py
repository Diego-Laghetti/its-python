#flowchart5
n= int(input("Leggi n: "))
if n<2:
    print(f"Il numero non è primo")
else:
    div=2
    while div < n:
        if n%div==0:
            print("Il numero non è primo")
            break
        else:
            div=div+1
    else:
        print("Il numero è primo")
