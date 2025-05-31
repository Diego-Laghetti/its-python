#esercizio9_13
from random import randint

class Dice:
    def __init__(self, sides = 6) -> None:
        self.sides = sides
    
    def roll_dice(self) -> int:
        return randint(1, self.sides)
    
d6 = Dice()

result: list[int] = []
for roll in range(10):
    roll = d6.roll_dice()
    result.append(roll)
print(result)

d10 = Dice(sides = 10)

result: list[int] = []
for roll in range(10):
    roll = d10.roll_dice()
    result.append(roll)
print(result)

d20 = Dice(sides = 20)

result: list[int] = []
for roll in range(10):
    roll = d20.roll_dice()
    result.append(roll)
print(result)


