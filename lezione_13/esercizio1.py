#esercizio1
def countdown(n:int)->None:
    if n < 0:
        print("error")
    while n >= 0:
        print(n)
        n -= 1

countdown(5)
countdown(-5)




