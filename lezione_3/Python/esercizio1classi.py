#esercizio1classi
'''1. Copy the code and print the age of
bob (using the dot notation)
2. Create an if-statement that prints
the name of the oldest of the two
Persons
3. Create three other Persons. Make
a list called people with all 5
Persons.
4. Make a loop that finds and prints
the youngest person’s name'''


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

#1
print(bob.name)

#2
if bob.age > alice.age:
    print(bob.age)
else:
    print(alice.age)

#3
diego = Person("Diego L.", 20)
luca = Person("Luca T.", 19)
alessio = Person("Alessio R.", 21)
people =  [diego, luca, alessio, alice, bob]

#4
min_age= people[0]
for i in people:
    if i.age < min_age.age:
        min_age = i
print(f"Il più giovane è: {min_age.name} {min_age.age}")
