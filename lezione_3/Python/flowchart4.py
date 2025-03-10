#flowchart4
n_tutor = 10
attesa = 0
while True:
    studente=str(input("Leggi nome studente: "))
    if n_tutor>0:
        n_tutor = n_tutor -1
        print("Tutor assegnato con successo")
    else:
        attesa = attesa + 1
        print("Studente in attesa")
    if n_tutor == 0 and attesa > 50:
        break
    else:
        continue