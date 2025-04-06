def check_value(numero):
    if numero > 5:
        print(f"il numero è maggiore di 5")
    elif numero < 5:
         print(f"il numero è minore di 5") 
    else:
        print(f"il numero è uguale a 5")
        
x = int(input())
check_value(x)