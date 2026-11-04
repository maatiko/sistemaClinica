class TelaTipoAtendimento:
    def __init__(self, controlador_tipo_atendiemnto):
        self.__controlador = controlador_tipo_atendiemnto
    
    def menu_tipo_atendimento(self):
        while True:
            print("\n--- MENU DE TIPOS ATENDIMENTOS ---")
            print("1. Cadastrar Tipo de Atendimento")
            print("2. Remover Tipo de Atendimento")
            print("3. Alterar Dados do Tipo de Atendimento")
            print("4. Listar Tipos de Atendimentos")
            print("0. Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.cadastrar_tipo_atendimento()
            elif opcao == "2":
                self.remover_tipo_atendimento()
            elif opcao == "3":
                self.alterar_tipo_atendimento()
            elif opcao == "4":
                self.listar_tipo_atendimento()
            elif opcao == "0":
                break
            else:
                print("Opção inválida! Tente novamente.")        
    
    def cadastrar_tipo_atendimento(self):
        print("\n--- CADASTRO Do TIPO ATENDIMENTO ---")
        
        nome = input("Nome: ")
        descricao = input("Descrição do Tipo Atendimento: ")
        try:
            valor = float(input("O valor desse Tipo Atendimento: "))
            self.__controlador.adicionar_tipo_atendimento(
                nome, descricao, valor
            )
            print("Tipo Atendimento cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro ao cadastrar Tipo Atendimento: {e}")

    def remover_tipo_atendimento(self):
        print("\n--- REMOÇÃO DE TIPO ATENDIMENTO ---")
        nome = input("Nome do Tipo Atendimento: ")

        try:
            self.__controlador.remover_tipo_atendimento(nome)
            print("Tipo Atendimento removido com sucesso!")
        except ValueError as e:
            print(f"Erro ao remover paciente: {e}")

    def alterar_tipo_atendimento(self):
        print("\n--- ALTERAÇÃO DE TIPO ATENDIMENTO ---")

        nome_atual = input("Nome atual do Tipo de Atendimento: ").strip()
        novo_nome = input("Novo nome: ")
        nova_descricao = input("Nova descrição: ")

        try:
            novo_valor = float(input("Novo valor do Tipo Atendimento: "))
            self.__controlador.alterar_tipo_atendimento(
                nome_atual,
                novo_nome,
                nova_descricao,
                novo_valor,
            )
            print("Dados do paciente alterados com sucesso!")
        except ValueError as e:
            print(f"Erro ao alterar paciente: {e}")

    def listar_tipo_atendimento(self):
        tipos = self.__controlador.listar_tipo_atendimento()

        print("\n--- LISTA DE TIPO ATENDIMENTO ---")

        if not tipos:
            print("Nenhum Tipo de Atendimento cadastrado.")
            return

        for tipo in tipos:
            print(tipo)