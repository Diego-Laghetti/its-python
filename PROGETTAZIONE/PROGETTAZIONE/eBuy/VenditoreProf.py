from Utente import *

class VenditoreProf(Utente):
    _vetrina: Url
    def __init__(self, username, registrazione, vetrina: Url):
        super().__init__(username, registrazione)
        self.set_vetrina(vetrina)

    def set_vetrina(self, vetrina) -> None:
        self._vetrina = vetrina
    
    def get_vetrina(self) -> Url:
        return self._vetrina
    
