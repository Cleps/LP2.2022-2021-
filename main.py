from conta import Conta
from banco import Banco
from emprestimo import Emprestimo

c1 = Conta(1, 'fulano', 1000, 123)
c2 = Conta(2, 'cicrano', 2000, 123)
c3 = Conta(3, 'carinha', 3000, 123)

bb = Banco()

bb.incluir_conta(c1)
bb.incluir_conta(c2)
bb.incluir_conta(c3)

c1.depositar(1000)
c1.sacar(500)

c2.depositar(1000)

bb.listar_contas()
bb.imprime_caixa()

e1 = Emprestimo(1000, 10, 0.1, c3)
for i in range(10):
    e1.pagar_parcela()
