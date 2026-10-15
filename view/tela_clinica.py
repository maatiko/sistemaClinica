class TelaClinica:
    def __init__(self,controlador_clin):
        self.__controlador = controlador_clin

    def menu_clinica(self):
        while True:
                    print("\n--- Menu de Clínica ---")
                    print("Escolha uma opção:")
                    print("1. Cadastrar Clínica")
                    print("2. Excluir Clínica")
                    print("3. Alterar Clínica")
                    print("4. Listar Clinícas")
                    print("0. Retornar ao menu")
                    opcao = input("Insira sua opção: ")
        
                    if opcao =="1":
                        nome = input("Nome da clínica: ")
                        cidade = input("Cidade: ")
                        descricao = input("Descrição: ")
                        abertura = input("Horário de Abertura (HH:MM): ")
                        fechamento = input("Horário de Fechamento (HH:MM): ")
        
                        adicionar_clinica = self.__controlador.adicionar_clinica(nome, cidade, descricao, abertura, fechamento)
                        print(f"\n[Resultado]: {adicionar_clinica}")
        
                    elif opcao == "2":
                        nome = input("Nome da Clínica para ser excluída: ")
                        excluir_clinica = self.__controlador.excluir_clinica(nome)
                        print(f"Resultado: {excluir_clinica}")
        
                    elif opcao == "3":
                        nome_atual = input("Nome da Clínica para ser alterada: ").strip()
                        if self.__controlador.verificar_existencia(nome):
                            print("Cliníca Encontrada! Digite os novos dados:")
                            novo_nome = input("Digite o novo nome: ")
                            nova_localizacao = input("Digite a nova localização/cidade: ")
                            nova_descricao = input("Digite a nova descrição: ")
                            novo_horario_abertura = input("Digite o novo horário de abertura: ")
                            novo_horario_fechamento = input("Digite o novo horário de fechamento: ")
                            self.__controlador.alterar_dados_clinica(nome_atual,novo_nome,nova_localizacao,nova_descricao,novo_horario_abertura,novo_horario_fechamento)
                            print("Dados Alterados com Sucesso!")
                        else:
                            #erro que não existe a clínica que está se procurando
                            pass
                    elif opcao == "4":
                        clinicas = self.__controlador.listar_clinicas()
                        if not clinicas:
                            print("Não há clinicas cadastradas")
                        else:
                            for indice,clinica in enumerate(clinicas):
                                print(f"{indice + 1} {clinica}")
        
                    elif opcao =="0":
                        print("Retornando ao menu principal...")
                        break
        
                    else:
                        print("Escolha Inválida! Tente Novamente!")