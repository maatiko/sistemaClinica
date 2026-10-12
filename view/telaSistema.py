from controller import controladorClinica
from controller import controladorConsulta
from controller import controladorPagamento
from controller import controladorPessoa
from controller import controladorRelatorio

class TelaSistema:
    def __init__(self,controlador_clinica,controlador_consulta,controlador_pagamento,controlador_pessoa,controlador_relatorio):
        self.__controlador_clinica = controlador_clinica
        self.__controlador_consulta = controlador_consulta
        self.__controlador_pagamento = controlador_pagamento
        self.__controlador_pessoa = controlador_pessoa
        self.__controlador_relatorio = controlador_relatorio

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

            opcao = input("Selecione uma opção:")

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
            print("\n--- Cadastro de Clínica ---")
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

       
                adicionar_clinica = self.__controlador_clinica.adicionar_clinica(
                nome, cidade, descricao, abertura, fechamento
                )
                print(f"\n[Resultado]: {adicionar_clinica}")
            elif opcao == "2":
                nome = input("Nome da Clínica para ser excluída: ")
                excluir_clinica = self.__controlador_clinica.excluir_clinica(nome)
                print(f"Resultado: {excluir_clinica}")


    def menu_paciente(self):
        pass

    def menu_profissional(self):
        pass

    def menu_consulta(self):
        pass

    def menu_pagamento(self):
        pass

    def menu_relatorio(self):
        pass
