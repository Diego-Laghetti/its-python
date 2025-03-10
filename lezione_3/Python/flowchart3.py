#flowchart3
max_posti= 100
nome_corso=str(input("Inserire nome corso: "))
while True:
    opzione = str(input("Inserisci opzione: "))
    match opzione:
        case "iscrivi":
            if max_posti > 0:
                max_posti -= 1
            else:
                print("Non ci sono posti disponibili")
        case "visualizza":
            print(max_posti)
            print(100-max_posti)
        case "elimina":
            corso=str(input("Inserire nome corso: "))
        case "esci":
            break
        case _:
            continue