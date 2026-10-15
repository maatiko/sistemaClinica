from datetime import datetime

from exception.excecoes import (
    CampoObrigatorio,
    HorarioInvalido,
)


class Clinica:

    def __init__(
        self,
        nome,
        localizacao,
        descricao,
        horario_abertura,
        horario_fechamento,
    ):
        self.nome = nome
        self.localizacao = localizacao
        self.descricao = descricao
        self.horario_abertura = horario_abertura
        self.horario_fechamento = horario_fechamento

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str) or len(novo_nome.strip()) < 2:
            raise CampoObrigatorio(
                "O nome da clínica deve ter pelo menos dois caracteres."
            )
        self.__nome = novo_nome.strip()

    @property
    def localizacao(self):
        return self.__localizacao

    @localizacao.setter
    def localizacao(self, nova_localizacao):
        if (
            not isinstance(nova_localizacao, str)
            or len(nova_localizacao.strip()) < 2
        ):
            raise CampoObrigatorio("A localização da clínica é obrigatória.")
        self.__localizacao = nova_localizacao.strip()

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        if (
            not isinstance(nova_descricao, str)
            or len(nova_descricao.strip()) < 2
        ):
            raise CampoObrigatorio("A descrição da clínica é obrigatória.")
        self.__descricao = nova_descricao.strip()

    @property
    def horario_abertura(self):
        return self.__horario_abertura

    @horario_abertura.setter
    def horario_abertura(self, novo_horario):
        if not isinstance(novo_horario, str):
            raise HorarioInvalido("O horário de abertura deve ser HH:MM.")

        try:
            datetime.strptime(novo_horario, "%H:%M")
        except ValueError:
            raise HorarioInvalido(
                "Horário de abertura inválido. Use HH:MM."
            )

        self.__horario_abertura = novo_horario

    @property
    def horario_fechamento(self):
        return self.__horario_fechamento

    @horario_fechamento.setter
    def horario_fechamento(self, novo_horario):
        if not isinstance(novo_horario, str):
            raise HorarioInvalido("O horário de fechamento deve ser HH:MM.")

        try:
            datetime.strptime(novo_horario, "%H:%M")
        except ValueError:
            raise HorarioInvalido(
                "Horário de fechamento inválido. Use HH:MM."
            )

        self.__horario_fechamento = novo_horario

    def __str__(self):
        return (
            f"Clínica: {self.nome} | Cidade: {self.localizacao} | "
            f"Descrição: {self.descricao} | "
            f"Abertura: {self.horario_abertura} | "
            f"Fechamento: {self.horario_fechamento}"
        )