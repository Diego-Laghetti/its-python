#esercizio5-6
età= int(input("Inserisci l'eta della persona: \n")) 

if età < 2:
    print("La persona è un neonato.")
elif età >= 2 and età < 4:
    print("La persona è un bambino.")
elif età >= 4 and età < 13:
    print("La persona è un bambino.")
elif età >= 13 and età < 20:
    print("La persona è un adolescente.")
elif età >= 20 and età < 65:
    print("La persona è un adulto.")
else:
    print("La persona è un anziano.")