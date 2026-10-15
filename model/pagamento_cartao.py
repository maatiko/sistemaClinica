from .pagamento import Pagamento
from exception.excecoes import DadosCartaoInvalidos


class PagamentoCartao(Pagamento):

    modalidade = "Cartão de crédito"

    def __init__(
        self,
        consulta,
        paciente,
        valor,
        data_pagamento,
        numero_cartao,
        bandeira,
    ):
        super().__init__(
            consulta,
            paciente,
            valor,
            data_pagamento,
        )

        numero = "".join(
            c for c in str(numero_cartao) if c.isdigit()
        )

        if not 13 <= len(numero) <= 19:
            raise DadosCartaoInvalidos(
                "O número do cartão deve conter entre 13 e 19 dígitos."
            )

        if not isinstance(bandeira, str) or not bandeira.strip():
            raise DadosCartaoInvalidos(
                "A bandeira do cartão é obrigatória."
            )

        self.numero_cartao = numero
        self.bandeira = bandeira.strip()