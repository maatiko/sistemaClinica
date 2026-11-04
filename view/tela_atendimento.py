class TelaAtendimento:
    def __init__(self,controlador_atend):
        self.__controlador = controlador_atend

    def menu_consulta(self):
        while True:
            print("\n--- Menu de Consulta ---")
            print("Escolha uma opção:")
            print("1. Agendar Consulta")
            print("2. Excluir Consulta")
            print("3. Alterar Consulta")
            print("4. Listar Consultas")
            print("5. Gerencimento de Procedimentos")
            print("0. Retornar ao menu")
            opcao = input("Insira sua opção: ")

            if opcao =="1":
                try:
                    nome_clinica = input("Nome da clínica: ").strip()
                    cpf_pac = input("CPF do Paciente: ").strip()
                    registro_prof = input("Registro do Profissional: ").strip()
                    tipo_consulta = input("Tipo de Consulta: ").strip()

                    data_cons = input("Data da Consulta (DD/MM/AAAA): ")
                    horario_inicio = input("Horário de início (HH:MM): ").strip()
                    horario_fim = input("Horário de fim (HH:MM): ").strip()

                    id_atendimento = self.__controlador.agendar_consulta(
                        nome_clinica,
                        cpf_pac,
                        registro_prof,
                        tipo_consulta,
                        data_cons,
                        horario_inicio,
                        horario_fim,
                    )
                    print(f"\nAtendimento agendado com sucesso. ID: {id_atendimento}")
                except ValueError as e:
                            print(f"ERRO : {e}")

            elif opcao == "2":
                try:
                    id_atendimento = input("ID do atendimento a ser excluído: ").strip()
                    self.__controlador.excluir_consulta(id_atendimento)
                    print("Atendimento removido.")
                except ValueError as e:
                    print(f"Erro: {e}")

            elif opcao == "3":
                    try:
                        print("Primeiro, identifique a consulta atual:")
                        id_atendimento = input("ID do atendimento: ").strip()

                        atendimento = self.__controlador.buscar_consulta_por_id(id_atendimento)
                        print(f"Atendimento encontrado: {atendimento}")
                        print("Informe o novo horário: ")
                        nova_data = input("Nova Data (DD/MM/AAAA): ").strip()
                        novo_horario_inicio = input("Novo horário de início (HH:MM): ").strip()
                        novo_horario_fim = input("Novo horário de fim (HH:MM): ").strip()
                        self.__controlador.alterar_dados_consulta(
                            id_atendimento,
                            nova_data,
                            novo_horario_inicio,
                            novo_horario_fim,
                        )
                        print("Reagendamento feito com sucesso")
                    except ValueError as e:
                            print(f"ERRO : {e}")

            elif opcao == "4":
                try:
                    consultas = self.__controlador.listar_consultas()
                    if not consultas:
                        print("Não há consultas cadastrados")
                    else:
                        print("\n--Lista Consultas--")
                        for consulta in consultas:
                            print(consulta)
                except ValueError as e:
                    print(f"Erro {e}")
                    
            elif opcao =="5":
                self.menu_procedimentos()

            elif opcao =="0":
                print("Retornando ao menu principal...")
                break

            else:
                print("Escolha Inválida! Tente Novamente!")
    
    def menu_procedimentos(self):
        
        print("\n[Identifique a consulta para acessar os procedimentos]")
        id_atendimento = input("ID do atendimento: ").strip()
        
        try:
            atendimento = self.__controlador.buscar_consulta_por_id(id_atendimento)
        except ValueError as e:
            print(f" Erro: {e}")
            return

        print(f"Atendimento selecionado: {atendimento}")
            
        while True:
            print(f"\n--- PROCEDIMENTOS DO ATENDIMENTO #{atendimento.id_atendimento} ---")
            print("1. Adicionar Procedimento")
            print("2. Excluir Procedimento")
            print("3. Alterar Procedimento")
            print("4. Listar Procedimentos")
            print("0. Voltar")
            opcao = input("Insira sua opção: ").strip()

            if opcao == "1":
                try:
                    desc = input("Descrição (Ex: Raio-X): ").strip()
                    custo = input("Custo R$: ").strip()
                    if not custo.replace(".", "", 1).isdigit():
                        raise ValueError("O custo deve ser numérico.")
                    registro = input("Registro do Médico responsável: ").strip()
                    
                    self.__controlador.adicionar_procedimento_na_consulta(
                        id_atendimento, desc, float(custo), registro
                    )
                    print(" Procedimento adicionado!")
                except ValueError as e:
                    print(f" Erro: {e}")

            elif opcao == "2":
                try:
                    desc_excluir = input("Descrição do procedimento a excluir: ")
                    self.__controlador.excluir_procedimento_da_consulta(
                        id_atendimento, desc_excluir
                    )
                    print(" Procedimento removido!")
                except ValueError as e:
                    print(f" Erro: {e}")

            elif opcao == "3":
                try:
                    desc_atual = input("Descrição atual do procedimento: ").strip()
                    print("\nInsira os novos dados:")
                    nova_desc = input("Nova Descrição: ").strip()
                    
                    novo_custo_str = input("Novo Custo R$: ")
                    if not novo_custo_str.replace(".", "", 1).isdigit():
                        raise ValueError("O custo deve ser numérico.")
                        
                    novo_registro = input("Registro do Médico responsável: ").strip()
                    
                    self.__controlador.alterar_procedimento_da_consulta(
                        id_atendimento,
                        desc_atual,
                        nova_desc,
                        float(novo_custo_str),
                        novo_registro,
                    )
                    print(" Procedimento alterado!")
                except ValueError as e:
                    print(f"Erro: {e}")

            elif opcao == "4":
                try:
                    procedimentos = self.__controlador.listar_procedimentos_da_consulta(
                        id_atendimento
                    )
                    if not procedimentos:
                        print("Nenhum procedimento registrado nesta consulta.")
                    else:
                        print("\n--- LISTA DE PROCEDIMENTOS ---")
                        for i, p in enumerate(procedimentos):
                            print(f"[{i+1}] {p}") 
                except ValueError as e:
                     print(f" Erro: {e}")

            elif opcao == "0":
                break
            else:
                print("Opção inválida.")