class TipoAtendimento:
    def __init__(self, nome:str,descricao:str,valor:float):
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome, str) and novo_nome.strip():
            self.__nome = novo_nome
        else:
            raise ValueError("Isso não funciona como nome de Tipo Atendimento.")

    @property
    def descricao(self):
            return self.__descricao
    
    @descricao.setter
    def descricao(self, nova_descricao):
        if isinstance(nova_descricao, str) and nova_descricao.strip():
            self.__descricao = nova_descricao
        else:
            raise ValueError("Isso não funciona como descrição de Tipo Atendimento.")

    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self, novo_valor):
        if isinstance(novo_valor, (int, float)) and novo_valor >= 0:
            self.__valor = float(novo_valor)
        else:
            raise ValueError("O valor do Tipo de Atendimento deve ser numérico e não negativo.")

    def __str__(self):
        return f"{self.__nome} | {self.__descricao} | R$ {self.__valor:.2f}"
