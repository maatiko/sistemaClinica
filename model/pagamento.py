from datetime import date

from .excecoes import (
    DataPagamentoInvalida,
    ValorInvalido,
    CampoObrigatorio,
)


class Pagamento:

    modalidade = "Genérico"

    def __init__(
        self,
        consulta,
        paciente,
        valor,
        data_pagamento,
    ):
        if consulta is None or paciente is None:
            raise CampoObrigatorio(
                "Consulta e paciente são obrigatórios para o pagamento."
            )

        try:
            valor = float(valor)
        except (TypeError, ValueError):
            raise ValorInvalido(
                "O valor pago deve ser numérico."
            )

        if valor <= 0:
            raise ValorInvalido(
                "O valor pago deve ser maior que zero."
            )

        if isinstance(data_pagamento, str):
            try:
                data_pagamento = date.fromisoformat(data_pagamento)
            except ValueError:
                raise DataPagamentoInvalida(
                    "Data de pagamento inválida. Use AAAA-MM-DD."
                )

        if not isinstance(data_pagamento, date):
            raise DataPagamentoInvalida(
                "Data de pagamento inválida."
            )

        if data_pagamento > consulta.data:
            raise DataPagamentoInvalida(
                "O pagamento deve ser realizado até a data do atendimento."
            )

        self.consulta = consulta
        self.paciente = paciente
        self.valor = valor
        self.data_pagamento = data_pagamento

    def __str__(self):
        return (
            f"{self.data_pagamento.isoformat()} | "
            f"{self.modalidade} | {self.paciente.nome} | "
            f"R$ {self.valor:.2f}"
        )