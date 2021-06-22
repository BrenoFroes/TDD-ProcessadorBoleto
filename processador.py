from boleto import Boleto
from fatura import Fatura
import unittest

class Processador(unittest.TestCase):
    def teste_processador(self):
        boletos = []
        boletos.append(Boleto(0, 0, '', ''))
        boletos.append(Boleto(0, 0, '', ''))
        boletos.append(Boleto(0, 0, '', ''))

    def teste_inicial(self):
        fatura = Fatura(0, '', '')
        boleto = Boleto(0, 0, '', '')
        if boleto == fatura:
            return True
        return False