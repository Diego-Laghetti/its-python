#esercizio5-11
numeri=list(range(1, 13))
print (numeri)

for i in numeri:
    if i==1:
        print (f"{i}st")
    elif i==2:
        print (f"{i}nd")
    elif i==3:
        print (f"{i}rd")
    else:
        print (f"{i}th")