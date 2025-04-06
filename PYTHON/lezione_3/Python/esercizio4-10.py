#esercizio4-10
numbers: list = list(range(1,10))
m = len(numbers)//2

print(f"I primi tre numeri della lista sono: {numbers[:3]}")
print(f"I  tre numeri in mezzo alla lista sono: {numbers[m-1:m+2]}")
print(f"Gli ultimi tre numeri della lista sono: {numbers[-3:]}")