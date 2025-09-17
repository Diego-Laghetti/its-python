from Privato import *
from bid import *

class bid_ut:

    class _link:
        _privato: Privato #immutabile
        _bid: Bid #immutabile non noto alla nascita

        def __init__(self, privato: Privato, bid = Bid):
            self._privato = privato
            self._bid = bid

        def get_privato(self) -> Privato:
            return self._privato
        
        def get_bid(self) -> Bid:
            return self._bid
