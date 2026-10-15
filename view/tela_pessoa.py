from datetime import date,datetime

class TelaPessoa:
    def __init__(self,controlador_pes):
        self.__controlador = controlador_pes

    def menu_principal_pessoa(self):
        while True:
            print("\n--- MÓDULO DE PESSOAS ---")
            print("1. Gerenciar Pacientes")
            print("2. Gerenciar Profissionais")
            print("0. Retornar ao menu principal")
            opcao = input("Insira sua opção: ").strip()
            
            if opcao == "1":
                self.menu_paciente()
            elif opcao == "2":
                self.menu_profissional()
            elif opcao == "0":
                break
            else:
                print("Escolha inválida!")

    def menu_paciente(self):
            while True:
                print("\n--- Menu Paciente ---")
                print("Escolha uma opção:")
                print("1. Cadastrar Paciente")
                print("2. Excluir Paciente")
                print("3. Alterar Paciente")
                print("4. Listar Pacientes")
                print("0. Retornar ao menu")
                opcao = input("Insira sua opção: ")
    
                if opcao =="1":
                    
                    nome = input("Nome do Paciente: ")
                    cpf = input("CPF do Paciente: ")
                    telefone = input("Telefone do paciente: ")
                    data_nascimento = input("Data de Nascimento do Paciente (DD/MM/AAAA): ")
                    data_convertida = datetime.strptime(data_nascimento,"%d/%m/%Y").date()
                    adicionar_paciente = self.__controlador.adicionar_paciente(nome, cpf,telefone,data_nascimento )
                    print(f"\n[Resultado]: {adicionar_paciente}")
                
    
                elif opcao == "2":
    
                    cpf_pac = input("CPF do Paciente para ser excluída: ")
                    excluir_paciente = self.__controlador.remover_paciente(cpf_pac)
                    print(f"Resultado: {excluir_paciente}")
    
                elif opcao == "3":
    
                    cpf_atual = input("CPF do Paciente para ser alterado: ")
                    if self.__controlador.verificar_existencia_paciente(cpf_atual):
                        print("CPF Encontrado! Vamos alterar o cadastro: ")
                        novo_nome = input("Nome do Paciente: ")
                        novo_cpf = input("CPF do Paciente: ")
                        novo_telefone = input("Telefone do paciente: ")
                        nova_data_nascimento = input("Data de Nascimento do Paciente: ")     
                        data_convertida = datetime.strptime(nova_data_nascimento,"%d/%m/%Y").date()
    
                        alterar_paciente = self.__controlador.alterar_dados_pessoa(cpf_atual,novo_nome, novo_cpf, novo_telefone,data_convertida)
                    print(f"Resultado: {alterar_paciente}")
                
                elif opcao == "4":
                    pacientes = self.__controlador.mostrar_pacientes()
                    if not pacientes:
                        print("Não há pacientes cadastrados")
                    else:
                        print("\n--Lista Pacientes--")
                        for indice,paciente in enumerate(pacientes):
                            print(f"{indice + 1} {paciente}")
        
                elif opcao =="0":
                    print("Retornando ao menu principal...")
                    break
    
                else:
                    print("Escolha Inválida! Tente Novamente!")
    
    def menu_profissional(self):
            while True:
                print("\n--- Menu de Profissional ---")
                print("Escolha uma opção:")
                print("1. Cadastrar Profissional")
                print("2. Excluir Profissional")
                print("3. Alterar Profissional")
                print("4. Listar Profissionais")
                print("0. Retornar ao menu")
                opcao = input("Insira sua opção: ")
    
                if opcao =="1":
                    
                    nome = input("Nome do Profissional: ")
                    cpf = input("CPF do Profissional: ")
                    telefone = input("Telefone do Profissional: ")
                    registro = input("Registro do Profissional ")
                    especialidade = input("Especialidade do Profissional: ")
                    adicionar_profissional = self.__controlador.adicionar_profissional(nome, cpf,telefone,registro,especialidade )
                    print(f"\n[Resultado]: {adicionar_profissional}")
                
                elif opcao == "2":
    
                    cpf_prof = input("CPF do Profissional para ser excluída: ")
                    excluir_prof = self.__controlador.remover_profissional(cpf_prof)
                    print(f"Resultado: {excluir_prof}")
    
                elif opcao == "3":
    
                    cpf_atual = input("CPF do Profissional para ser alterado: ")
                    if self.__controlador.verificar_existencia_profissional(cpf_atual):
                        print("CPF Encontrado! Vamos alterar o cadastro: ")
                        novo_nome = input("Nome do Profissional: ")
                        novo_cpf = input("CPF do Profissional: ")
                        novo_telefone = input("Telefone do Profissional: ")
                        novo_registro = input("Registro do Profissional: ")  
                        nova_especialidade = input("A especialidade do Profissional:")   
    
                        alterar_profissional = self.__controlador.alterar_dados_pessoa(cpf_atual,novo_nome, novo_cpf, novo_telefone,novo_registro,novo_telefone)
                    print(f"Resultado: {alterar_profissional}")
                
                elif opcao == "4":
                    profissionais = self.__controlador.mostrar_profissionais()
                    if not profissionais:
                        print("Não há profissionais cadastrados")
                    else:
                        print("\n--Lista Profissionais--")
                        for indice,prof in enumerate(profissionais):
                            print(f"{indice + 1} {prof}")
        
                elif opcao =="0":
                    print("Retornando ao menu principal...")
                    break
    
                else:
                    print("Escolha Inválida! Tente Novamente!")  
    