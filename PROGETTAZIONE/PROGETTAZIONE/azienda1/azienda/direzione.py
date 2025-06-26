from custom_types import *
from impiegato import *
from dipartimento import *
from typing import Any

class direzione:

    class _link:
        _impiegato:Impiegato #sempre immutabile e noto alla nascita
        _dipartimento:Dipartimento #sempre immutabile e noto alla nascita

    def __init__(self, impiegato :Impiegato, dipartimento :Dipartimento) -> None:
        self._impiegato:Impiegato = impiegato
        self._dipartimento:Dipartimento = dipartimento

    def get_impiegato(self) -> Impiegato:
        return self._impiegato
    
    def get_dipartimento(self) -> Progetto:
        return self._dipartimento 
    
    def __hash__(self) -> int:
        return hash((self.get_impiegato(), self.get_dipartimento()))
     
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self != hash(other)):
            return False
        
        return (self.get_impiegato(), self.get_dipartimento()) == (other.impiegato(), other.progetto())