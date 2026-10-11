class Clinica:

    def __init__(self,nome,localizacao,descricao,horario_funcionamento):
        self.__nome = nome
        self.__localizacao = localizacao
        self.__descricao = descricao
        self.__horario_fucionamento : horario_funcionamento

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome,str) and len(novo_nome) > 1:
            self.__nome = novo_nome

    @property
    def localizacao(self):
        return self.__localizacao
    
    @localizacao.setter
    def localizacao(self, nova_localizacao):
        if isinstance(nova_localizacao,str) and len(nova_localizacao) > 1:
            self.__localizacao = nova_localizacao

    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, nova_descricao):
        if isinstance(nova_descricao,str) and len(nova_descricao) > 1:
            self.__descricao = nova_descricao

    @property
    def horario_funcionamento(self):
        return self.__registro
    
    @horario_funcionamento.setter
    def horario_funcionamento(self, novo_horario_funcionamento):
        if isinstance(novo_horario_funcionamento,str) and len(novo_horario_funcionamento) > 1:
            self.__registro = novo_horario_funcionamento
