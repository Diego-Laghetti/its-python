class Pagamento:
    _importo: float

    def __init__(self):
        self._importo = 0.0

    def get_importo(self):
        return self._importo

    def set_importo(self, _importo):
        self._importo = _importo

    def dettagliPagamento(self):
        print(f"Importo del pagamento: {self._importo:.2f} euro")

class PagamentoContanti(Pagamento):
    def __init__(self, _importo):
        super().__init__()
        self._importo = _importo  

    def dettagliPagamento(self):
        print(f"Pagamento in contanti di: {self._importo:.2f} euro")

    def inPezziDa(self):
        importo_centesimi = self._importo * 100
        tagli:list = [50000, 200000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
        soldi_usati = {}
        for n in tagli:
            if n <= importo_centesimi:
                while (importo_centesimi - n) >= 0:
                    importo_centesimi -= n
                    if n in soldi_usati:
                        soldi_usati[n] += 1
                    else: 
                        soldi_usati[n] = 1
        for key, value in soldi_usati.items():
            if key > 500:
                if value == 1:
                    print(f"{value} banconota da {key / 100} euri")
                else:
                    print(f"{value} banconote da {key / 100} euri")
            else:
                if value == 1:
                    print(f"{value} moneta da {key / 100} euri")
                else:
                    print(f"{value} monete da {key / 100} euri")


class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, _importo: float, nome: str, cognome: str, data: str, numerocarta: int):
        super().__init__()
        self._importo = _importo
        self.nome = nome
        self.cognome = cognome
        self.data = data
        self.numerocarta = numerocarta

    def dettagliPagamento(self):
        print(f"Pagamento di {self._importo} effettuato con la carta di credito")
        print(f"Nome sulla carta: {self.nome} {self.cognome}")
        print(f"Data di scadenza: {self.data}")
        print(f"Numero della carta: {self.numerocarta}")


p = PagamentoContanti(250.53)
p.dettagliPagamento()
p.inPezziDa()

p1= PagamentoCartaDiCredito(1407.69, "gigi", "buffon", "08/06", 1234123412341234)
p1.dettagliPagamento()

