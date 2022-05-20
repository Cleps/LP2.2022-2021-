from funcionario import Funcionario

class Secretaria(Funcionario):
    def __init__(self, nome, cpf, salario):
        super().__init__(nome, cpf, salario)

    def bonificacao(self):
        return 0