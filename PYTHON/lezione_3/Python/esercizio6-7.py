#esercizio6-7
persona1: dict={"nome":"luca", "cognome":"taggiasco", "citta":"roma", "eta": 19}
persona2: dict={"nome":"diego", "cognome":"laghetti", "citta":"roma", "eta": 19}
persona3: dict={"nome":"claudio", "cognome":"benigni", "citta":"roma", "eta": 19}

people = [persona1, persona2, persona3]

for i in people:
    print(f"Nome: {i['nome']}")
    print(f"Cognome: {i['cognome']}")
    print(f"Citta: {i['citta']}")
    print(f"Eta: {i['eta']}")