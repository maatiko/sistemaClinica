from datetime import date, datetime, time

from model.clinica import Clinica
from model.profissional import Profissional
from model.paciente import Paciente
from exception.excecoes import (
    CampoObrigatorio,
    DataInvalida,
    HorarioInvalido,
    ValorInvalido,
)


class Consulta:

    def __init__(
        self,
        clinica: Clinica,
        paciente: Paciente,
        profissional: Profissional,
        tipo: str,
        data,
        horario,
        valor: float,
    ):
        if clinica is None or paciente is None or profissional is None:
            raise CampoObrigatorio(
                "Clínica, paciente e profissional são obrigatórios."
            )

        if not isinstance(tipo, str) or not tipo.strip():
            raise CampoObrigatorio("O tipo de consulta é obrigatório.")

        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__tipo = tipo.strip()
        self.data = data
        self.horario = horario
        self.valor_base = valor
        self.__procedimentos = []

    @property
    def clinica(self):
        return self.__clinica

    @property
    def paciente(self):
        return self.__paciente

    @property
    def profissional(self):
        return self.__profissional

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, novo_tipo):
        if not isinstance(novo_tipo, str) or not novo_tipo.strip():
            raise CampoObrigatorio("O tipo de consulta é obrigatório.")
        self.__tipo = novo_tipo.strip()

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, nova_data):
        if isinstance(nova_data, datetime):
            nova_data = nova_data.date()

        if isinstance(nova_data, str):
            try:
                nova_data = datetime.strptime(
                    nova_data, "%d/%m/%Y"
                ).date()
            except ValueError:
                raise DataInvalida(
                    "Data inválida. Use o formato DD/MM/AAAA."
                )

        if not isinstance(nova_data, date):
            raise DataInvalida("A data da consulta é inválida.")

        self.__data = nova_data

    @property
    def horario(self):
        return self.__horario

    @horario.setter
    def horario(self, novo_horario):
        if isinstance(novo_horario, str):
            try:
                novo_horario = datetime.strptime(
                    novo_horario, "%H:%M"
                ).time()
            except ValueError:
                raise HorarioInvalido(
                    "Horário inválido. Use o formato HH:MM."
                )

        if not isinstance(novo_horario, time):
            raise HorarioInvalido("O horário da consulta é inválido.")

        self.__horario = novo_horario

    @property
    def procedimentos(self):
        return self.__procedimentos

    @property
    def valor_base(self):
        return self.__valor_base

    @valor_base.setter
    def valor_base(self, novo_valor):
        try:
            novo_valor = float(novo_valor)
        except (TypeError, ValueError):
            raise ValorInvalido(
                "O valor da consulta deve ser numérico."
            )

        if novo_valor <= 0:
            raise ValorInvalido(
                "O valor da consulta deve ser maior que zero."
            )

        self.__valor_base = novo_valor

    @property
    def valor_total(self):
        custo_procedimentos = sum(
            procedimento.custo for procedimento in self.__procedimentos
        )
        return self.__valor_base + custo_procedimentos

    def adicionar_procedimento(self, procedimento_novo):
        if procedimento_novo is None:
            raise ValorInvalido("Procedimento inválido.")

        self.__procedimentos.append(procedimento_novo)

    def remover_procedimento(self, procedimento_remover):
        if procedimento_remover not in self.__procedimentos:
            raise ValorInvalido(
                "O procedimento informado não está associado a esta consulta."
            )

        self.__procedimentos.remove(procedimento_remover)

    def __str__(self):
        return (
            f"Consulta dia {self.data.strftime('%d/%m/%Y')} "
            f"às {self.horario.strftime('%H:%M')} | "
            f"Paciente: {self.paciente.nome} | "
            f"Valor Total: R$ {self.valor_total:.2f} "
            f"({len(self.__procedimentos)} procedimentos adicionais)"
        )