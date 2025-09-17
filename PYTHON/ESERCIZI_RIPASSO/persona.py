'''### CLASSE: Persona

Creare un file chiamato "persona.py". In tale file, definire una classe chiamata Persona. Tale classe deve avere due attributi privati 
di tipo String, uno per il nome ed uno per il cognome, ed un attributo privato di tipo int per l'età.
- La classe Persona deve avere i seguenti metodi:

    init(first_name, last_name). Tale metodo, deve verificare che first_name, last_name siano stringhe; in caso negativo, impostare a None
     l'attributo che non risulta essere una stringa, stampando un messaggio di errore, ad esempio, "Il nome inserito non è una stringa!"
    . Se first_name e last_name sono due stringhe, assegnare 0 all'attributo relativo all'età di una persona; se first_name e last_name 
    non sono due stringhe, allora assegnare None all'età.
    setName(first_name): consente di impostare il nome di una persona, modificando il valore del relativo attributo. Il valore viene 
    modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio "Il nome 
    inserito non è una stringa!".
    setLastName(last_name): consente di impostare il cognome di una persona, modificando il valore del relativo attributo. Il valore 
    viene modificato se e solo se viene passata al metodo una stringa. In caso contrario, stampare un messaggio di errore, ad esempio 
    "Il cognome inserito non è una stringa!".
    setAge(age): consente di impostare l'età di una persona, modificando il valore del relativo attributo. Il valore viene modificato se 
    e solo se viene passato al metodo un numero intero. In caso contrario, stampare un messaggio di errore, ad esempio "L'età deve essere 
    un numero intero!".
    getName(): consente di ritornare il nome di una persona.
    getLastname(): consente di ritornare il cognome di una persona.
    getAge(): consente di ritornare l'età di una persona.
    greet(): stampa il seguente saluto "Ciao, sono {nome} {cognome}! Ho {età} anni!"

'''
class Persona:
    def __init__(self, nome, cognome):
        if isinstance(nome, str):
            self.nome = nome
        else:
            print("Il nome deve essere una stringa")
            self.nome = None

        if isinstance(cognome, str):
            self.cognome = cognome
        else:
            print("Il cognome deve essere una stringa")
            self.cognome = None

        if self.nome is not None and self.cognome is not None:
            self.eta = 0
        else:
            self.eta = None

    def SetNome(self, nome):
        if isinstance(nome, str):
            self.nome = nome
        else:
            print("Il nome inserito non è una stringa. Il nome non è stato modificato.")

    def SetCognome(self, cognome):
        if isinstance(cognome, str):
            self.cognome = cognome
        else:
            print("Il cognome inserito non è una stringa. Il cognome non è stato modificato.")

    def SetEta(self, eta):
        if isinstance(eta, int):
            self.eta = eta
        else:
            print("L'età inserito non è un'intero. L'età non è stata modificata.")

    def GetNome(self):
        return self.nome
    
    def GetCognome(self):
        return self.cognome
    
    def GetEta(self):
        return self.eta
    
    def greet(self):
        print(f"Ciao, sono {self.nome} {self.cognome}! Ho {self.eta} anni!")




    

    