from datetime import date, datetime
import math


class Pagamento:
    def __init__(
        self,
        consulta,
        valor_pago,
        data_pagamento,
        *,
        permite_pagamento_apos_atendimento: bool = False,
    ):
        try:
            valor_pago = float(valor_pago)
        except (TypeError, ValueError):
            raise ValueError("O valor pago deve ser um número válido.")

        if not math.isfinite(valor_pago) or valor_pago <= 0:
            raise ValueError("O valor pago deve ser maior que zero.")

        self.__consulta = consulta
        self.__valor_pago = valor_pago

        if data_pagamento is None:
            self.__data_pagamento = datetime.now()

        elif isinstance(data_pagamento, str):
            try:
                self.__data_pagamento = datetime.strptime(
                    data_pagamento, "%d/%m/%Y %H:%M"
                )
            except ValueError:
                try:
                    self.__data_pagamento = datetime.strptime(
                        data_pagamento, "%d/%m/%Y"
                    )
                except ValueError:
                    raise ValueError(
                        "Data de pagamento inválida. Use DD/MM/AAAA ou DD/MM/AAAA HH:MM."
                    )
        elif isinstance(data_pagamento, datetime):
            self.__data_pagamento = data_pagamento
        elif isinstance(data_pagamento, date):
            self.__data_pagamento = datetime.combine(data_pagamento, datetime.min.time())
        else:
            raise ValueError("A data do pagamento deve ser uma data válida.")

        data_atendimento = getattr(consulta, "data", None)
        if isinstance(data_atendimento, datetime):
            data_atendimento = data_atendimento.date()
        elif isinstance(data_atendimento, date):
            pass
        elif isinstance(data_atendimento, str):
            try:
                data_atendimento = datetime.strptime(
                    data_atendimento.strip(), "%d/%m/%Y"
                ).date()
            except ValueError:
                raise ValueError("A data do atendimento deve ser válida.")
        else:
            raise ValueError("O atendimento deve possuir uma data válida.")

        if (
            self.__data_pagamento.date() > data_atendimento
            and not permite_pagamento_apos_atendimento
        ):
            raise ValueError(
                "A data do pagamento não pode ser posterior à data do atendimento, "
                "exceto em pagamentos parcelados no crédito."
            )

    @property
    def consulta(self):
        return self.__consulta

    @property
    def paciente(self):
        if hasattr(self.__consulta, "paciente"):
            return self.__consulta.paciente
        return None

    @property
    def valor_pago(self):
        return self.__valor_pago

    @property
    def data_pagamento(self):
        return self.__data_pagamento

    def descricao_detalhada(self):
        pass