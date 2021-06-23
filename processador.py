from boleto import Boleto
from fatura import Fatura

class Processador:
    def __init__(self):
        self.fatura = Fatura('21-06-2021', 1109.65 , 'Breno Froes')
        self.processar()
        self.boletos
        self.verificaPagamento()

    def processar(self):
        self.boletos = [Boleto(239921113, 200.43, '15-02-2021'), Boleto(312331122, 200.32, '18-03-2021'), Boleto(211238812, 399.65, '30-04-2021')]
        ## Comentar próxima linha para uma fatura não paga
        self.boletos.append(Boleto(239921113, 310.12, '12-05-2021'))

    def verificaPagamento(self):
        valorSomaBoletos = 0
        valores = str((self.boletos))
        valoresNovos = valores.replace("[", "")
        valoresNovos2 = valoresNovos.replace("]", "")

        for boleto in self.boletos:
            valorSomaBoletos = valorSomaBoletos + boleto.valorPago

        if valorSomaBoletos >= self.fatura.valorTotal:
            print('Fatura de ' + str(self.fatura.valorTotal) + ' com ' + str(
                len(self.boletos)) + ' boletos no valor de ' +
                  valoresNovos2 + ': fatura marcada como PAGA, e ' + str(
                len(self.boletos)) + ' pagamentos do tipo ' + str(
                self.boletos[0].instanciaPagamento().tipoPagamento) + ' criados.')
            return True
        else:
            print('Fatura de ' + str(self.fatura.valorTotal) + ' com ' + str(
                len(self.boletos)) + ' boletos no valor de ' +
                  valoresNovos2 + ': fatura não marcada como PAGA, e ' + str(
                len(self.boletos)) + ' pagamentos do tipo ' + str(
                self.boletos[0].instanciaPagamento().tipoPagamento) + ' criados.')
            return False

processador = Processador()