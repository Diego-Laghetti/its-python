#flowchart6
while True:
    n= int(input("Leggi n: "))
    if n> 0:
        break
    else:
        print("Il numero inserito deve essere positivo")
fattoriale = 1
i = 1
for i in range(1,n+1):
    fattoriale *= i
    i=i+1
    if 1==n+1:
        break
print(fattoriale)
        

