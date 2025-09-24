'''In un file chiamato "film.py", si definisca la classe Film che rappresenta un film preso a nolleggio. In tale classe, definire un codice identificativo (int) ed un
 titolo (string). Entrambi gli attributi sono da considerarsi privati.
 
- Definire i seguenti metodi:

    init(id, title): metodo costruttore.
    setID(id): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.d
    setTitle(title): che consente di impostare il codice identificativo del film, modificando il valore del relativo attributo.
    getID(): che consente di ritornare il valore del codice identificativo di un film.
    getTitle(): che consente di ritornare il valore del titolo di un film.
    isEqual(otherFilm): che ritorna true se il codice identificativo di due film è uguale.  
'''
class Film:
    _id: int
    _titolo: str

    def __init__(self, _id, _titolo):
        self._id = _id
        self._titolo = _titolo

    def setID(self, _id):
        self._id = _id

    def setTitle(self, _titolo):
        self._titolo = _titolo

    def getID(self):
        return self._id
    
    def getTitle(self):
        return self._titolo
    
    def isEqual(self, otherFilm: int):
        if self._id == otherFilm:
            return True

