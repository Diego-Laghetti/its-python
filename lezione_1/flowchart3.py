#flowchart4
sum=0
cont=1
while True:
    n= int(input("Leggi il valore di n: "))
    if n > 0:
        sum=sum+n
    cont=cont+1
    if cont == 5:
        break
print(sum)