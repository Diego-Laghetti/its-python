from enum import StrEnum, auto
from typing import Any, Self
import re

from enum import StrEnum, auto
from typing import Any, Self

class Genere(StrEnum):
    uomo = auto()
    donna = auto()

print("__name__ all'interno di mytypes.py: " + __name__)

class Voto(int):
    def __new__(cls, v: int) -> Self:
        if v < 18 or v > 31:
            raise ValueError(f"Il voto v={v} deve essere tra 18 e 31")
        return int.__new__(cls, v)

if __name__ == '__main__':
    print("Test di mytypes.py\n========\n")
    print(Genere.uomo)
    print(type(Genere.uomo))
    print(Genere.donna)

class Indirizzo:
    def __init__(self, via: str, civico: str, cap: str) -> None:
        if not isinstance(via, str) or not isinstance(civico, str) or not (isinstance(cap, str) and len(cap) == 5 and cap.isdigit()):
            raise TypeError("Dati non validi per un indirizzo")
        self.via = via
        self.civico = civico
        self.cap = cap

    def get_via(self) -> str: return self.via
    def get_civico(self) -> str: return self.civico
    def get_cap(self) -> str: return self.cap

    def __hash__(self) -> int:
        return hash((self.via, self.civico, self.cap))

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Indirizzo) and (self.via, self.civico, self.cap) == (other.via, other.civico, other.cap)

class Email:
    c: str = "@"
    d: list = [".it", ".com"]

    def __init__(self, c: str, i: str, f: str, d: list, dominio: str) -> None:
        if not isinstance(i, str) or c != "@" or not isinstance(f, str) or dominio not in d:
            raise TypeError("Non va bene")
        self.c = c
        self.i = i
        self.f = f
        self.d = d
        self.dominio = dominio

    def get_c(self) -> str: return self.c
    def get_i(self) -> str: return self.i
    def get_f(self) -> str: return self.f
    def get_dominio(self) -> str: return self.dominio

    def __hash__(self) -> int:
        return hash((self.c, self.i, self.f, self.dominio))

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Email) and (self.c, self.i, self.f, self.dominio) == (other.c, other.i, other.f, other.dominio)

class Telefono:
    def __init__(self, numero: str) -> None:
        if not (len(numero) == 10 and numero.isdigit()):
            raise TypeError("Errore caratteri")
        self.numero = numero

    def get_numero(self) -> str:
        return self.numero

    def __hash__(self) -> int:
        return hash(self.numero)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Telefono) and self.numero == other.numero

class CF(str):
    def __new__(cls, val: str) -> Self:
        if not val.isalnum() or len(val) != 16:
            raise ValueError("CF non valido")
        return str.__new__(cls, val)
    
'''
class Genere(StrEnum):
    uomo = auto()
    donna = auto()

print("__name__ all'interno di mytypes.py: " + __name__)

class Voto(int):
    def __new__(cls, v: int) -> Self:
        if v < 18 or v > 31:
            raise ValueError(f"Il voto v={v} deve essere tra 18 e 31")
        return int.__new__(cls, v)

if __name__ == '__main__':
    print("Test di mytypes.py\n========\n")
    print(Genere.uomo)
    print(type(Genere.uomo))
    print(Genere.donna)

class Indirizzo:
    def __init__(self, via: str, civico: str, cap: str) -> None:
        if not isinstance(via, str) or not isinstance(civico, str) or not (isinstance(cap, str) and len(cap) == 5 and cap.isdigit()):
            raise TypeError("Dati non validi per un indirizzo")
        self.via = via
        self.civico = civico
        self.cap = cap

    def get_via(self) -> str: return self.via
    def get_civico(self) -> str: return self.civico
    def get_cap(self) -> str: return self.cap

    def __hash__(self) -> int:
        return hash((self.via, self.civico, self.cap))

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Indirizzo) and (self.via, self.civico, self.cap) == (other.via, other.civico, other.cap)

class Email(str):
    EMAIL_REGEX = re.compile(r'^[\w\.-]+@[\w\.-]+\.(it|com)$')

    def __new__(cls, val: str) -> Self:
        if not Email.EMAIL_REGEX.match(val):
            raise ValueError(f"Email non valida: {val}")
        return str.__new__(cls, val)

    def get_email(self) -> str:
        return str(self)

class Telefono:
    TELEFONO_REGEX = re.compile(r'^\d{10}$')

    def __init__(self, numero: str) -> None:
        if not isinstance(numero, str) or not Telefono.TELEFONO_REGEX.fullmatch(numero):
            raise TypeError("Numero di telefono non valido (deve essere di 10 cifre)")
        self.numero = numero

    def get_numero(self) -> str:
        return self.numero

    def __hash__(self) -> int:
        return hash(self.numero)

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Telefono) and self.numero == other.numero

class CF(str):
    CF_REGEX = re.compile(r'^[A-Z]{6}[0-9]{2}[A-Z][0-9]{2}[A-Z][0-9]{3}[A-Z]$')

    def __new__(cls, val: str) -> Self:
        if not isinstance(val, str) or not CF.CF_REGEX.fullmatch(val.upper()):
            raise ValueError("CF non valido")
        return str.__new__(cls, val.upper())'''




    

