import unittest
from boleto import Boleto
from fatura import Fatura

class Pagamento(unittest.TestCase):


    def teste_inicial(self):
        fatura = Fatura(0, '', '')
        boleto = Boleto(0, 0, '')
        if boleto == fatura:
            return True
        return False
