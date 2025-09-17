from enum import *
from typing import Any
from typing import Self
from enum import *
import re

class RealGEZ(float):

    def __new__(cls, x:int|float|bool|str):
        n:float =  super().__new__(x)

        if n >= 0:
            return n
        
class IntGEZ(int):
    def __new__(cls, x:int|float|bool|str):
        n:int =  super().__new__(x)

        if n >= 0:
            return n
        
        raise ValueError("Il valore non può essere minore di 0")
    
class RealGZ(float):

    def __new__(cls, x:int|float|bool|str):
        n:float =  super().__new__(x)

        if n > 0:
            return n
        
class Url(str):
    def __new__(cls, url: str) -> Self:
        pattern = r"^https?:\/\/[\w.-]+\.[a-z]{2,}.*$"
        
        if re.fullmatch(pattern, url):
            return url

        else:
            ValueError("Errore")

class Condizione(StrEnum):
    Usato_buone_condizioni = auto()
    Usato_ottime_condizioni = auto()
    Usato_accettabili_condizioni = auto()
    Usato_pessime_condizioni = auto()

        