from pagamento import Pagamento

class Boleto:
    def __init__(self, codigoBoleto, valorPago, data):
        self.codigoBoleto = codigoBoleto
        self.valorPago = valorPago
        self.data = data
        self.instanciaPagamento()

    def instanciaPagamento(self):
        pagamento = Pagamento(self.valorPago, self.data, 'Boleto')
        return pagamento

    def __repr__(self):
        return str(self.valorPago)