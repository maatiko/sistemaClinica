from .pagamento import Pagamento
from ..exception.excecoes import DadosPixInvalidos


class PagamentoPix(Pagamento):

    modalidade = "PIX"

    def __init__(
        self,
        consulta,
        paciente,
        valor,
        data_pagamento,
        cpf_pix,
    ):
        super().__init__(
            consulta,
            paciente,
            valor,
            data_pagamento,
        )

        if not isinstance(cpf_pix, str):
            raise DadosPixInvalidos(
                "O CPF do pagador no PIX é obrigatório."
            )

        cpf = "".join(c for c in cpf_pix if c.isdigit())

        if len(cpf) != 11:
            raise DadosPixInvalidos(
                "O CPF do pagador no PIX deve conter 11 dígitos."
            )

        self.cpf_pix = cpf