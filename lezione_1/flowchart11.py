#flowchart11
liberi = 20
while True:
    opzione = str(input("Inserisci opzione: "))
    match opzione:
        case "prenota":
            if liberi > 0:
                liberi -= 1
            else:
                print("Non ci sono posti disponibili")
        case "libera":
            if liberi < 20:
                liberi += 1
            else:
                print("Tutti i posti sono già disponibili")
        case "visualizza":
            print("liberi", liberi)
            pinko= 20 - liberi
            print("occupati", pinko)
        case "esci":
            break
        case _:
            continue

