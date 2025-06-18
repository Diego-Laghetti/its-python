def leggi_intero_positivo(msg):
    while True:
        n = float(input("Inserisci un numero intero positivo: "))
        if n.is_integer() and n >= 0:
            return int(n)
        else:
            print("Errore: inserisci un numero intero positivo (>=0).")

x = leggi_intero_positivo("Inserisci un numero intero positivo x: ")
while x == 0:
    print("x deve essere maggiore di 0")
    x = leggi_intero_positivo("Inserisci un numero intero positivo x: ")
lista1 = []
cont = 0
somma = 0
pos = -1
i = 0

while True:
    n = leggi_intero_positivo("Inserisci un numero intero positivo (0 per terminare): ")
    if n == 0:
        break
    lista1.append(n)
    i += 1
    if n == x:
        cont += 1
        if pos == -1:
            pos = i
    else:
        somma += n

print("Sequenza inserita:", lista1)

if cont == 1:
    print(f"Il numero {x} compare 1 sola volta nella sequenza.")
else:
    print(f"Il numero {x} compare {cont} volte nella sequenza.")

if pos != -1:
    print(f"Il numero {x} compare per la prima volta in posizione {pos} nella sequenza.")
else:
    print(f"Il numero {x} non compare nella sequenza.")

print(f"La somma dei valori della sequenza diversi da {x} è {somma}.")






