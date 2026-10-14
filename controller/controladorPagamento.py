from datetime import date, datetime


class ControladorPagamento:
    def __init__(self):
        self.pagamentos_realizados = []
        self.pagamentos_devidos = []

    def validar_pagamento(self, pagamento):
        if pagamento is None:
            raise ValueError("Pagamento não informado.")

        if pagamento.atendimento is None:
            raise ValueError("Pagamento sem atendimento associado.")

        if pagamento.paciente is None:
            raise ValueError("Pagamento sem paciente associado.")

        if pagamento.valor_pago < 0:
            raise ValueError("O valor pago não pode ser negativo.")

        modalidades_validas = {"dinheiro", "pix", "cartão de crédito"} 

        modalidade = pagamento.modalidade.strip().lower()

        if modalidade not in modalidades_validas:
            raise ValueError("Modalidade inválida. Use dinheiro, PIX ou cartão de crédito.")

        data_pagamento = pagamento.data 
        data_atendimento = pagamento.atendimento.data 

        if isinstance(data_pagamento, str):
            data_pagamento = datetime.strptime(data_pagamento, "%d/%m/%Y").date()

        if isinstance(data_atendimento, str):
            data_atendimento = datetime.strptime(data_atendimento, "%d/%m/%Y").date()

        if isinstance(data_pagamento, datetime):
            data_pagamento = data_pagamento.date()

        if isinstance(data_atendimento, datetime):
            data_atendimento = data_atendimento.date()

        if data_pagamento > data_atendimento:
            raise ValueError("O pagamento deve ocorrer até a data do atencimento.")

        if modalidade == "pix":
            if not pagamento.cpf_pagador:
                raise ValueError("Informe o CPF do pagador do PIX.") 

        if modalidade in {"cartão de crédito", "cartao de credito"}:
            if not pagamento.numero_cartao:
                raise ValueError("Informe o número do cartão.")

            if not pagamento.bandeira:
                raise ValueError("Informe a bandeira do cartão.")

        total = pagamento.atendimento.valor
        pago_anteriormente = sum(p.valor_pago for p in self.pagamentos_realizados if p.atendimento is pagamento.atendimento and p is not pagamento)

        if pago_anteriormente + pagamento.valor_pago > total:
            raise ValueError("O valor dos pagamentos ultrapassa o total do atendimento.")

        return True

    def processar_pagamento(self, pagamento):
        self.validar_pagamento(pagamento)

        if pagamento not in self.pagamentos_realizados:
            self.pagamentos_realizados.append(pagamento)

        self.atualizar_divida(pagamento.atendimento)

    def atualizar_divida(self, atendimento):
        total = atendimento.valor

        pago = sum(p.valor_pago for p in self.pagamentos_realizados if p.atendimento is atendimento)

        restante = max(0, total - pago)

        if restante > 0:
            if atendimento not in self.pagamentos_devidos:
                self.pagamentos_devidos.append(atendimento)

        elif atendimento in self.pagamentos_devidos:
            self.pagamentos_devidos.remove(atendimento)

        return restante

    def parcelar_consulta(self, atendimento):
        if atendimento is None:
            raise ValueError("Atendimento não informado.")

        if atendimento not in self.pagamentos_devidos:
            raise ValueError("Atendimento não possui dívida.")

        restante = self.atualizar_divida(atendimento)

        if restante <= 0:
            raise ValueError("Não há dívida a ser parcelada.")

        return restante

    def mostrar_valor_restante(self, atendimento):
        if atendimento is None:
            raise ValueError("Atendimento não informado.")

        if atendimento not in self.pagamentos_devidos:
            raise ValueError("Atendimento não possui dívida.")

        restante = self.atualizar_divida(atendimento)

        return restante