class TelaPessoa:
    def __init__(self, controlador_pessoa):
        self.__controlador = controlador_pessoa

    def menu_principal_pessoa(self):
        while True:
            print("\n--- MENU DE PACIENTES E PROFISSIONAIS ---")
            print("1. Gerenciar Pacientes")
            print("2. Gerenciar Profissionais")
            print("0. Voltar ao Menu Principal")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.menu_pacientes()
            elif opcao == "2":
                self.menu_profissionais()
            elif opcao == "0":
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_pacientes(self):
        while True:
            print("\n--- MENU DE PACIENTES ---")
            print("1. Cadastrar Paciente")
            print("2. Remover Paciente")
            print("3. Alterar Dados do Paciente")
            print("4. Listar Pacientes")
            print("0. Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.cadastrar_paciente()
            elif opcao == "2":
                self.remover_paciente()
            elif opcao == "3":
                self.alterar_paciente()
            elif opcao == "4":
                self.listar_pacientes()
            elif opcao == "0":
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_profissionais(self):
        while True:
            print("\n--- MENU DE PROFISSIONAIS ---")
            print("1. Cadastrar Profissional")
            print("2. Remover Profissional")
            print("3. Alterar Dados do Profissional")
            print("4. Listar Profissionais")
            print("0. Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.cadastrar_profissional()
            elif opcao == "2":
                self.remover_profissional()
            elif opcao == "3":
                self.alterar_profissional()
            elif opcao == "4":
                self.listar_profissionais()
            elif opcao == "0":
                break
            else:
                print("Opção inválida! Tente novamente.")

    def cadastrar_paciente(self):
        print("\n--- CADASTRO DE PACIENTE ---")

        nome = input("Nome: ").strip()
        cpf = input("CPF (somente números): ").strip()
        telefone = input("Telefone (DDD + número): ").strip()

        from datetime import datetime

        while True:
            data_nascimento = input(
                "Data de nascimento (DD/MM/AAAA): "
            ).strip()

            try:
                data_convertida = datetime.strptime(
                    data_nascimento, "%d/%m/%Y"
                ).date()
                break
            except ValueError:
                print("Data inválida! Use o formato DD/MM/AAAA.")

        try:
            self.__controlador.adicionar_paciente(
                nome, cpf, telefone, data_convertida
            )
            print("Paciente cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro ao cadastrar paciente: {e}")

    def remover_paciente(self):
        print("\n--- REMOÇÃO DE PACIENTE ---")
        cpf = input("CPF do paciente: ").strip()

        try:
            self.__controlador.remover_paciente(cpf)
            print("Paciente removido com sucesso!")
        except ValueError as e:
            print(f"Erro ao remover paciente: {e}")

    def alterar_paciente(self):
        print("\n--- ALTERAÇÃO DE PACIENTE ---")

        cpf_atual = input("CPF atual do paciente: ").strip()
        novo_nome = input("Novo nome: ").strip()
        novo_cpf = input("Novo CPF (somente números): ").strip()
        novo_telefone = input(
            "Novo telefone (DDD + número): "
        ).strip()

        from datetime import datetime

        while True:
            data_nascimento = input(
                "Nova data de nascimento (DD/MM/AAAA): "
            ).strip()

            try:
                data_convertida = datetime.strptime(
                    data_nascimento, "%d/%m/%Y"
                ).date()
                break
            except ValueError:
                print("Data inválida! Use o formato DD/MM/AAAA.")

        try:
            self.__controlador.alterar_dados_pessoa(
                cpf_atual,
                novo_nome,
                novo_cpf,
                novo_telefone,
                nova_data_nascimento=data_convertida
            )
            print("Dados do paciente alterados com sucesso!")
        except ValueError as e:
            print(f"Erro ao alterar paciente: {e}")

    def listar_pacientes(self):
        pacientes = self.__controlador.mostrar_pacientes()

        print("\n--- LISTA DE PACIENTES ---")

        if not pacientes:
            print("Nenhum paciente cadastrado.")
            return

        for paciente in pacientes:
            print(paciente)

    def cadastrar_profissional(self):
        print("\n--- CADASTRO DE PROFISSIONAL ---")

        nome = input("Nome: ").strip()
        cpf = input("CPF (somente números): ").strip()
        telefone = input("Telefone (DDD + número): ").strip()
        especialidade = input("Especialidade: ").strip()
        registro = input("Registro profissional: ").strip()

        try:
            self.__controlador.adicionar_profissional(
                nome, cpf, telefone, especialidade, registro
            )
            print("Profissional cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro ao cadastrar profissional: {e}")

    def remover_profissional(self):
        print("\n--- REMOÇÃO DE PROFISSIONAL ---")
        cpf = input("CPF do profissional: ").strip()

        try:
            self.__controlador.remover_profissional(cpf)
            print("Profissional removido com sucesso!")
        except ValueError as e:
            print(f"Erro ao remover profissional: {e}")

    def alterar_profissional(self):
        print("\n--- ALTERAÇÃO DE PROFISSIONAL ---")

        cpf_atual = input("CPF atual do profissional: ").strip()
        novo_nome = input("Novo nome: ").strip()
        novo_cpf = input("Novo CPF (somente números): ").strip()
        novo_telefone = input(
            "Novo telefone (DDD + número): "
        ).strip()
        nova_especialidade = input("Nova especialidade: ").strip()
        novo_registro = input("Novo registro profissional: ").strip()

        try:
            self.__controlador.alterar_dados_pessoa(
                cpf_atual,
                novo_nome,
                novo_cpf,
                novo_telefone,
                nova_especialidade=nova_especialidade,
                novo_registro=novo_registro
            )
            print("Dados do profissional alterados com sucesso!")
        except ValueError as e:
            print(f"Erro ao alterar profissional: {e}")

    def listar_profissionais(self):
        profissionais = self.__controlador.mostrar_profissionais()

        print("\n--- LISTA DE PROFISSIONAIS ---")

        if not profissionais:
            print("Nenhum profissional cadastrado.")
            return

        for profissional in profissionais:
            print(profissional)