import random

class Creatura:
    def __init__(self, nome: str):
        self.setNome(nome)

    def setNome(self, nome):
        if isinstance(nome, str):  
            self.__nome = nome
        else:
            self.__nome = "Creatura Generica"

    def getNome(self):
        return self.__nome

    def __str__(self) -> str:
        return f"Creatura: {self.__nome}"
    
class Alieno(Creatura):
    def __init__(self, nome):
        super().__init__(nome)
        self.__setMatricola()
        self.__setMunizioni()
        if nome != "Robot-":
            print("Attenzione! Tutti gli Alieni devono avere il nome 'Robot' seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            nome = "Robot-"
        self.setNome(str(nome + str(self.getMatricola())))
    
    def __setMatricola(self):
        self.__matricola = random.randint(10000, 90000)

    def __setMunizioni(self):
        self.__munizioni = [i**2 for i in range(15)] 

    def getMatricola(self):
        return self.__matricola

    def getMunizioni(self):
        return self.__munizioni

    def __str__(self):
        return f"Alieno: {self.getNome()}"
    
class Mostro(Creatura):
    def __init__(self, nome, urlo_vittoria, gemito_sconfitta):
        super().__init__(nome)
        self.__setVittoria(urlo_vittoria)
        self.__setSconfitta(gemito_sconfitta)
        self.__setAssalto()

    def __setVittoria(self, urlo_vittoria: str):
        if not isinstance(urlo_vittoria, str):
            self.__urlo_vittoria = "GRAAAHHH"
        self.__urlo_vittoria = urlo_vittoria


    def __setSconfitta(self, gemito_sconfitta: str):
        if not isinstance(gemito_sconfitta, str):
            self.__gemito_sconfitta = "Uuurghhh"
        self.__gemito_sconfitta = gemito_sconfitta

    def __setAssalto(self):
        pool_number = list (i for i in range(1, 101))
        self.__assalto = random.sample(pool_number, 15)

    def getAssalto(self):
        return self.__assalto

    def getVittoria(self):
        return self.__urlo_vittoria
    
    def getSconfitta(self):
        return self.__gemito_sconfitta
    
    
    def __str__(self) -> str:
        nome_alternato = ""
        for p, c in enumerate(self.getNome()):
            if p % 2 == 0:
                nome_alternato += c.lower()
            else:
                nome_alternato += c.upper()
        return f"Mostro: {nome_alternato}"
    
def pariUguali(a: list[int], b: list[int]) -> list:
    for x, y in zip(a, b):
        if x < 0 and y < 0:
            print("Errore")
    c: list = []
    for x, y in zip(a, b):
        if x % 2 == 0 and y % 2 == 0:
            c.append(1)
        else:
            c.append(0)
    return c

def combattimento(a: Alieno, m: Mostro): 
    if not isinstance (a, Alieno) or not isinstance (m, Mostro):
        print("Errore")
        return None
    
    c = pariUguali(a.getMunizioni(), m.getAssalto())

    cont = 0
    for i in c:
        if i == 1:
            cont += 1
    if cont >= 4:
        print (f"{m.getVittoria()}\n" * 3)
        return m
    else:
        print (m.getSconfitta())
        return a
        
def proclamaVincitore(c: Creatura):
    if isinstance(c, Alieno):
        print("Hanno vinto gli alieni!")
    if isinstance(c, Mostro):
        print("Hanno vinto i mostri!")

    linea = str(c)
    larghezza = len(linea) + 10
    altezza = 5
    
    for i in range(altezza):
        if i == 0 or i == altezza - 1:
            print('*' * larghezza)
        elif i == 2:
            spazi_sinistra = (larghezza - len(linea) - 2) // 2
            spazi_destra = larghezza - len(linea) - spazi_sinistra - 2
            print("*" + " " * spazi_sinistra + linea + " " * spazi_destra + "*")
        else:
            print("*" + " " * (larghezza - 2) + "*")

def main():
    alieno = Alieno("Robot-")
    mostro = Mostro("Diego", "GRAAAHHH", "Uuurghhh")

    print(alieno)
    print("Munizioni:", alieno.getMunizioni(), "\n")

    print(mostro)
    print("Assalto:", mostro.getAssalto(), "\n")

    vincitore = combattimento(alieno, mostro)
    proclamaVincitore(vincitore)

main()

    
    

        




        







