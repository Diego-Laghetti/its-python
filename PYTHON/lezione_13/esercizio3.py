#esercizio3
def sumInRange(a:int, b:int) -> int:
    if a > b:
        c:int = a
        a = b
        b = c
    sum = 0
    while b>=a:
        sum += b
        b = b - 1
    print(sum)
    return int(sum)
    
sumInRange(5, 10)