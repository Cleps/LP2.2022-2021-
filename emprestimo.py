class Emprestimo():
    def __init__(self, valor, parcelas, juros, conta):
        self._valor = valor
        self._parcelas = parcelas
        self._juros = juros
        self._conta = conta
        self._montante = self._valor + (self._valor*juros)
        self._valor_parcela = self._montante / self._parcelas
        conta.depositar(self._valor)

    def pagar_parcela(self):
        self._conta.sacar(self._valor_parcela)
        self._parcelas -= 1
        self._montante -= self._valor_parcela
        self.status()

    def status(self):
        print(f'---Situação do emprestimo---')
        print(f'Faltam {self._parcelas} parcelas de R${self._valor_parcela}')
        print(f'Falta pagar R${self._montante} no total')
        print(f'Seu saldo é de R$ {self._conta.saldo}')
        print('------------------------------------')