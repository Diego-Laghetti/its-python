#esercizio3classi
class Animal:
    def __init__(self, nome, gambe, abitat):
        self.nome=nome
        self.gambe=gambe
        self.abitat=abitat
#4 aggiungere gambe
    def setGambe(self, nuove_gambe):
        self.gambe=nuove_gambe
#5 return il numero di gambe
    def getGambe(self):
        return self.gambe
#6 funzione che printa tutti gli attributi degli animali
    def printInfo(self):
        print(f"nome: {self.nome}")
        print(f"gambe: {self.gambe}")
        print(f"abitat: {self.abitat}")

#1 creare istanze
dog= Animal("Dog", 4, "Terra")
shark= Animal("Shark", 0, "Acqua")
#2 printare il nome degli animali
print(dog.nome)
print(shark.nome)
#3 cambiare il numero di ngambe ad un animale
shark.gambe = 1
print(shark.gambe)
#4
shark.setGambe(0)
print(shark.gambe)
#5
print(dog.getGambe())
print(shark.getGambe())
#6
dog.printInfo()
shark.printInfo()

