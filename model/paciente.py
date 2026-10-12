from abstractPessoa import Pessoa
from datetime import date
class Paciente(Pessoa):

    def __init__(self, nome, cpf, telefone,data_nascimento):
        super().__init__(nome, cpf, telefone)
        self.__data_nascimento = data_nascimento

    def verificar_idade(self):
        hoje = date.today()
        idade = hoje.year - self.__data_nascimento.year - ((hoje.month, hoje.day) < (self.__data_nascimento.month, self.__data_nascimento.day))
        return idade