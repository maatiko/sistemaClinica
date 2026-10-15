from controller.controladorConsulta import ControladorConsulta

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
            print("0. Retornar ao menu")
            opcao = input("Insira sua opção: ")

            if opcao =="1":
                nome_clinica = input("Nome da clínica: ")
                cpf_pac = input("CPF do Paciente: ")
                registro_prof = input("Registro do Profissional: ")
                tipo_consulta = input("Tipo de Consulta: ")

                valor = input("Valor da Consulta R$: ")
                if not valor.replace(".","",1).isdigit():
                    raise ValueError("Deve ser númerico apenas")
                
                data_cons = input("Data da Consulta (DD/MM/AAAA): ")
                horario_cons = input("Horário da Consulta (HH:MM): ")

                self.__controlador.agendar_consulta(nome_clinica, cpf_pac, registro_prof, tipo_consulta, valor, data_cons,horario_cons)
                print(f"\n[Resultado]: ")

            elif opcao == "2":

                cpf_pac = input("CPF do paciente para a consulta ser excluída: ")
                data_consulta = input("Data da consulta a ser cancelada (DD/MM/AAAA): ")
                horario_consulta = input("Horário da consulta a ser cancelada (HH:MM): ")
                
                excluir_consulta = self.__controlador.excluir_consulta(cpf_pac,data_consulta,horario_consulta)
                print(f"Resultado: {excluir_consulta}")

            elif opcao == "3":
                    
                    print("Primeiro, identifique a consulta atual:")
                    cpf_paciente = input("CPF do Paciente: ")
                    data_atual = input("Data atual da consulta (DD/MM/AAAA): ")
                    horario_atual = input("Horário atual da consulta (HH:MM): ")

                    if self.__controlador.verificar_existencia_consulta(cpf_paciente, data_atual, horario_atual ):
                        print("Consulta achada, vamos reagendá-lá: ")
                        nova_data = input("Nova Data (DD/MM/AAAA): ")
                        novo_horario = input("Novo Horário (HH:MM): ")
                        self.__controlador.alterar_consulta(cpf_paciente, data_atual, horario_atual, nova_data, novo_horario)
                        print("Reagendamento feito com sucesso")

            elif opcao == "4":
                consultas = self.__controlador.listar_consultas()
                if not consultas:
                    print("Não há consultas cadastrados")
                else:
                    print("\n--Lista Consultas--")
                    for indice,consulta in enumerate(consultas):
                        print(f"{indice + 1} {consulta}")


            elif opcao =="0":
                print("Retornando ao menu principal...")
                break
            
            else:
                print("Escolha Inválida! Tente Novamente!")
