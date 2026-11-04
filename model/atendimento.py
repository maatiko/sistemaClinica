from .clinica import Clinica
from .profissional import Profissional
from .paciente import Paciente
from .tipo_atendimento import TipoAtendimento
class Atendimento:

    def __init__(self,clinica: Clinica,paciente: Paciente,profissional: Profissional,tipo: TipoAtendimento,data: str,horario_inicio: str,horario_fim: str,id_atendimento: int):
        self.__id_atendimento = id_atendimento
        self.__clinica = clinica
        self.__paciente = paciente
        self.__profissional = profissional
        self.__tipo = tipo
        self.__data = data
        self.__horario = horario_inicio
        self.__horario_fim = horario_fim
        self.__procedimentos=[]

    @property
    def id_atendimento(self):
        return self.__id_atendimento

    @property
    def paciente(self):
        return self.__paciente

    @property
    def clinica(self):
        return self.__clinica

    @property
    def profissional(self):
        return self.__profissional

    @property
    def tipo(self):
        return self.__tipo

    @property
    def procedimentos(self):
        return self.__procedimentos
    
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
    def horario_fim(self):
        return self.__horario_fim

    @horario_fim.setter
    def horario_fim(self, novo_horario):
        if isinstance(novo_horario, str) and len(novo_horario) > 1:
            self.__horario_fim = novo_horario

    @property
    def valor_base(self):
        return self.__tipo.valor

    @property
    def valor_total(self):
        custo_procedimentos = sum(p.custo for p in self.__procedimentos)
        return self.__tipo.valor + custo_procedimentos
    
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
        return (f"Atendimento #{self.id_atendimento} | "
                f"dia {self.data} das {self.horario} às {self.horario_fim} | "
                f"Paciente: {self.paciente.nome} | "
                f"Valor Total: R$ {self.valor_total:.2f} "
                f"({len(self.__procedimentos)} procedimentos adicionais)")