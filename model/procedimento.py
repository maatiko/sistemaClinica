class Procedimento:
    def __init__(self,descricao,custo,profissional):
        self.__descricao = descricao
        self.__custo = custo
        self.__profissional = profissional

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        if nova_descricao is not None and len(nova_descricao) >1:
            self.__descricao = nova_descricao

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, novo_custo):
        if novo_custo is not None and novo_custo >1:
            self.__custo = novo_custo

    @property
    def profissional(self):
        return self.__profissional

    def __str__(self):
        return f"Procedimento: {self.__descricao} | Custo: R$ {self.__custo:.2f} | Profissional: {self.__profissional.nome}"       