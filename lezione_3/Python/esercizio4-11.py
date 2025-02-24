#esercizio4-11
pizze:list= ["Margherita", "Boscaiola", "Bufala"]

for pizza in pizze:
    print(f"Mi piace la pizza:{pizza}\n")
    
print ("MI PIACE TANTIISSIO LA PIZZA !!!!")

friend_pizzas= pizze[:]                                                
print(f"La copia della lista {pizze} e':\n{friend_pizzas}")

pizze.append("Capricciosa")

friend_pizzas.append("Napoli")
print("Le mie pizze preferite sono:")
for pizza in pizze:
    print(pizza)
print("Le pizze preferite del mio amico sono:")
for pizza in friend_pizzas:
    print(pizza)