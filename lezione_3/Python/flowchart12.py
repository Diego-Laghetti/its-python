#flowchart12
n = int(input("Inserisci n: "))
i = 0
while i != n:
    x = int(input("Inserisci x: "))
    y = int(input("Inserisci y: "))
    if x > 0 and y > 0:
        result = x*y
        print(result)
    elif x < 0 and y < 0:
        print("errore")
    else:
        result = x+y
        print(result)
    i += 1
