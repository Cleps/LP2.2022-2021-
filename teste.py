#from funcionario import Funcionario
from diretor import Diretor
from presidente import Presidente
from secretaria import Secretaria

func = Diretor("nome", 123123213, 1234, 123)
dir = Presidente('nomee',12334123,1234)
print(func._nome)
print(dir._nome)

sec = Secretaria('nomedela', 123123, 123123)

print(sec._nome)