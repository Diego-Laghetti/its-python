#flowchart9
nome = str(input("Inserisci nome: "))
vendite = int(input("Inserisci vendite: "))
max_nome= nome
max=vendite
min_nome= nome
min = vendite
cont = 0
for i in range (19):
    new_nome = str(input("Inserisci nuovo nome: "))
    new_vendite = int(input("Inserisci nuove vendite: "))
    if new_vendite > max:
        max_nome = new_nome
        max = new_vendite
    elif new_vendite < min:
        min_nome = new_nome
        min = new_vendite
print(f"La persona con più vendite è {max_nome} con {max} vendite")
print(f"La persona con meno vendite è {min_nome} con {min} vendite")