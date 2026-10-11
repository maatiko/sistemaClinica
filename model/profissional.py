from abstractPessoa import Pessoa

class Profissional(Pessoa):

    def __init__(self, nome, cpf, telefone,especialidade,registro):
        super().__init__(nome, cpf, telefone)
        self.__especialidade = especialidade
        self.__registro = registro

    @property
    def especialidade(self):
        return self.__especialidade
    
    @especialidade.setter
    def especialidade(self, nova_especialidade):
        if isinstance(nova_especialidade,str) and len(nova_especialidade) > 1:
            self.__especialidade = nova_especialidade

    @property
    def registro(self):
        return self.__registro
    
    @registro.setter
    def registro(self, novo_registro):
        if isinstance(novo_registro,str) and len(novo_registro) > 1:
            self.__registro = novo_registro
