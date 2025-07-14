'''
Scrivere un programma in Python che legga dall’utente una serie di nomi di persona (stringhe). L'inserimento dei nomi deve terminare quando l’utente inserisce un nome già inserito in precedenza, oppure sono stati inseriti 30 nomi distinti. Inoltre, si deve porre il vincolo che ciascun nome sia una stringa di lunghezza inferiore a 20 caratteri e che non venga inserita una stringa vuota.

Al termine dell'inserimento, il programma deve:
- stampare quanti nomi sono stati inseriti in totale;
- stampare il nome più lungo tra quelli inseriti;
- stampare la lunghezza del nome più lungo.

Se ci sono più nomi con la stessa lunghezza massima, puoi scegliere uno qualsiasi tra quelli più lunghi.

Esempio:
Inserisci un nome: Dora
Inserisci un nome: Marcella
Inserisci un nome: Teresa
Inserisci un nome: Valentina
Inserisci un nome: Dora
 
Hai inserito 4 nomi distinti.
Il più lungo è Valentina con 9 caratteri.
'''
def main():
    nomi = []
    max_nomi = 30

    while True:
        nome = input("Inserisci un nome: ")

        if nome in nomi:
            break

        nomi.append(nome)

        if len(nomi) == max_nomi:
            break

    if len(nomi) == 0:
        print("Non sono stati inseriti nomi validi.")
        return

    nome_piu_lungo = nomi[0]
    for n in nomi:
        if len(n) > len(nome_piu_lungo):
            nome_piu_lungo = n

    print(f"Hai inserito {len(nomi)} nomi distinti.")
    print(f"Il più lungo è {nome_piu_lungo} con {len(nome_piu_lungo)} caratteri.")

if __name__ == "__main__":
    main()




