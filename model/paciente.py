from model.abstractPessoa import Pessoa
from datetime import date,datetime


class Paciente(Pessoa):

    def __init__(self, nome, cpf, telefone, data_nascimento):
        super().__init__(nome, cpf, telefone)
        self.__data_nascimento = data_nascimento

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        if isinstance(nova_data, date):
            self.__data_nascimento = nova_data
        else:
            raise ValueError(
                "A data de nascimento deve ser um objeto date."
            )

    def verificar_idade(self):
        hoje = date.today()
        idade = (
            hoje.year - self.__data_nascimento.year
            - (
                (hoje.month, hoje.day)
                < (self.__data_nascimento.month,
                   self.__data_nascimento.day)
            )
        )
        return idade

    def verificar_tipo(self):
        return "Paciente"
    
    def __str__(self):
        if isinstance(self.data_nascimento, str):
            data_formatada = self.data_nascimento
        else:
            data_formatada = self.data_nascimento.strftime("%d/%m/%Y")
            
        return f"Nome: {self.nome} | CPF: {self.cpf} | Tel: {self.telefone} | Nasc: {data_formatada}"