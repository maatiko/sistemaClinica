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
        if isinstance(novo_nome, str) and len(novo_nome.strip()) > 1:
            self.__nome = novo_nome.strip()
        else:
            raise ValueError("Nome inválido.")

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        if isinstance(novo_cpf, str) and len(novo_cpf.strip()) > 1:
            self.__cpf = novo_cpf.strip()
        else:
            raise ValueError("CPF inválido.")

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        if isinstance(novo_telefone, str) and len(novo_telefone.strip()) > 1:
            self.__telefone = novo_telefone.strip()
        else:
            raise ValueError("Telefone inválido.")

    @abstractmethod
    def verificar_tipo(self):
        pass