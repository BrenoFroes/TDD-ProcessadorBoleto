import unittest
from boleto import Boleto

class Fatura:
    def __init__(self, valorTotal, data, nomeCliente):
        self.data = data
        self.valorTotal = valorTotal
        self.nomeCliente = nomeCliente
