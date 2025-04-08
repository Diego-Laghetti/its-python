#esercizio2
def compoundInterest(m: float, t: int) -> float:
    if t == 0:
        return m
    else: 
        return (compoundInterest(m * 1.005, t-1))
    
print(compoundInterest(3, 1))