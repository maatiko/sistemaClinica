from datetime import date

def popular_sistema(controlador_sistema):
    try:

        # 1. Clínicas
        controlador_sistema.controlador_clinica.adicionar_clinica(
            "Clínica Santa Cruz", "Florianópolis", "Multiespecialidades", "08:00", "18:00"
        )
        controlador_sistema.controlador_clinica.adicionar_clinica(
            "Clínica Santos ", "Florianópolis", "Multiespecialidades", "08:00", "18:00"
        )
        
        # 2. Pessoas (Paciente e Médico)
        controlador_sistema.controlador_pessoa.adicionar_paciente(
            "João Silva", "11122233344", "48999991111", date(1990, 5, 20)
        )
        controlador_sistema.controlador_pessoa.adicionar_paciente(
            "Paulo", "777777777", "48999996666", date(1990, 5, 20)
        )
        controlador_sistema.controlador_pessoa.adicionar_profissional(
            "Dra. Maria Souza", "22233344455", "48999992222", "Cardiologia", "CRM1234"
        )
        controlador_sistema.controlador_pessoa.adicionar_profissional(
            "Dra. Maria Souza", "22933344455", "48999992222", "Cardiologia", "CRM1234"
        )

        # 3. Consultas e Procedimentos
        controlador_sistema.controlador_consulta.agendar_consulta(
            "Clínica Santa Cruz", "11122233344", "CRM1234", "Retorno", 200.0, "25/11/2026", "10:00"
        )
        controlador_sistema.controlador_consulta.adicionar_procedimento_na_consulta(
            "11122233344", "25/11/2026", "10:00", "Eletrocardiograma", 150.0, "CRM1234"
        )

        print("⚡ [TESTE] Dados iniciais carregados com sucesso!")
    except Exception as e:
        print(f" Erro ao popular dados de teste: {e}")