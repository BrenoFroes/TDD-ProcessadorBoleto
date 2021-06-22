import unittest
from boleto import Boleto
from fatura import Fatura

class Pagamento(unittest.TestCase):

    def __init__(self, valorPago, data, tipoPagamento):
        self.valorPago = valorPago
        self.data = data
        self.tipoPagamento = tipoPagamento


