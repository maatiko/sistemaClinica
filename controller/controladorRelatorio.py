from collections import Counter

class ControladorRelatorio:

    def __init__(self, controlador_clinica, controlador_consulta, controlador_pagamento):
        self.controlador_clinica = controlador_clinica
        self.controlador_consulta = controlador_consulta
        self.controlador_pagamento = controlador_pagamento

    def checar_clinica_maior_atendimento(self):
        consultas = self.controlador_consulta.listar_consultas()

        if not consultas:
            return None

        contagem = Counter(consulta.clinica for consulta in consultas)

        clinica, quntidade = contagem.most_common(1)[0]

        return {"clinica": clinica, "quantidade_atendimentos": quntidade}

    def gerar_relatorio_consulta(self):
        return {"clinica_com_mais_atendimentos": self.checar_clinica_maior_atendimento(), "consulta_mais_cara": self.checar_consulta_cara(), "consulta_mais_barata": self.checar_consulta_barata()} 

    def checar_consulta_cara(self):
        consultas = self.controlador_consulta.listar_consultas()

        if not consultas:
            return None

        return max(consultas, key=lambda consulta: consulta.valor)

    def checar_consulta_barata(self):
        consultas = self.controlador_consulta.listar_consultas()

        if not consultas:
            return None

        return min(consultas, key=lambda consulta: consulta.valor)

    def checar_procedimentos_popular(self):
        consultas = self.controlador_consulta.listar_consultas()
        procedimentos = []

        for consulta in consultas:
            procedimentos.extend(consulta.procedimentos_realizados)

        if not procedimentos:
            return None 

        contagem = Counter(procedimento.descricao for procedimento in procedimentos)
        descricao, quantidade = contagem.most_common(1)[0]

        return {"descricao": descricao, "quantidade": quantidade}

    def checar_procedimento_barato(self):
        consultas = self.controlador_consulta.listar_consultas()
        procedimentos = []

        for consulta in consultas:
            procedimentos.extend(consulta.procedimentos_realizados)

        if not procedimentos:
            return None

        return min(procedimentos, key=lambda procedimento: procedimento.custo)

    def checar_procedimento_caro(self):
        consultas = self.controlador_consulta.listar_consultas()
        procedimentos = []

        for consulta in consultas:
            procedimentos.extend(consulta.procedimentos_realizados)

        if not procedimentos:
            return None

        return max(procedimentos, key=lambda procedimento: procedimento.custo)

    def gerar_relatorio_procedimento(self):
        return {"procedimento_mais_popular": self.checar_procedimentos_popular(), "procedimento_mais_barato": self.checar_procedimento_barato(), "procedimento_mais_caro": self.checar_procedimento_caro()}