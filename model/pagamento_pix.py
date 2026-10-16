from .pagamento import Pagamento

class PagamentoPix(Pagamento):
    def __init__(
        self,
        consulta,
        valor_pago,
        data_pagamento,
        cpf_pagador,
    ):
        super().__init__(
            consulta,
            valor_pago,
            data_pagamento
        )
        self.__cpf_pagador = str(cpf_pagador)
    @property
    def cpf_pagador(self):
        return self.__cpf_pagador
    
    def descricao_detalhada(self):
        return f"PIX | Chave: {self.__cpf_pagador}"