'''
Creare un file chiamato "paziente.py".
In tale file, creare una classe chiamata Paziente. Si derivi Paziente dalla classe Persona.

Un paziente ha un nome, un cognome, un età, definiti dalla classe Persona ed un codice identificativo (si usi il tipo String).
- Definire i seguenti metodi:

    costruttore della classe paziente, il quale richiede in input il codice identificativo, il quale deve essere un attributo privato.
    setIdCode(idCode): consente di impostare il codice identificativo del paziente.
    getidCode(): consente di ritornare il codice identificativo del paziente.
    patientInfo(): stampa in output le informazioni del paziente in questo modo:

        "Paziente: {nome} {cognome}
         ID: {codice identificativo}"
'''
from persona import Persona
class Paziente(Persona):
    def __init__(self, nome, cognome, idCode):
        super().__init__(nome, cognome)
        if isinstance(idCode, str):
            self._idCode = idCode
        else:
            self._idCode = None

    def SetIdCode(self,idCode):
        if isinstance(idCode, str):
            self._idCode = idCode
        else:
            print("Il codice identificativo inserito non è una stringa!")

    def GetIdCode(self):
        return self._idCode
    
    def PatientInfo(self):
        print(f"Paziente: {self.nome} {self.cognome}. ID: {self._idCode}")