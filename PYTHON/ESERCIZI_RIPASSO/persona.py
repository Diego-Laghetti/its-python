class Persona:
    def __init__(self, first_name:str, last_name:str):
        if not isinstance(first_name, str):
            first_name = None
            print("Il nome inserito non è una stringa!")
        if (isinstance(first_name, str) and isinstance(last_name, str)):
            age = 0
        if (not isinstance(first_name, str) and not isinstance(last_name, str)):
            age = None
        else:
            self.first_name = first_name
            self.last_name = last_name 
    
    def setName(self, name):
        if not isinstance(name, str):
            print("Il nome inserito non è una stringa!")
        else:
            self.first_name = name 

    def setLast_name(self, Last_name):
        if not isinstance(Last_name, str):
            print("Il cognome inserito non è una stringa!")
        else:
            self.last_name = Last_name 

    def setAge(self, eta):
        if not isinstance(eta, int):
            print("L'età inserita non è un int!")
        else:
            self.age = eta
    
    def getName(self):
        return self.first_name
    
    def getLast_name(self):
        return self.last_name
    
    def getAge(self):
        return self.age
    
    def greet(self):
        print(f"Ciao, sono {self.first_name} {self.last_name}! Ho {self.age} anni!")


