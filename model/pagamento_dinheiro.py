from typing import Optional

from model.pagamento import Pagamento


class PagamentoDinheiro(Pagamento):
    def __init__(self, consulta, valor_pago: float, quantia_recebida: Optional[float] = None, data_pagamento=None):
        val_pago = float(valor_pago) if valor_pago is not None else 0.0
        super().__init__(consulta=consulta, valor_pago=val_pago, data_pagamento=data_pagamento)
        
        quantia = quantia_recebida if quantia_recebida is not None else val_pago
        self.__quantia_recebida = float(quantia)
        self.__troco = max(0.0, self.__quantia_recebida - val_pago)
    
    @property
    def quantia_recebida(self):
        return self.__quantia_recebida

    @property
    def troco(self):
        return self.__troco

    def descricao_detalhada(self) :
        return f"Espécie | Recebido: R$ {self.__quantia_recebida:.2f} | Troco: R$ {self.__troco:.2f}"