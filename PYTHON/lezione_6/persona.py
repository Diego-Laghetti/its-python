#persona.py

#costruttore
class Persona:

    def __init__(self, name:str, lastname:str, age: int):
        self.name = name
        self.lastname = lastname
        self.age =age 

#funzione nella classe Persona che visualizza in output i dati di una persona

    def displayData(self) -> None:
        print(f"nome: {self.name}\ncognome: {self.lastname}\netà: {self.age}")