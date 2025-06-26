from custom_types import *
from impiegato import *
from progetto import *
from typing import Any

class Coinvolto:
    # questa è una class factory: non ha oggetti suoi
    # serve solo a creare oggetti di un'altra classe (in questo caso, di classe Link)
    @classmethod
    def add_link(cls, impiegato: Impiegato, progetto: Progetto) -> None:
        # crea il link (impiegato, progetto)
        l: __class__._link = __class__._link(impiegato, progetto) 
        return l
    
    def remove_link(cls, impiegato: Impiegato, progetto: Progetto) -> None:

    class _link:
        # ogni oggetto di questa class rappresenta un link di associazione Coinvolto
        # ovvero una coppia (Impiegato, Progetto)
        _impiegato: Impiegato
        _progetto: Progetto
        def __init__(self, impiegato: Impiegato, progetto: Progetto):
            self._impiegato=impiegato
            self._progetto=progetto

        def impiegato(self):
            return self._impiegato

        def progetto(self):
            return self._progetto