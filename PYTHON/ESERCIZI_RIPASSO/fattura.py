from dottore import Dottore
from paziente import Paziente

class Fattura:
    def __init__(self, patient:list[Paziente], doctor: Dottore):
        if doctor.isAValidDoctor():
            self.fatture = int(len(patient))
            self.salary = 0
            self.doctor = doctor
            self.patient = patient
        else:
            self.patient = None
            self.doctor = None
            self.fatture = None
            self.salary = None
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        self.salary = self.doctor.getParcel() * int(len(self.patient))
        return self.salary
    
    def getFatture(self):
        return self.fatture == int(len(self.patient))
    
    def addPatient(self, newPatient):
        self.patient.append(newPatient)
        self.getFatture()
        self.getSalary() 
        print(f"Alla lista del Dottor {self.doctor.last_name} è stato aggiunto il paziente {self._cod_id}")

    def removePatient(self, _cod_id):
        for p in self.patient:
            if p.getIdCode() == _cod_id:
                self.patient.remove(p)
        self.getFatture()
        self.getSalary()
        print(f"Alla lista del Dottor {self.last_name} è stato rimosso il paziente {self._cod_id}")

