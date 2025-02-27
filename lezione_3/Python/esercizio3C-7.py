#esercizio3C-7
dado=1
testa=0
croce=0
perct=0
percc=0
while dado <= 8:
    print(f"Il {dado} lancio della moneta effettuato!!!!")
    x = str(input("Cosa è uscito? "))
    if x == "t":
        print("E' uscito testa")
        testa+=1
    else:
        print("E' uscito croce")
        croce+=1
    dado+=1
print(f"testa è uscito {testa} volte")
print(f"croce è uscito {croce} volte")
perct=testa/8*100
percc=croce/8*100
print(f"la percentuale delle volte in cui è uscita testa è {perct}%")
print(f"la percentuale delle volte in cui è uscita croce è {percc}%")

