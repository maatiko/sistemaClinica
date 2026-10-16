class Clinica:

    def __init__(self,nome,localizacao,descricao,horario_abertura,horario_fechamento):
        self.__nome = nome
        self.__localizacao = localizacao
        self.__descricao = descricao
        self.__horario_abertura = horario_abertura
        self.__horario_fechamento = horario_fechamento

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
    def horario_abertura(self):
        return self.__horario_abertura
    
    @horario_abertura.setter
    def horario_abertura(self, novo_horario_funcionamento):
        if isinstance(novo_horario_funcionamento,str) and len(novo_horario_funcionamento) > 1:
            self.__horario_abertura = novo_horario_funcionamento
        
    @property
    def horario_fechamento(self):
        return self.__horario_fechamento
    
    @horario_fechamento.setter
    def horario_fechamento(self, novo_horario_fechamento):
        if isinstance(novo_horario_fechamento,str) and len(novo_horario_fechamento) > 1:
            self.__horario_fechamento = novo_horario_fechamento

    def __str__(self):
        return f"Clínica: {self.__nome} | Cidade: {self.__localizacao} | Descrição: {self.__descricao} | Abertura: {self.__horario_abertura} | Fechamento: {self.__horario_fechamento}"