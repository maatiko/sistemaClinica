
from datetime import date, datetime
from abc import ABC, abstractmethod

from exception.excecoes import (
    DataPagamentoInvalida,
    ValorInvalido,
    CampoObrigatorio,
)

class Pagamento:
    def __init__(
        self,
        consulta,
        valor_pago,
        data_pagamento):
        if valor_pago <= 0 and valor_pago is not None:
                    raise ValueError("O valor pago deve ser maior que zero.")
        self.__consulta = consulta
        self.__valor_pago = valor_pago        
         
        if data_pagamento is None:
                self.__data_pagamento = datetime.now()
        elif isinstance(data_pagamento, str):
                try:
                    self.__data_pagamento = datetime.strptime(data_pagamento, "%d/%m/%Y %H:%M")
                except ValueError:
                    try:
                        self.__data_pagamento = datetime.strptime(data_pagamento, "%d/%m/%Y")
                    except ValueError:
                        self.__data_pagamento = datetime.now()
        else:
                self.__data_pagamento = data_pagamento
    def __validar_data_pagamento(self):
        if hasattr(self.__consulta, 'data'):
            data_c = self.__consulta.data
            if isinstance(data_c, str):
                try:
                    data_c = datetime.strptime(data_c, "%d/%m/%Y").date()
                except ValueError:
                    data_c = None
            elif isinstance(data_c, datetime):
                data_c = data_c.date()

            data_p = self.__data_pagamento.date() if isinstance(self.__data_pagamento, datetime) else self.__data_pagamento

            if data_c and isinstance(data_p, date) and data_p > data_c:
                raise ValueError(f"Data de pagamento inválida! O pagamento ({data_p.strftime('%d/%m/%Y')}) não pode ser realizado após a data do atendimento ({data_c.strftime('%d/%m/%Y')}).")
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
    