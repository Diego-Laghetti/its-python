#flowchart8

a = int(input("Inserisci a: "))
b = int(input("Inserisci b: "))

if a >= b:
    print("a deve essere minore di b")
elif a < 0 or b < 0:
    print("a e b devono essere positivi")
elif a % 1 != 0 or b % 1 != 0:
    print("a e b devono essere interi")
else:
    somma = 0
    for i in range(a, b):
        somma += i
    print("La somma dei numeri tra a e b è:", somma)

