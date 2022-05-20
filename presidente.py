from funcionario import Funcionario
from autenticavel import Autemticavel
class Presidente(Funcionario, Autenticavel):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def bonificacao(self):
        return 2000

    def autemtica(self, valor):
        if self._senha == valor + '123':
            return True
        else:
            return False