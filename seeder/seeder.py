from datetime import date

def popular_sistema(controlador_sistema):
    try:
        controlador_sistema.controlador_tipo_atendimento.adicionar_tipo_atendimento(
            "Retorno", "Consulta de retorno", 200.0
        )
        controlador_sistema.controlador_tipo_atendimento.adicionar_tipo_atendimento(
            "Primeira Consulta", "Consulta inicial", 180.0
        )

        controlador_sistema.controlador_clinica.adicionar_clinica(
            "Clínica Santa Cruz", "Florianópolis", "Multiespecialidades", "08:00", "18:00"
        )
        controlador_sistema.controlador_clinica.adicionar_clinica(
            "Clínica Santos", "Florianópolis", "Multiespecialidades", "08:00", "18:00"
        )
        
        controlador_sistema.controlador_pessoa.adicionar_paciente(
            "João Silva", "11122233344", "48999991111", date(1990, 5, 20)
        )
        controlador_sistema.controlador_pessoa.adicionar_paciente(
            "Paulo Santos", "77777777700", "48999996666", date(1985, 8, 15)
        )
        
        controlador_sistema.controlador_pessoa.adicionar_profissional(
            "Dra. Maria Souza", "22233344455", "48999992222", "Cardiologia", "CRM1234"
        )
        controlador_sistema.controlador_pessoa.adicionar_profissional(
            "Dr. Carlos Lima", "22933344455", "48999993333", "Ortopedia", "CRM5678"
        )

        id_atendimento = controlador_sistema.controlador_consulta.agendar_consulta(
            "Clínica Santa Cruz",
            "11122233344",
            "CRM1234",
            "Retorno",
            "25/11/2026",
            "10:00",
            "11:00",
        )
        controlador_sistema.controlador_consulta.adicionar_procedimento_na_consulta(
            id_atendimento, "Eletrocardiograma", 150.0, "CRM1234"
        )

        controlador_sistema.controlador_consulta.agendar_consulta(
            "Clínica Santos",
            "77777777700",
            "CRM5678",
            "Primeira Consulta",
            "26/11/2026",
            "14:30",
            "15:30",
        )

        ctrl_pag = controlador_sistema.controlador_pagamento

        ctrl_pag.processar_pagamento(
            id_atendimento=id_atendimento,
            valor_a_pagar=150.0,
            tipo="3",
            dados_extra={"cpf_pagador": "11122233344"},
            data_pagamento="25/11/2026"
        )


        print("⚡ [TESTE] Dados iniciais e pagamentos carregados com sucesso!")

    except Exception as e:
        print(f" Erro ao popular dados de teste: {e}")