#flowchart10
r = int(input("Inserisci reddito: "))
m = int(input("Inserisci media: "))
if r < 20000 and m > 27:
    print("Borsa di studio approvata")
else:
    print("Borsa di studio rifiutata.(Motivo: reddito o media insufficiente)")