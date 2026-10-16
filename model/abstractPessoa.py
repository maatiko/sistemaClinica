from abc import ABC, abstractmethod
from exception.excecoes import DadosInvalidos, CampoObrigatorio


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
        if not isinstance(novo_nome, str) or not novo_nome.strip():
            raise CampoObrigatorio("O nome é obrigatório.")

        if (
            len(novo_nome.strip()) < 2
            or not any(letra.isalpha() for letra in novo_nome)
        ):
            raise DadosInvalidos(
                "Nome inválido. Digite um nome com letras."
            )

        self.__nome = novo_nome.strip()

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        if not isinstance(novo_cpf, str) or not novo_cpf.strip():
            raise CampoObrigatorio("O CPF é obrigatório.")

        if not novo_cpf.isdigit() or len(novo_cpf) != 11:
            raise DadosInvalidos(
                "CPF inválido. Digite os 11 números do CPF."
            )

        self.__cpf = novo_cpf.strip()

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        if (
            not isinstance(novo_telefone, str)
            or not novo_telefone.strip()
        ):
            raise CampoObrigatorio("O telefone é obrigatório.")

        if (
            not novo_telefone.isdigit()
            or len(novo_telefone) not in (10, 11)
        ):
            raise DadosInvalidos(
                "Telefone inválido. Digite o DDD e o número, "
                "apenas com números."
            )

        self.__telefone = novo_telefone.strip()

    @abstractmethod
    def verificar_tipo(self):
        pass
