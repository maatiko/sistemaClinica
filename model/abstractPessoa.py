from abc import ABC,abstractmethod

class Pessoa(ABC):

    @abstractmethod
    def __init__(self,nome,cpf,telefone):
        self.__nome = nome
        self.__cpf = cpf
        self.__telefone = telefone

    @abstractmethod
    @property
    def nome(self):
        return self.__nome
    
    @abstractmethod
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome,str) and len(novo_nome) > 1:
            self.__nome = novo_nome

    @abstractmethod
    @property
    def cpf(self):
        return self.__cpf
    
    @abstractmethod
    @cpf.setter
    def cpf(self, novo_cpf):
        if isinstance(novo_cpf,str) and len(novo_cpf) > 1:
            self.__cpf = novo_cpf

    @abstractmethod
    @property
    def telefone(self):
        return self.__telefone
    
    @abstractmethod
    @telefone.setter
    def telefone(self, novo_telefone):
        if isinstance(novo_telefone,str) and len(novo_telefone) > 1:
            self.__telefone = novo_telefone