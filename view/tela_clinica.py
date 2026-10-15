from exception.excecoes import (
    ClinicaDuplicadaException,
    ClinicaNaoInformadaException,
    ClinicaNaoEncontradaException,
    ClinicaException,
)

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
                        
                        try:
                            nome = input("Nome da clínica: ").strip()
                            cidade = input("Cidade: ").strip()
                            descricao = input("Descrição: ").strip()
                            abertura = input("Horário de Abertura (HH:MM): ").strip()
                            fechamento = input("Horário de Fechamento (HH:MM): ").strip()

                            self.__controlador.adicionar_clinica(
                                nome, cidade, descricao, abertura, fechamento
                            )

                            print("Clínica adicionada com sucesso!")

                        except ClinicaDuplicadaException as e:
                            print(f"ERRO — CLÍNICA DUPLICADA: {e}")

                        except ClinicaNaoInformadaException as e:
                            print(f"ERRO — CAMPO OBRIGATÓRIO: {e}")

                        except ClinicaNaoEncontradaException as e:
                            print(f"ERRO — CLÍNICA NÃO ENCONTRADA: {e}")

                        except (ClinicaException, ValueError) as e:
                            print(f"ERRO — CLÍNICA: {e}")
 
                    elif opcao == "2":
                        try:
                            nome = input("Nome da Clínica para ser excluída: ")
                            self.__controlador.excluir_clinica(nome)
                            print(f"Clínica Excluída com sucesso")
                        except (ClinicaException, ValueError) as e:
                            print(f"ERRO : {e}")
                    elif opcao == "3":
                        nome_atual = input("Nome da Clínica para ser alterada: ").strip()
                        try:
                            print("Cliníca Encontrada! Digite os novos dados:")
                            novo_nome = input("Digite o novo nome: ").strip()
                            nova_localizacao = input("Digite a nova localização/cidade: ").strip()
                            nova_descricao = input("Digite a nova descrição: ").strip()
                            novo_horario_abertura = input("Digite o novo horário de abertura: ").strip()
                            novo_horario_fechamento = input("Digite o novo horário de fechamento: ").strip()
                            self.__controlador.alterar_dados_clinica(nome_atual,novo_nome,nova_localizacao,nova_descricao,novo_horario_abertura,novo_horario_fechamento)
                            print("Dados de Clínica Alterados com Sucesso!")
                        except (ClinicaException, ValueError) as e:
                            print(f"ERRO : {e}") 

                    elif opcao == "4":
                        try:
                            clinicas = self.__controlador.listar_clinicas()
                            if not clinicas:
                                print("Não há clinicas cadastradas")
                            else:
                                for indice,clinica in enumerate(clinicas):
                                    print(f"{indice + 1} {clinica}")
                        except (ClinicaException, ValueError) as e:
                            print(f"ERRO : {e}")       
                    elif opcao =="0":
                        print("Retornando ao menu principal...")
                        break
        
                    else:
                        print("Escolha Inválida! Tente Novamente!")