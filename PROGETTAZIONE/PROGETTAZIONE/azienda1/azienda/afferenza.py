from custom_types import *
from impiegato import *
from dipartimento import *
from typing import Any
from datetime import datetime

class afferenza:

    class _link:
        _impiegato:Impiegato #sempre immutabile e noto alla nascita
        _dipartimento:Dipartimento # sempre immutabile e noto alla nascita
        _data_afferenza: datetime # sempre immutabile e noto alla nascita

    def __init__(self, impiegato :Impiegato, dipartimento :Dipartimento, data_afferenza: datetime) -> None:
        self._impiegato:Impiegato = impiegato
        self._dipartimento:Dipartimento = dipartimento
        self._data_afferenza: datetime = data_afferenza

    def get_impiegato(self) -> Impiegato:
        return self._impiegato
    
    def get_dipartimento(self) -> Progetto:
        return self._dipartimento 
    
    def get_data_afferenza(self) -> datetime:
        return self._data_afferenza
    
    def __hash__(self) -> int:
        return hash((self.get_impiegato(), self.get_dipartimento(), self.get_data_afferenza()))
     
    def __eq__(self, other: Any) -> bool:
        if type(self) != type(other) or hash(self != hash(other)):
            return False
        
        return (self.get_impiegato(), self.get_dipartimento(), self.get_data_afferenza()) == (other.impiegato(), other.progetto(), other.data_afferenza())