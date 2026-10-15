from exception.excecoes import (
    CampoObrigatorio,
    ValorInvalido,
)


class Procedimento:

    def __init__(self, descricao, custo, profissional):
        self.descricao = descricao
        self.custo = custo
        self.profissional = profissional

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nova_descricao):
        if not isinstance(nova_descricao, str) or len(nova_descricao.strip()) < 2:
            raise CampoObrigatorio(
                "A descrição do procedimento deve ter pelo menos dois caracteres."
            )

        self.__descricao = nova_descricao.strip()

    @property
    def custo(self):
        return self.__custo

    @custo.setter
    def custo(self, novo_custo):
        try:
            novo_custo = float(novo_custo)
        except (TypeError, ValueError):
            raise ValorInvalido(
                "O custo do procedimento deve ser numérico."
            )

        if novo_custo <= 0:
            raise ValorInvalido(
                "O custo do procedimento deve ser maior que zero."
            )

        self.__custo = novo_custo

    @property
    def profissional(self):
        return self.__profissional

    @profissional.setter
    def profissional(self, novo_profissional):
        if novo_profissional is None:
            raise CampoObrigatorio(
                "O profissional responsável é obrigatório."
            )

        self.__profissional = novo_profissional

    def __str__(self):
        return (
            f"Procedimento: {self.descricao} | "
            f"Custo: R$ {self.custo:.2f} | "
            f"Profissional: {self.profissional.nome}"
        )