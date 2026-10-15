from model.abstractPessoa import Pessoa
from exception.excecoes import CampoObrigatorio


class Profissional(Pessoa):

    def __init__(self, nome, cpf, telefone, especialidade, registro):
        super().__init__(nome, cpf, telefone)
        self.especialidade = especialidade
        self.registro = registro

    @property
    def especialidade(self):
        return self.__especialidade

    @especialidade.setter
    def especialidade(self, nova_especialidade):
        if (
            not isinstance(nova_especialidade, str)
            or len(nova_especialidade.strip()) < 2
        ):
            raise CampoObrigatorio(
                "A especialidade deve ter pelo menos dois caracteres."
            )

        self.__especialidade = nova_especialidade.strip()

    @property
    def registro(self):
        return self.__registro

    @registro.setter
    def registro(self, novo_registro):
        if (
            not isinstance(novo_registro, str)
            or len(novo_registro.strip()) < 2
        ):
            raise CampoObrigatorio(
                "O registro profissional deve ter pelo menos dois caracteres."
            )

        self.__registro = novo_registro.strip()

    def verificar_tipo(self):
        return "Profissional"

    def __str__(self):
        return (
            f"Dr(a). {self.nome} | CRM/Registro: {self.registro} | "
            f"Especialidade: {self.especialidade}"
        )