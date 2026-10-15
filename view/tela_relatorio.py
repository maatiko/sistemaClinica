class TelaRelatorio:
    def __init__(self, controlador_relatorio):
        self.__controlador = controlador_relatorio

    def menu_relatorio(self):
        while True:
            print("\n--- MÓDULO DE RELATÓRIOS ---")
            print("1. Relatório Geral de Consultas e Clínicas")
            print("2. Relatório Geral de Procedimentos")
            print("0. Retornar ao Menu Principal")
            opcao = input("Insira sua opção: ").strip()

            if opcao == "1":
                self.exibir_relatorio_consultas()
            elif opcao == "2":
                self.exibir_relatorio_procedimentos()
            elif opcao == "0":
                print("Retornando ao menu principal...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def exibir_relatorio_consultas(self):
        dados = self.__controlador.gerar_relatorio_consulta()

        clinica_top = dados.get("clinica_com_mais_atendimentos")
        c_cara = dados.get("consulta_mais_cara")
        c_barata = dados.get("consulta_mais_barata")

        if not clinica_top and not c_cara and not c_barata:
            print("\n❌ Nenhuma consulta registrada no sistema para gerar relatórios.")
            return

        print("\n==========================================")
        print("      RELATÓRIO DE CONSULTAS E CLÍNICAS    ")
        print("==========================================")

        if clinica_top:
            nome_clinica = (
                clinica_top['clinica'].nome
                if hasattr(clinica_top['clinica'], 'nome')
                else clinica_top['clinica']
            )
            qtd = clinica_top['quantidade_atendimentos']
            print(f"🏥 Clínica Líder em Atendimentos: {nome_clinica} ({qtd} atendimento(s))")

        if c_cara:
            val_cara = c_cara.valor_total() if callable(getattr(c_cara, "valor_total", None)) else c_cara.valor_total
            data_f = c_cara.data.strftime("%d/%m/%Y")
            print(f"💰 Consulta Mais Cara: R${val_cara:.2f} | Paciente: {c_cara.paciente.nome} | Data: {data_f}")

        if c_barata:
            val_barata = c_barata.valor_total() if callable(getattr(c_barata, "valor_total", None)) else c_barata.valor_total
            data_f = c_barata.data.strftime("%d/%m/%Y")
            print(f"🏷️ Consulta Mais Barata: R${val_barata:.2f} | Paciente: {c_barata.paciente.nome} | Data: {data_f}")

    def exibir_relatorio_procedimentos(self):
        dados = self.__controlador.gerar_relatorio_procedimento()

        p_popular = dados.get("procedimento_mais_popular")
        p_caro = dados.get("procedimento_mais_caro")
        p_barato = dados.get("procedimento_mais_barato")

        if not p_popular and not p_caro and not p_barato:
            print("\n❌ Nenhum procedimento registrado em consultas para gerar relatórios.")
            return

        print("\n==========================================")
        print("        RELATÓRIO DE PROCEDIMENTOS        ")
        print("==========================================")

        if p_popular:
            print(f"🔥 Procedimento Mais Realizado: {p_popular['descricao']}")