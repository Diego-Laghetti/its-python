from asta import Asta
from bid import *

class asta_bid:
     
     class _link:
        _asta: Asta
        _bid: Bid #immutabile, non noto alla nascita

        def __init__(self, asta: Asta, bid: Bid):
            self._asta = asta
            self._bid = bid
        
        def get_asta(self) -> Asta:
            return self._asta

        def get_bid(self) -> Bid:
            return self._bid
