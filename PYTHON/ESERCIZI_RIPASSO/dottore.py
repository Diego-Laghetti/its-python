from persona import Persona

class Dottore(Persona):
    def __init__(self, first_name, last_name, specialization:str, parcel:float):
        super().__init__(first_name, last_name)
        self.specializzazione = specialization
        self.parcel = parcel 

        if not isinstance(self.specializzazione, str):
            self.specialization = None
        
        if not isinstance(self.parcel, float):
            print("La parcella inserita non è un float!")

    def setSpecialization(self, specializzazione):
        if not isinstance(specializzazione, str):
            print("La specializzazione inserita non è una stringa!")
        else: 
            self.specialization = specializzazione

    def setParcel(self, parcella):
        if not isinstance(parcella, float):
            print("La parcella inserita non è un float!")

    def getSpecialization(self):
        return self.specialization
    
    def getParcel(self):
        return self.parcel
    
    def isAValidDoctor(self) -> bool:
        if self.age > 30:
            print(f"Doctor {self.first_name} {self.last_name} is valid!")
            return True
        
        else: 
            print(f"Doctor {self.first_name} {self.last_name} is not valid!")
            return False
    
    def greet(self):
        print("Ciao!", end= " ")

    def doctorGreet(self):
        self.greet()
        print(f"Sono un medico {self.specializzazione}")


