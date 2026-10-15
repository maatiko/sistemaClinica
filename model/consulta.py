from .clinica import Clinica
from .profissional import Profissional
from .paciente import Paciente
from datetime import date

class Consulta:

    def __init__(self, clinica : Clinica,paciente:Paciente,profissional:Profissional,tipo:str, data:str,horario:str,valor:float):
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__tipo = tipo
        self.__data = data
        self.__horario = horario
        self.__valor_base = valor
        self.__procedimentos=[]

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, nova_data):
        if isinstance(nova_data,str) and len(nova_data) > 1:
            self.__data = nova_data

    @property
    def horario(self):
        return self.__horario
    
    @horario.setter
    def horario(self, novo_horario):
        if isinstance(novo_horario,str) and len(novo_horario) > 1:
            self.__horario = novo_horario

    @property
    def procedimentos(self):
        return self.__procedimentos
    
    @property
    def valor_base(self):
        return self.__valor_base
    
    @valor_base.setter
    def valor_base(self, novo_valor):
        if isinstance(novo_valor,str) and novo_valor > 0:
            self.__valor_base = novo_valor

    @property
    def valor_total(self):
        custo_procedimentos = sum(p.custo for p in self.__procedimentos)
        return self.__valor_base + custo_procedimentos
    
    def adicionar_procedimento(self,procedimento_novo):
        if procedimento_novo is None:
            raise ValueError("Procedimento inválido.")
        self.__procedimentos.append(procedimento_novo)

    def remover_procedimento(self,procedimento_remover):
        if procedimento_remover in self.__procedimentos:
            self.__procedimentos.remove(procedimento_remover)
        else:
            raise ValueError("O procedimento informado não está associado a esta consulta.")
    def __str__(self):
        return (f"Consulta dia {self.data} às {self.horario} | Paciente: {self.paciente.nome} | "
                f"Valor Total: R$ {self.valor_total:.2f} "
                f"({len(self.__procedimentos)} procedimentos adicionais)")