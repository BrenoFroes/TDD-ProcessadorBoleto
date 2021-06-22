import unittest
from fatura import Fatura
from boleto import Boleto

class Processador(unittest.TestCase):

    def teste_inicial(self):
        fatura = Fatura(0, '', '')
        boleto = Boleto(0, 0, '')
        if boleto == fatura:
            return True
        return False