class Pagamento:
    def __init__(self) -> None:
        self.__pagamento = None
    def set_pagamento(self, pagamento):
        self.__pagamento = pagamento
    def getpagamento(self):
        return self.__pagamento
    def dettagliPagamento(self):
        print(f'importo pagamento: {self.getpagamento():.2f}')

class PagamentoContanti(Pagamento):
    def __init__(self, importo) -> None:
        super().__init__()
        self.set_pagamento(importo)

    def dettagliPagamento(self):
        print(f'pagamento in contanti: {self.getpagamento():.2f}')
    def inPezziDa(self):
        importo =  self.getpagamento()
        banconote = [500, 200, 100, 50, 20, 10, 5]
        monete = [2, 1, 0.50, 0.20, 0.10, 0.05, 0.01]
        for banconota in banconote:
            num_banconote = int(importo / banconota)
            if num_banconote > 0:
                print(f'{num_banconote} banconota da {banconota} euro')
                importo -= num_banconote * banconota
        
        for moneta in monete:
            num_monete = int(importo / moneta)
            if num_monete > 0:
                print(f'{num_monete} moneta da {moneta} euro')
                importo -= num_monete * moneta

class PagamentoCartaDiCredito(Pagamento):
    def __init__(self, nome, data_di_scadenza, numero_carta) -> None:
        super().__init__()
        self.nome = nome
        self.data_di_scadenza = data_di_scadenza
        self.numero_carta = numero_carta










