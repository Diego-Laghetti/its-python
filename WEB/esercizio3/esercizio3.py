#esercizio3
def recursiveFactorial(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * recursiveFactorial(n-1)
    
print(recursiveFactorial(5))