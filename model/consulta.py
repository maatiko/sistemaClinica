from .clinica import Clinica
from .profissional import Profissional
from .paciente import Paciente
from datetime import date

class Consulta:

    def __init__(self, clinica : Clinica,paciente:Paciente,profissional:Profissional,data:str,horario:str,tipo_atendimento:str,valor:float):
        #mais tarde checar se está recebendo a classe ou não
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__data = data
        self.__horario = horario
        self.__tipo_atendimento = tipo_atendimento
        self.__valor = valor

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
    def tipo_atendimento(self):
        return self.__tipo_atendimento
    
    @tipo_atendimento.setter
    def tipo_atendimento(self, novo_tipo):
        if isinstance(novo_tipo,str) and len(novo_tipo) > 1:
            self.__tipo_atendimento = novo_tipo

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, novo_valor):
        if isinstance(novo_valor,str) and novo_valor > 0:
            self.__valor = novo_valor