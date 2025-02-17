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
print (f"Aura {favorite[1]} ")

#esercizio3-4
guest = ["Lionel Messi", "Totti Gol", "Ciro immobile"]

print (f"ciao {guest[0]} che ne dici di andare a cena fuori? ")
print (f"ciao {guest[1]} che ne dici di andare a cena fuori? ")
print (f"ciao {guest[2]} che ne dici di andare a cena fuori? ")

#esercizio3-5
print (f"{guest[0]} non fa in tempo")

guest[0]= "Mattia Zaccagni"

print (f"ciao {guest[0]} che ne dici di andare a cena fuori? ")
print (f"ciao {guest[1]} che ne dici di andare a cena fuori? ")
print (f"ciao {guest[2]} che ne dici di andare a cena fuori? ")

#esercizio3-6
print ("ho trovato un tavolo più grande, inviterò altre persone")

guest.insert(0, "Mario Gila")
guest.insert(2, "Gustav Isaksen")
guest.append("Miroslav Klose")

print (f"ciao {guest[0]} che ne dici di andare a cena fuori insieme ai tuoi compagni di squadra? ")
print (f"ciao {guest[1]} che ne dici di andare a cena fuori insieme ai tuoi compagni di squadra? ")
print (f"ciao {guest[2]} che ne dici di andare a cena fuori insieme ai tuoi compagni di squadra? ")
print (f"ciao {guest[3]} che ne dici di andare a cena fuori insieme ai tuoi compagni di squadra? ")
print (f"ciao {guest[4]} che ne dici di andare a cena fuori insieme ai tuoi compagni di squadra? ")
print (f"ciao {guest[5]} che ne dici di andare a cena fuori insieme ai tuoi compagni di squadra? ")

#esercizio3-7
name=guest.pop(5)
print ("posso far venire solo due di voi per un equivoco")

print (f" scusa {name} ma non è più disponibile il tavolo, faremo un'altra volta")

name=guest.pop(4)

print (f" scusa {name}ma non è più disponibile il tavolo, faremo un'altra volta")
name=guest.pop(3)

print (f" scusa {name}ma non è più disponibile il tavolo, faremo un'altra volta")

name=guest.pop(2)

print (f" scusa {name}ma non è più disponibile il tavolo, faremo un'altra volta")

print (f" {guest[0]} e {guest[1]} tranquilli, siete ancora invitati")

del guest

#esercizio3-8
places = ["Amogus","Ubuntu","SSLazio","Skibidi","Sigma"]
print (places)

places = sorted(places)
print (places)

places = sorted(places, reverse=True)
print (places)

places.reverse()
print (places)

places.reverse()
print (places)

places.sort()
print (places)

places.sort(reverse=True)
print (places)

#esercizio3-9
print (len(favorite))