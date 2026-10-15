from datetime import datetime

from exception.excecoes import ErroClinica


class TelaClinica:

    def __init__(self, controlador_clinica):
        self.__controlador = controlador_clinica

    def iniciar(self):
        while True:
            print("\n===== MENU DE CLÍNICAS =====")
            print("1 - Cadastrar clínica")
            print("2 - Alterar clínica")
            print("3 - Excluir clínica")
            print("4 - Listar clínicas")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "0":
                return

            try:
                if opcao == "1":
                    self.cadastrar_clinica()
                elif opcao == "2":
                    self.alterar_clinica()
                elif opcao == "3":
                    self.excluir_clinica()
                elif opcao == "4":
                    self.listar_clinicas()
                else:
                    print("Opção inválida.")

            except (ErroClinica, ValueError, TypeError, AttributeError) as erro:
                print(f"\n[Erro] {erro}")

    def cadastrar_clinica(self):
        nome = input("Nome: ").strip()
        localizacao = input("Localização: ").strip()
        descricao = input("Descrição: ").strip()
        abertura = input("Horário de abertura (HH:MM): ").strip()
        fechamento = input("Horário de fechamento (HH:MM): ").strip()

        if not all([nome, localizacao, descricao, abertura, fechamento]):
            raise ValueError("Todos os campos são obrigatórios.")

        self.validar_horario(abertura)
        self.validar_horario(fechamento)

        self.__controlador.adicionar_clinica(
            nome, localizacao, descricao, abertura, fechamento
        )
        print("Clínica cadastrada com sucesso.")

    def alterar_clinica(self):
        nome_atual = input("Nome atual da clínica: ").strip()
        novo_nome = input("Novo nome: ").strip()
        localizacao = input("Nova localização: ").strip()
        descricao = input("Nova descrição: ").strip()
        abertura = input("Novo horário de abertura (HH:MM): ").strip()
        fechamento = input("Novo horário de fechamento (HH:MM): ").strip()

        if not all([
            nome_atual, novo_nome, localizacao,
            descricao, abertura, fechamento
        ]):
            raise ValueError("Todos os campos são obrigatórios.")

        self.validar_horario(abertura)
        self.validar_horario(fechamento)

        self.__controlador.alterar_dados_clinica(
            nome_atual,
            novo_nome,
            localizacao,
            descricao,
            abertura,
            fechamento,
        )
        print("Clínica alterada com sucesso.")

    def excluir_clinica(self):
        nome = input("Nome da clínica que deseja excluir: ").strip()

        if not nome:
            raise ValueError("O nome da clínica é obrigatório.")

        self.__controlador.excluir_clinica(nome)
        print("Clínica excluída com sucesso.")

    def listar_clinicas(self):
        clinicas = self.__controlador.listar_clinicas()

        if not clinicas:
            print("Nenhuma clínica cadastrada.")
            return

        print("\n===== CLÍNICAS CADASTRADAS =====")
        for clinica in clinicas:
            print(clinica)

    @staticmethod
    def validar_horario(horario):
        try:
            datetime.strptime(horario, "%H:%M")
        except (ValueError, TypeError):
            raise ValueError(
                "Horário inválido. Informe no formato HH:MM."
            )