from funcionario import Funcionario
from autenticavel import Autenticavel

class Gerente(Funcionario, Autenticavel):
    def __init__(self, nome, cpf, salario, senha):
        super().__init__(nome, cpf, salario)
        self._senha = senha

    #Método sobrescrito
    def bonificacao(self):
        return super().bonificacao() + 500

    def autentica(self, valor):
        if self._senha == valor:
            return True
        else:
            return False

