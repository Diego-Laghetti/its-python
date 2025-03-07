#flowchart7
pari = 0
dispari = 0
cont = 0
for i in range(10):
    n= int(input("Leggi n: "))
    if n%2==0:
        pari+=1
    else:
        dispari+=1

print("I numeri pari sono: ", pari)
print("I numeri dispari sono: ", dispari)
       