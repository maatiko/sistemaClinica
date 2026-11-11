from .pagamento import Pagamento


class PagamentoCartao(Pagamento):
    def __init__(
        self,
        consulta,
        valor_pago,
        numero_cartao,
        bandeira,
        parcelas:int = 1,
        data_pagamento = None,
        modalidade: str = "credito",
        
    ):
        numero_cartao = str(numero_cartao).strip() if numero_cartao is not None else ""
        if not numero_cartao:
            raise ValueError("O número do cartão deve ser informado.")

        bandeira = str(bandeira).strip() if bandeira is not None else ""
        if not bandeira:
            raise ValueError("A bandeira do cartão deve ser informada.")

        if isinstance(parcelas, bool) or not isinstance(parcelas, int) or parcelas <= 0:
            raise ValueError("O número de parcelas deve ser um inteiro maior que zero.")

        modalidades = {
            "credito": "crédito",
            "crédito": "crédito",
            "debito": "débito",
            "débito": "débito",
        }
        modalidade_normalizada = (
            str(modalidade).strip().casefold() if modalidade is not None else ""
        )
        if modalidade_normalizada not in modalidades:
            raise ValueError("A modalidade deve ser crédito ou débito.")

        super().__init__(
            consulta,
            valor_pago,
            data_pagamento,
            permite_pagamento_apos_atendimento=(
                modalidade_normalizada in {"credito", "crédito"} and parcelas > 1
            ),
        )
        self.__numero_cartao = numero_cartao
        self.__bandeira = bandeira
        self.__parcelas = parcelas
        self.__modalidade = modalidades[modalidade_normalizada]
    
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

    def descricao_detalhada(self) -> str:
        desc = f"Cartão de {self.__modalidade.capitalize()}"
        if self.__modalidade.lower() == "credito" or self.__modalidade.lower() == "crédito":
            desc += f" em {self.__parcelas}x"
        return desc