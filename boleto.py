import unittest

class Boleto:
    def __init__(self, codigoBoleto, valorPago, data):
        self.codigoBoleto = codigoBoleto
        self.valorPago = valorPago
        self.data = data