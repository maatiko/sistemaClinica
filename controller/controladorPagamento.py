from datetime import date, datetime
from model.pagamento import Pagamento
from model.pagamento_dinheiro import PagamentoDinheiro
from model.pagamento_cartao import PagamentoCartao
from model.pagamento_pix import PagamentoPix
from view.tela_pagamento import TelaPagamento

class ControladorPagamento:
    def __init__(self,controlador_sistema):
        self.__sistema = controlador_sistema
        self.__pagamentos= []
        self.__tela_pagamento = TelaPagamento(self)

    def abrir_tela(self):
        self.__tela_pagamento.menu_pagamento()

    def obter_resumo_financeiro_consulta(self, cpf: str, data_str: str, horario_str: str) -> dict:
        consulta = self.__buscar_consulta(cpf, data_str, horario_str)
        valor_total = self.__calcular_valor_total_consulta(consulta) or 0.0
        total_pago = self.calcular_total_pago_por_consulta(consulta) or 0.0
        valor_restante = max(0.0, valor_total - total_pago)

        nome_paciente = consulta.paciente.nome if hasattr(consulta.paciente, 'nome') else str(consulta.paciente)

        return {
            "consulta": consulta,
            "paciente_nome": nome_paciente,
            "paciente_cpf": cpf,
            "valor_total": valor_total,
            "total_pago": total_pago,
            "valor_restante": valor_restante,
            "quitado": valor_restante == 0.0
        }
    
    def calcular_total_pago_por_consulta(self, consulta) -> float:
        total = 0.0
        for pag in self.__pagamentos:
            if pag.consulta == consulta:
                total += pag.valor_pago
        return total
       
    def processar_pagamento(self, cpf: str, data_str: str, horario_str: str, valor_a_pagar: float, tipo: str, dados_extra: dict, data_pagamento=None):
        resumo = self.obter_resumo_financeiro_consulta(cpf, data_str, horario_str)
        consulta = resumo["consulta"]
        valor_restante = resumo["valor_restante"]

        if valor_restante <= 0:
            raise ValueError("Esta consulta já está completamente quitada!")

        if valor_a_pagar > valor_restante:
            raise ValueError(f"O valor informado (R$ {valor_a_pagar:.2f}) é maior que o valor restante (R$ {valor_restante:.2f}).")

        if tipo == "1":
            quantia_entregue = dados_extra.get("quantia_recebida", valor_a_pagar)
            if quantia_entregue < valor_a_pagar:
                raise ValueError("A quantia entregue em dinheiro é menor do que o valor do pagamento.")
            
            novo_pagamento = PagamentoDinheiro(
                consulta=consulta, 
                valor_pago=valor_a_pagar, 
                quantia_recebida=quantia_entregue, 
                data_pagamento=data_pagamento
            )

        elif tipo == "2":
            numero_cartao = dados_extra.get("numero_cartao")
            bandeira = dados_extra.get("bandeira")
            parcelas = dados_extra.get("parcelas", 1)
            
            novo_pagamento = PagamentoCartao(
                consulta=consulta, 
                valor_pago=valor_a_pagar, 
                numero_cartao=numero_cartao, 
                bandeira=bandeira, 
                parcelas=parcelas, 
                data_pagamento=data_pagamento
            )

        elif tipo == "3":
            cpf_pagador = dados_extra.get("cpf_pagador")
            
            novo_pagamento = PagamentoPix(
                consulta=consulta, 
                valor_pago=valor_a_pagar, 
                cpf_pagador=cpf_pagador, 
                data_pagamento=data_pagamento
            )
        else:
            raise ValueError("Tipo de pagamento inválido.")

        self.__pagamentos.append(novo_pagamento)
        return novo_pagamento

    def __calcular_valor_total_consulta(self, consulta) -> float:
        if hasattr(consulta, "valor_total") and callable(getattr(consulta, "valor_total")):
            res = consulta.valor_total()
            if res is not None:
                return float(res)
        valor_base = getattr(consulta, "valor", 0.0) or 0.0

        custo_procedimentos = 0.0
        if hasattr(consulta, "procedimentos") and consulta.procedimentos:
            for p in consulta.procedimentos:
                custo = getattr(p, 'custo', 0.0)
                if custo is not None:
                    custo_procedimentos += float(custo)
            
        return float(valor_base) + custo_procedimentos
            
    
    def __buscar_consulta(self, cpf: str, data_str: str, horario_str: str):
        consultas = self.__sistema.controlador_consulta.listar_consultas()
        
        for c in consultas:
            cpf_c = c.paciente.cpf if hasattr(c, 'paciente') and hasattr(c.paciente, 'cpf') else None
            
            if hasattr(c, 'data') and hasattr(c.data, 'strftime'):
                data_c = c.data.strftime("%d/%m/%Y")
            else:
                data_c = str(getattr(c, 'data', ''))

            if hasattr(c, 'horario') and hasattr(c.horario, 'strftime'):
                horario_c = c.horario.strftime("%H:%M")
            else:
                horario_c = str(getattr(c, 'horario', ''))

            if cpf_c == cpf and data_c == data_str and horario_c == horario_str:
                return c

        raise ValueError(f"Consulta não encontrada para o CPF {cpf} em {data_str} às {horario_str}.")

    def buscar_por_cpf(self, cpf: str):
        resultados = []
        for pag in self.__pagamentos:
            cpf_paciente = pag.consulta.paciente.cpf if hasattr(pag.consulta.paciente, 'cpf') else None
            if cpf_paciente == cpf:
                resultados.append(pag)
        return resultados