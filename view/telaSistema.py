from datetime import datetime
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

                adicionar_clinica = self.__sistema.controlador_clinica.adicionar_clinica(nome, cidade, descricao, abertura, fechamento)
                print(f"\n[Resultado]: {adicionar_clinica}")

            elif opcao == "2":
                nome = input("Nome da Clínica para ser excluída: ")
                excluir_clinica = self.__sistema.controlador_clinica.excluir_clinica(nome)
                print(f"Resultado: {excluir_clinica}")

            elif opcao == "3":
                nome_atual = input("Nome da Clínica para ser alterada: ").strip()
                if self.__sistema.controlador_clinica.verificar_existencia(nome):
                    print("Cliníca Encontrada! Digite os novos dados:")
                    novo_nome = input("Digite o novo nome: ")
                    nova_localizacao = input("Digite a nova localização/cidade: ")
                    nova_descricao = input("Digite a nova descrição: ")
                    novo_horario_abertura = input("Digite o novo horário de abertura: ")
                    novo_horario_fechamento = input("Digite o novo horário de fechamento: ")
                    self.__sistema.controlador_clinica.alterar_dados_clinica(nome_atual,novo_nome,nova_localizacao,nova_descricao,novo_horario_abertura,novo_horario_fechamento)
                    print("Dados Alterados com Sucesso!")
                else:
                    #erro que não existe a clínica que está se procurando
                    pass
            elif opcao == "4":
                clinicas = self.__sistema.controlador_clinica.listar_clinicas()
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
                adicionar_paciente = self.__sistema.controlador_pessoa.adicionar_paciente(nome, cpf,telefone,data_nascimento )
                print(f"\n[Resultado]: {adicionar_paciente}")
            

            elif opcao == "2":

                cpf_pac = input("CPF do Paciente para ser excluída: ")
                excluir_paciente = self.__sistema.controlador_pessoa.remover_paciente(cpf_pac)
                print(f"Resultado: {excluir_paciente}")

            elif opcao == "3":

                cpf_atual = input("CPF do Paciente para ser alterado: ")
                if self.__sistema.controlador_pessoa.verificar_existencia_paciente(cpf_atual):
                    print("CPF Encontrado! Vamos alterar o cadastro: ")
                    novo_nome = input("Nome do Paciente: ")
                    novo_cpf = input("CPF do Paciente: ")
                    novo_telefone = input("Telefone do paciente: ")
                    nova_data_nascimento = input("Data de Nascimento do Paciente: ")     
                    data_convertida = datetime.strptime(nova_data_nascimento,"%d/%m/%Y").date()

                    alterar_paciente = self.__sistema.controlador_pessoa.alterar_dados_pessoa(cpf_atual,novo_nome, novo_cpf, novo_telefone,data_convertida)
                print(f"Resultado: {alterar_paciente}")
            
            elif opcao == "4":
                pacientes = self.__sistema.controlador_clinica.listar_pacientes()
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
                adicionar_profissional = self.__sistema.controlador_pessoa.adicionar_profissional(nome, cpf,telefone,registro,especialidade )
                print(f"\n[Resultado]: {adicionar_profissional}")
            
            elif opcao == "2":

                cpf_prof = input("CPF do Profissional para ser excluída: ")
                excluir_prof = self.__sistema.controlador_pessoa.remover_profissional(cpf_prof)
                print(f"Resultado: {excluir_prof}")

            elif opcao == "3":

                cpf_atual = input("CPF do Profissional para ser alterado: ")
                if self.__sistema.controlador_pessoa.verificar_existencia_profissional(cpf_atual):
                    print("CPF Encontrado! Vamos alterar o cadastro: ")
                    novo_nome = input("Nome do Profissional: ")
                    novo_cpf = input("CPF do Profissional: ")
                    novo_telefone = input("Telefone do Profissional: ")
                    novo_registro = input("Registro do Profissional: ")  
                    nova_especialidade = input("A especialidade do Profissional:")   

                    alterar_profissional = self.__sistema.controlador_pessoa.alterar_dados_pessoa(cpf_atual,novo_nome, novo_cpf, novo_telefone,novo_registro,novo_telefone)
                print(f"Resultado: {alterar_profissional}")
            
            elif opcao == "4":
                profissionais = self.__sistema.controlador_clinica.listar_profissionais()
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
                self.__sistema.agendar_consulta(nome_clinica, cpf_pac, registro_prof, tipo_consulta, valor, data_cons,horario_cons)
                print(f"\n[Resultado]: ")

            elif opcao == "2":

                cpf_pac = input("CPF do paciente para a consulta ser excluída: ")
                data_consulta = input("Data da consulta a ser cancelada (DD/MM/AAAA): ")
                horario_consulta = input("Horário da consulta a ser cancelada (HH:MM): ")
                
                excluir_consulta = self.__sistema.controlador_sistema.excluir_consulta(cpf_pac,data_consulta,horario_consulta)
                print(f"Resultado: {excluir_consulta}")

            elif opcao == "3":
                    print("Primeiro, identifique a consulta atual:")
                    cpf_paciente = input("CPF do Paciente: ")
                    data_atual = input("Data atual da consulta (DD/MM/AAAA): ")
                    horario_atual = input("Horário atual da consulta (HH:MM): ")                
                    if self.__sistema.controlador_consulta.verificar_existencia_consulta(cpf_paciente, data_atual, horario_atual ):
                        print("Consulta achada, vamos reagendá-lá: ")
                        nova_data = input("Nova Data (DD/MM/AAAA): ")
                        novo_horario = input("Novo Horário (HH:MM): ")
                        self.__sistema.alterar_consulta(cpf_paciente, data_atual, horario_atual, nova_data, novo_horario)
                        print("Reagendamento feito com sucesso")
            elif opcao == "4":
                consultas = self.__sistema.controlador_consultar.listar_consultas()
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

    def menu_pagamento(self):
        pass

    def menu_relatorio(self):
        pass