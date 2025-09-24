from persona import Persona

class Paziente(Persona):
    def __init__(self, first_name, last_name, _cod_id:str):
        super().__init__(first_name, last_name)
        self._cod_id = _cod_id

    def setIdCode(self, _cod_id):
        self._cod_id = _cod_id

    def getIdCode(self):
        return self._cod_id
    
    def pazienteInfo(self):
        print(f"Paziente: {self.first_name} {self.last_name}\n ID: {self._cod_id}")
