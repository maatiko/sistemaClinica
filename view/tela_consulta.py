class TelaConsulta:
    def __init__(self,controlador_cons):
        self.__controlador = controlador_cons

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

                    valor = input("Valor da Consulta R$: ")
                    if not valor.replace(".","",1).isdigit():
                        raise ValueError("O valor da consulta deve ser númerico apenas")
                    
                    data_cons = input("Data da Consulta (DD/MM/AAAA): ")
                    horario_cons = input("Horário da Consulta (HH:MM): ")

                    self.__controlador.agendar_consulta(nome_clinica, cpf_pac, registro_prof, tipo_consulta, valor, data_cons,horario_cons)
                    print(f"\nAgendado a Consulta ")
                except ValueError as e:
                            print(f"ERRO : {e}")

            elif opcao == "2":
                try:
                    cpf_pac = input("CPF do paciente para a consulta ser excluída: ").strip()
                    data_consulta = input("Data da consulta a ser cancelada (DD/MM/AAAA): ").strip()
                    horario_consulta = input("Horário da consulta a ser cancelada (HH:MM): ").strip()
                    
                    excluir_consulta = self.__controlador.excluir_consulta(cpf_pac,data_consulta,horario_consulta)
                    print(f"Removida a Consulta")
                except ValueError as e:
                    print(f"Erro: {e}")

            elif opcao == "3":
                    try:
                        print("Primeiro, identifique a consulta atual:")
                        cpf_paciente = input("CPF do Paciente: ").strip()
                        data_atual = input("Data atual da consulta (DD/MM/AAAA): ").strip()
                        horario_atual = input("Horário atual da consulta (HH:MM): ").strip()

                        self.__controlador.verificar_existencia_consulta(cpf_paciente, data_atual, horario_atual)
                        print("Consulta achada, vamos reagendá-lá: ")
                        nova_data = input("Nova Data (DD/MM/AAAA): ").strip()
                        novo_horario = input("Novo Horário (HH:MM): ").strip()
                        self.__controlador.alterar_consulta(cpf_paciente, data_atual, horario_atual, nova_data, novo_horario)
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
                        for indice,consulta in enumerate(consultas):
                            print(f"{indice + 1} {consulta}")
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
        cpf_pac = input("CPF do paciente: ")
        data_cons = input("Data da Consulta (DD/MM/AAAA): ")
        horario_cons = input("Horário da Consulta (HH:MM): ")
        
        try:
            self.__controlador.verificar_existencia_consulta(cpf_pac, data_cons, horario_cons)
        except ValueError as e:
            print(f" Erro: {e}")
            
        while True:
            print(f"\n--- PROCEDIMENTOS DA CONSULTA ({data_cons} às {horario_cons}) ---")
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
                    
                    self.__controlador.adicionar_procedimento_na_consulta(cpf_pac, data_cons, horario_cons, desc, float(custo), registro)
                    print(" Procedimento adicionado!")
                except ValueError as e:
                    print(f" Erro: {e}")

            elif opcao == "2":
                try:
                    desc_excluir = input("Descrição do procedimento a excluir: ")
                    self.__controlador.excluir_procedimento_da_consulta(cpf_pac, data_cons, horario_cons, desc_excluir)
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
                    
                    self.__controlador.alterar_procedimento_da_consulta(cpf_pac, data_cons, horario_cons, desc_atual,nova_desc, float(novo_custo_str), novo_registro)
                    print(" Procedimento alterado!")
                except ValueError as e:
                    print(f"Erro: {e}")

            elif opcao == "4":
                try:
                    procedimentos = self.__controlador.listar_procedimentos_da_consulta(cpf_pac, data_cons, horario_cons)
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