#flowchart11_1
liberi = int(input("Inserire il numero di posti liberi: "))
p_liberi = liberi
while True:
    opzione = str(input("Inserisci opzione: "))
    match opzione:
        case "prenota":
            if liberi > 0:
                liberi -= 1
            else:
                print("Non ci sono posti disponibili")
        case "libera":
            if liberi < p_liberi:
                liberi += 1
            else:
                print("Tutti i posti sono già disponibili")
        case "visualizza":
            print("liberi", liberi)
            pinko= p_liberi - liberi
            print("occupati", pinko)
        case "esci":
            break
        case _:
            continue