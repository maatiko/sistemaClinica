class TelaPagamento:
    def __init__(self, controlador_pagamento):
        self.__controlador = controlador_pagamento

    def menu_pagamento(self):
        while True:
            print("\n" + "="*42)
            print("        MÓDULO DE PAGAMENTOS")
            print("="*42)
            print("1 - Registrar Pagamento de Consulta")
            print("2 - Listar Todos os Pagamentos")
            print("3 - Buscar Pagamentos por Paciente (CPF)")
            print("0 - Retornar ao Menu Principal")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.registrar_pagamento()
            elif opcao == "2":
                self.listar_pagamentos()
            elif opcao == "3":
                self.buscar_por_cpf()
            elif opcao == "0":
                break
            else:
                print("⚠️ Opção inválida. Tente novamente.")

    def registrar_pagamento(self):
        print("\n--- REGISTRO DE PAGAMENTO ---")
        cpf = input("CPF do Paciente: ").strip()
        data_str = input("Data da Consulta (DD/MM/AAAA): ").strip()
        horario_str = input("Horário da Consulta (HH:MM): ").strip()

        try:
            resumo = self.__controlador.obter_resumo_financeiro_consulta(cpf, data_str, horario_str)

            print("\n" + "-"*40)
            print(" DETALHES DO ATENDIMENTO")
            print(f"• Paciente: {resumo['paciente_nome']} (CPF: {resumo['paciente_cpf']})")
            print(f"• Data/Horário: {data_str} às {horario_str}")
            print(f"• Valor Total da Consulta: R$ {resumo['valor_total']:.2f}")
            print(f"• Total Já Pago:            R$ {resumo['total_pago']:.2f}")
            print(f"• VALOR RESTANTE:           R$ {resumo['valor_restante']:.2f}")
            print("-" * 40)

            if resumo["quitado"]:
                print(" Esta consulta já está totalmente quitada!")
                return

            opcao_pagar = input("\nDeseja efetuar um pagamento agora? (s/n): ").strip().lower()
            if opcao_pagar != 's':
                return

            data_pagamento_input = input("Data do Pagamento (DD/MM/AAAA) [deixe em branco para HOJE]: ").strip()
            data_pag = data_pagamento_input if data_pagamento_input else None

            valor_a_pagar = float(input(f"Valor a pagar (máx R$ {resumo['valor_restante']:.2f}): ").replace(",", "."))

            print("\nForma de Pagamento:")
            print("1 - Dinheiro")
            print("2 - Cartão de Crédito")
            print("3 - PIX")
            tipo = input("Selecione o tipo: ").strip()

            dados_extra = {}
            if tipo == "1":
                quantia = float(input("Quantia entregue pelo cliente (R$): ").replace(",", "."))
                dados_extra["quantia_recebida"] = quantia
            elif tipo == "2":
                dados_extra["numero_cartao"] = input("Número do Cartão: ").strip()
                dados_extra["bandeira"] = input("Bandeira (Visa, Mastercard, etc.): ").strip()
                dados_extra["parcelas"] = int(input("Número de parcelas: ").strip() or "1")
            elif tipo == "3":
                dados_extra["cpf_pagador"] = input("CPF do Pagador: ").strip()

            pagamento = self.__controlador.processar_pagamento(
                cpf, data_str, horario_str, valor_a_pagar, tipo, dados_extra, data_pagamento=data_pag
            )
            
            novo_resumo = self.__controlador.obter_resumo_financeiro_consulta(cpf, data_str, horario_str)

            print("\n Pagamento registrado com sucesso!")
            print(f"• Valor Pago: R$ {pagamento.valor_pago:.2f} | Forma: {pagamento.descricao_detalhada()}")
            print(f"• Data do Registro: {pagamento.data_pagamento.strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"• Novo Valor Restante: R$ {novo_resumo['valor_restante']:.2f}")

        except ValueError as e:
            print(f" Erro ao registrar pagamento: {e}")
        except Exception as e:
            print(f" Erro inesperado: {e}")

    def listar_pagamentos(self):
        print("\n--- LISTA DE PAGAMENTOS REGISTRADOS ---")
        pagamentos = self.__controlador.listar_pagamentos()

        if not pagamentos:
            print("Nenhum pagamento registrado até o momento.")
            return

        for idx, pag in enumerate(pagamentos, start=1):
            nome_paciente = pag.consulta.paciente.nome if hasattr(pag.consulta, 'paciente') and hasattr(pag.consulta.paciente, 'nome') else pag.consulta.paciente
            data_p = pag.data_pagamento.strftime("%d/%m/%Y %H:%M") if hasattr(pag.data_pagamento, 'strftime') else str(pag.data_pagamento)
            print(f"{idx}. Paciente: {nome_paciente} | Valor: R$ {pag.valor_pago:.2f} | Data: {data_p}")
            print(f"   Forma: {pag.descricao_detalhada()}")
            print("-" * 45)

    def buscar_por_cpf(self):
        cpf = input("Informe o CPF do paciente: ").strip()
        pagamentos = self.__controlador.buscar_por_cpf(cpf)

        print(f"\n--- PAGAMENTOS DO PACIENTE (CPF: {cpf}) ---")
        if not pagamentos:
            print("Nenhum pagamento encontrado para este paciente.")
            return

        for pag in pagamentos:
            data_p = pag.data_pagamento.strftime("%d/%m/%Y %H:%M") if hasattr(pag.data_pagamento, 'strftime') else str(pag.data_pagamento)
            print(f"• Valor: R$ {pag.valor_pago:.2f} em {data_p} ({pag.descricao_detalhada()})")