#esercizio5-9
elenco= ["Diego", "Luca", "Andrea", "Alessio","Davide"]

for nomi in elenco:
    if nomi=="Admin":
        print(f"Ciao {nomi} un saluto speciale a te")
        
    else:
        print(f"Benvenuto {nomi}")
        
for index in range (len(elenco)):
    elenco.pop()
if len(elenco)==0:
    print("la tua lista e' vuota, dobbiamo trovare alcuni utenti")