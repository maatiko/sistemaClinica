from datetime import datetime

from exception.excecoes import ErroClinica


class TelaPessoa:

    def __init__(self, controlador_pessoa):
        self.__controlador = controlador_pessoa

    def iniciar(self):
        while True:
            print("\n===== MENU DE PESSOAS =====")
            print("1 - Pacientes")
            print("2 - Profissionais")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "0":
                return
            elif opcao == "1":
                self.menu_pacientes()
            elif opcao == "2":
                self.menu_profissionais()
            else:
                print("Opção inválida.")

    def menu_pacientes(self):
        while True:
            print("\n===== MENU DE PACIENTES =====")
            print("1 - Cadastrar paciente")
            print("2 - Alterar paciente")
            print("3 - Excluir paciente")
            print("4 - Listar pacientes")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "0":
                return

            try:
                if opcao == "1":
                    self.cadastrar_paciente()
                elif opcao == "2":
                    self.alterar_paciente()
                elif opcao == "3":
                    self.excluir_paciente()
                elif opcao == "4":
                    self.listar_pacientes()
                else:
                    print("Opção inválida.")

            except (ErroClinica, ValueError, TypeError, AttributeError) as erro:
                print(f"\n[Erro] {erro}")

    def menu_profissionais(self):
        while True:
            print("\n===== MENU DE PROFISSIONAIS =====")
            print("1 - Cadastrar profissional")
            print("2 - Alterar profissional")
            print("3 - Excluir profissional")
            print("4 - Listar profissionais")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "0":
                return

            try:
                if opcao == "1":
                    self.cadastrar_profissional()
                elif opcao == "2":
                    self.alterar_profissional()
                elif opcao == "3":
                    self.excluir_profissional()
                elif opcao == "4":
                    self.listar_profissionais()
                else:
                    print("Opção inválida.")

            except (ErroClinica, ValueError, TypeError, AttributeError) as erro:
                print(f"\n[Erro] {erro}")

    def cadastrar_paciente(self):
        nome = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        telefone = input("Telefone: ").strip()
        nascimento = input("Data de nascimento (DD/MM/AAAA): ").strip()

        if not all([nome, cpf, telefone, nascimento]):
            raise ValueError("Todos os campos são obrigatórios.")

        self.validar_data(nascimento)

        self.__controlador.adicionar_paciente(
            nome, cpf, telefone, nascimento
        )
        print("Paciente cadastrado com sucesso.")

    def alterar_paciente(self):
        cpf_atual = input("CPF atual do paciente: ").strip()
        novo_nome = input("Novo nome: ").strip()
        novo_cpf = input("Novo CPF: ").strip()
        novo_telefone = input("Novo telefone: ").strip()
        nascimento = input(
            "Nova data de nascimento (DD/MM/AAAA): "
        ).strip()

        if not all([
            cpf_atual, novo_nome, novo_cpf, novo_telefone, nascimento
        ]):
            raise ValueError("Todos os campos são obrigatórios.")

        data_convertida = self.validar_data(nascimento)

        self.__controlador.alterar_dados_pessoa(
            cpf_atual,
            novo_nome,
            novo_cpf,
            novo_telefone,
            data_convertida,
            None,
            None,
        )
        print("Paciente alterado com sucesso.")

    def excluir_paciente(self):
        cpf = input("CPF do paciente que deseja excluir: ").strip()

        if not cpf:
            raise ValueError("O CPF é obrigatório.")

        self.__controlador.remover_paciente(cpf)
        print("Paciente excluído com sucesso.")

    def listar_pacientes(self):
        pacientes = self.__controlador.mostrar_pacientes()

        if not pacientes:
            print("Nenhum paciente cadastrado.")
            return

        print("\n===== PACIENTES CADASTRADOS =====")
        for paciente in pacientes:
            print(paciente)

    def cadastrar_profissional(self):
        nome = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        telefone = input("Telefone: ").strip()
        especialidade = input("Especialidade: ").strip()
        registro = input("Registro profissional: ").strip()

        if not all([nome, cpf, telefone, especialidade, registro]):
            raise ValueError("Todos os campos são obrigatórios.")

        self.__controlador.adicionar_profissional(
            nome, cpf, telefone, especialidade, registro
        )
        print("Profissional cadastrado com sucesso.")

    def alterar_profissional(self):
        cpf_atual = input("CPF atual do profissional: ").strip()
        novo_nome = input("Novo nome: ").strip()
        novo_cpf = input("Novo CPF: ").strip()
        novo_telefone = input("Novo telefone: ").strip()
        especialidade = input("Nova especialidade: ").strip()
        registro = input("Novo registro profissional: ").strip()

        if not all([
            cpf_atual, novo_nome, novo_cpf,
            novo_telefone, especialidade, registro
        ]):
            raise ValueError("Todos os campos são obrigatórios.")

        self.__controlador.alterar_dados_pessoa(
            cpf_atual,
            novo_nome,
            novo_cpf,
            novo_telefone,
            None,
            especialidade,
            registro,
        )
        print("Profissional alterado com sucesso.")

    def excluir_profissional(self):
        cpf = input("CPF do profissional que deseja excluir: ").strip()

        if not cpf:
            raise ValueError("O CPF é obrigatório.")

        self.__controlador.remover_profissional(cpf)
        print("Profissional excluído com sucesso.")

    def listar_profissionais(self):
        profissionais = self.__controlador.mostrar_profissionais()

        if not profissionais:
            print("Nenhum profissional cadastrado.")
            return

        print("\n===== PROFISSIONAIS CADASTRADOS =====")
        for profissional in profissionais:
            print(profissional)

    @staticmethod
    def validar_data(data_texto):
        try:
            return datetime.strptime(data_texto, "%d/%m/%Y").date()
        except (ValueError, TypeError):
            raise ValueError(
                "Data inválida. Informe no formato DD/MM/AAAA."
            )