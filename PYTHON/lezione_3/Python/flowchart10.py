#flowchart10
eta = int (input("Inserisci età: "))
if eta >= 18 and eta <= 65:
    print("Puoi partecipare all'attività")
elif eta > 18:
    print("Non puoi partecipare all'attività perchè non hai raggiunto l'età minima rischiesta")
else:
    print("Non puoi partecipare all'attività perchè hai superato l'età massima consentita")
