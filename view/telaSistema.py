class TelaSistema:
    def __init__(self,ControladorSistema):
        self.__sistema = ControladorSistema

    def iniciar(self):
        while True:
            print("\n"+"*" * 40)
            print("SISTEMA DE GESTÃO CLÍNICAS")
            print("-"*40)
            print("Gostaria de acessar:")
            print("1. Cadastro de Clínica")
            print("2. Cadastro de Pacientes ")
            print("3. Cadastro de Profissionais")
            print("4. Agendar Consulta")
            print("5. Registrar Pagamento")
            print("6. Exibir Relatórios")
            print("0. Sair")
            print("="*40)

            opcao = input("Selecione uma opção:").strip()

            if opcao == "1":
                self.menu_clinica()
            elif opcao == "2":
                self.menu_paciente()
            elif opcao == "3":
                self.menu_profissional()
            elif opcao == "4":
                self.menu_consulta()
            elif opcao == "5":
                self.menu_pagamento()
            elif opcao =="6":
                self.menu_relatorios()
            elif opcao == "0":
                print("\nEncerrando o sistema. Até logo!")
                break
            else:
                print("\n[Erro] Opção inválida! Tente novamente.")

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

                adicionar_clinica = self.__controlador_clinica.adicionar_clinica(nome, cidade, descricao, abertura, fechamento)
                print(f"\n[Resultado]: {adicionar_clinica}")

            elif opcao == "2":
                nome = input("Nome da Clínica para ser excluída: ")
                excluir_clinica = self.__controlador_clinica.excluir_clinica(nome)
                print(f"Resultado: {excluir_clinica}")

            elif opcao == "3":
                nome = input("Nome da Clínica para ser alterada: ")
                alterar_clinica = self.__controlador_clinica.alterar_clinica(nome)
                print(f"Resultado: {alterar_clinica}")

            elif opcao == "4":
                print(self.__controlador_clinica.listar_clinicas())

            elif opcao =="0":
                print("Retornando ao menu principal...")
                break

            else:
                print("Escolha Inválida! Tente Novamente!")
        
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
                data_nascimento = input("Data de Nascimento do Paciente: ")

                adicionar_paciente = self.__controlador_pessoa.adicionar_clinica(nome, cpf,telefone,data_nascimento )
                print(f"\n[Resultado]: {adicionar_paciente}")
            elif opcao == "2":

                nome = input("Nome do Paciente para ser excluída: ")
                excluir_clinica = self.__controlador_pessoa.excluir_paciente(nome)
                print(f"Resultado: {excluir_clinica}")

            elif opcao == "3":
                nome = input("Nome da Clínica para ser alterada: ")
                alterar_clinica = self.__controlador_pessoa.alterar_paciente(nome)
                print(f"Resultado: {alterar_clinica}")
            elif opcao == "4":
                print(self.__controlador_pessoa.listar_pacientes())
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
                registro = input("Registro do Profissional: ")
                especialidade = input("Especialidade do Profissional: ")

                adicionar_prof = self.__controlador_pessoa.adicionar_profissional(nome, cpf, telefone, registro, especialidade)
                print(f"\n[Resultado]: {adicionar_prof}")

            elif opcao == "2":
                nome = input("Registro do Profissional para ser excluída: ")
                excluir_prof = self.__controlador_pessoa.excluir_profissional(registro)
                print(f"Resultado: {excluir_prof}")

            elif opcao == "3":
                nome = input("Nome da Clínica para ser alterada: ")
                alterar_prof = self.__controlador_pessoa.alterar_profissional(nome)
                print("Resultado")
    
            elif opcao == "4":
                print(self.__controlador_pessoa.listar_profissionais())

            elif opcao =="0":
                print("Retornando ao menu principal...")
                break

            else:
                print("Escolha Inválida! Tente Novamente!")        

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
                nome = input("Nome da clínica: ")
                cidade = input("Cidade: ")
                descricao = input("Descrição: ")
                abertura = input("Horário de Abertura (HH:MM): ")
                fechamento = input("Horário de Fechamento (HH:MM): ")

                adicionar_clinica = self.__controlador_clinica.adicionar_clinica(nome, cidade, descricao, abertura, fechamento)
                print(f"\n[Resultado]: {adicionar_clinica}")
            elif opcao == "2":
                nome = input("Nome da Clínica para ser excluída: ")
                excluir_clinica = self.__controlador_clinica.excluir_clinica(nome)
                print(f"Resultado: {excluir_clinica}")
            elif opcao == "3":
                nome = input("Nome da Clínica para ser alterada: ")
                alterar_clinica = self.__controlador_clinica.alterar_clinica(nome)
                print("Resultado")
            elif opcao == "4":
                print(self.__controlador_clinica.listar_clinicas())
            elif opcao =="0":
                print("Retornando ao menu principal...")
                break
            else:
                print("Escolha Inválida! Tente Novamente!")

    def menu_pagamento(self):
        pass

    def menu_relatorio(self):
        pass
