from datetime import date, datetime

from model.abstractPessoa import Pessoa
from exception.excecoes import DataInvalida


class Paciente(Pessoa):

    def __init__(self, nome, cpf, telefone, data_nascimento):
        super().__init__(nome, cpf, telefone)
        self.data_nascimento = data_nascimento

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @data_nascimento.setter
    def data_nascimento(self, nova_data):
        if isinstance(nova_data, datetime):
            nova_data = nova_data.date()

        if isinstance(nova_data, str):
            try:
                nova_data = datetime.strptime(
                    nova_data, "%d/%m/%Y"
                ).date()
            except ValueError:
                raise DataInvalida(
                    "Data de nascimento inválida. Use DD/MM/AAAA."
                )

        if not isinstance(nova_data, date):
            raise DataInvalida(
                "A data de nascimento deve ser uma data válida."
            )

        if nova_data > date.today():
            raise DataInvalida(
                "A data de nascimento não pode estar no futuro."
            )

        self.__data_nascimento = nova_data

    def verificar_idade(self):
        hoje = date.today()
        nascimento = self.__data_nascimento

        return (
            hoje.year - nascimento.year
            - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
        )

    def verificar_tipo(self):
        return "Paciente"

    def __str__(self):
        data_formatada = self.data_nascimento.strftime("%d/%m/%Y")
        return (
            f"Nome: {self.nome} | CPF: {self.cpf} | "
            f"Tel: {self.telefone} | Nasc: {data_formatada}"
        )