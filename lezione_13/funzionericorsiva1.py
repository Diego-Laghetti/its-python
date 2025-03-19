#funzionericorsiva1
def countdown(n:int)->None:
    if n < 0:
        print("errore")
    elif n == 0:
        print(0)
    else:
        print(n)
        countdown(n-1)

countdown(0)
countdown(5)
countdown(-5)