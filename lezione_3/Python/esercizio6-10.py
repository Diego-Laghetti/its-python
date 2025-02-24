#esercizio6-10
numeri = {"Diego": [17, 9, 69],
        "Claudio": [8, 77, 97],
        "Luca": [16, 3, 69],
        "Davide": [2, 17, 88],
        "God": [1, 6, 19]}


for person, numbers in numeri.items():
    print(person)
    for number in numbers:
        print(number)