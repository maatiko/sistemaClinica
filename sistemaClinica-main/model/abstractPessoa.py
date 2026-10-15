from abc import ABC, abstractmethod


class Pessoa(ABC):

    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if not isinstance(novo_nome, str) or len(novo_nome.strip()) < 2:
            raise ValueError("Nome inválido.")
        self.__nome = novo_nome.strip()

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        if not isinstance(novo_cpf, str) or len(novo_cpf.strip()) < 2:
            raise ValueError("CPF inválido.")
        self.__cpf = novo_cpf.strip()

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        if (
            not isinstance(novo_telefone, str)
            or len(novo_telefone.strip()) < 2
        ):
            raise ValueError("Telefone inválido.")
        self.__telefone = novo_telefone.strip()

    @abstractmethod
    def verificar_tipo(self):
        pass