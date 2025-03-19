#esercizio2
def sum(n:int) -> int:
    if n < 0:
        print("error")
    else:
        sum:int = 0
        while n:
            sum += n
            n -= 1
        print(sum)
        
sum(5)
sum(-5)