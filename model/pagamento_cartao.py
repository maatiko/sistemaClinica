from model.pagamento import Pagamento
from exception.excecoes import DadosCartaoInvalidos


class PagamentoCartao(Pagamento):
    def __init__(
        self,
        consulta,
        valor_pago,
        numero_cartao,
        bandeira,
        parcelas:int = 1,
        data_pagamento = None
        
    ):
        super().__init__(
            consulta,
            valor_pago,
            data_pagamento
        )
        self.__numero_cartao = str(numero_cartao)
        self.__bandeira = str(bandeira)
        self.__parcelas = parcelas
    
    @property
    def numero_cartao(self):
        return self.__numero_cartao

    @property
    def bandeira(self):
        return self.__bandeira

    @property
    def parcelas(self):
        return self.__parcelas
    @property
    def modalidade(self):
        return self.__modalidade

    @property
    def parcelas(self):
        return self.__parcelas

    def descricao_detalhada(self) -> str:
        desc = f"Cartão de {self.__modalidade.capitalize()}"
        if self.__modalidade.lower() == "credito" or self.__modalidade.lower() == "crédito":
            desc += f" em {self.__parcelas}x"
        return desc