#esercizio2-3
Name = "Diego"
print (f" Ciao {Name} come va?")

#esercizio2-4
print (Name.upper())
print (Name.lower())
print (Name.title())

#esercizio2-5
print ("Uomini forti destini forti, uomini deboli destini deboli; Cit. Playdido")

#esercizio2-6
famous_person = "Playdido"
message = "Uomini forti destini forti, uomini deboli destini deboli"

print (famous_person,message) 

#esercizio3-1
friends = ["Diego","Davide"]

print (friends[0])
print (friends[1])

#esercizio3-2
print (f"{friends[0]} come va?")
print (f"{friends[1]} come va?")

#esercizio3-3
favorite = ["Ferrari","Porsche"]

print (f"{favorite[0]}, una delle macchine con i migliori motori ")
print (f"la miglior macchina del pianeta terra e' {favorite[1]} ")

#esercizio3-4
guest = ["Lionel Messi", "Totti Gol", "Ciro immobile"]

print (f"ciao {guest[0]} che ne dici di andare a cena fuori? ")
print (f"ciao {guest[1]} che ne dici di andare a cena fuori? ")
print (f"ciao {guest[2]} che ne dici di andare a cena fuori? ")

#esercizio3-5
print (f"{guest[0]} non fa in tempo")

guest = ["Mattia Zaccagni", " Totti Gol", "Ciro immobile"]

print (f"ciao {guest[0]} che ne dici di andare a cena fuori? ")
print (f"ciao {guest[1]} che ne dici di andare a cena fuori? ")
print (f"ciao {guest[2]} che ne dici di andare a cena fuori? ")

#esercizio3-6
print (f" {guest} ho trovato un tavolo più grande, inviterò altre persone")

guest.insert(3, "Mario Gila")
guest.insert(4, "Gustav Isaksen")
guest.append("Miroslav Klose")

print (f"ciao {guest[0]} che ne dici di andare a cena fuori insieme ai tuoi compagni di squadra? ")
print (f"ciao {guest[1]} che ne dici di andare a cena fuori insieme ai tuoi compagni di squadra? ")
print (f"ciao {guest[2]} che ne dici di andare a cena fuori insieme ai tuoi compagni di squadra? ")
print (f"ciao {guest[3]} che ne dici di andare a cena fuori insieme ai tuoi compagni di squadra? ")
print (f"ciao {guest[4]} che ne dici di andare a cena fuori insieme ai tuoi compagni di squadra? ")
print (f"ciao {guest[5]} che ne dici di andare a cena fuori insieme ai tuoi compagni di squadra? ")

#esercizio3-7
print ("posso far venire solo due di voi per un equivoco")

print (f" scusa {guest[5]} ma non è più disponibile il tavolo, faremo un'altra volta")
guest.pop(5)

print (f" scusa {guest[4]}ma non è più disponibile il tavolo, faremo un'altra volta")
guest.pop(4)

print (f" scusa {guest[3]}ma non è più disponibile il tavolo, faremo un'altra volta")
guest.pop(3)

print (f" scusa {guest[2]}ma non è più disponibile il tavolo, faremo un'altra volta")
guest.pop(2)

print (f" {guest[0]} e {guest[1]} traanquilli, siete ancora invitati")

del guest

#esercizio3-8
places = ["Amogus","Ubuntu","SSLazio","Skibidi","Sigma"]
print (places)

a_places = sorted(places)
print (a_places)
print (places)

b_places = sorted(places, reverse=True)
print (b_places)
print (places)

places.reverse()
print (places)

places.reverse()
print (places)

places.sort()
print (places)

places.sort()
print (places)

#esercizio3-9
print (len(favorite))
