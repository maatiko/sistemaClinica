from exception.excecoes import ErroClinica


class TelaConsulta:

    def __init__(self, controlador_consulta):
        self.__controlador = controlador_consulta

    def iniciar(self):
        while True:
            print("\n===== MENU DE CONSULTAS =====")
            print("1 - Agendar consulta")
            print("2 - Alterar consulta")
            print("3 - Excluir consulta")
            print("4 - Listar consultas")
            print("5 - Gerenciar procedimentos")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "0":
                return

            try:
                if opcao == "1":
                    self.agendar_consulta()
                elif opcao == "2":
                    self.alterar_consulta()
                elif opcao == "3":
                    self.excluir_consulta()
                elif opcao == "4":
                    self.listar_consultas()
                elif opcao == "5":
                    self.menu_procedimentos()
                else:
                    print("Opção inválida.")

            except (ErroClinica, ValueError, TypeError, AttributeError) as erro:
                print(f"\n[Erro] {erro}")

    def agendar_consulta(self):
        nome_clinica = input("Nome da clínica: ").strip()
        cpf = input("CPF do paciente: ").strip()
        registro = input("Registro do profissional: ").strip()
        tipo = input("Tipo de consulta: ").strip()
        valor = input("Valor da consulta: ").strip()
        data = input("Data (DD/MM/AAAA): ").strip()
        horario = input("Horário (HH:MM): ").strip()

        if not all([
            nome_clinica, cpf, registro, tipo, valor, data, horario
        ]):
            raise ValueError("Todos os campos são obrigatórios.")

        valor_convertido = self.converter_valor(valor)

        self.__controlador.agendar_consulta(
            nome_clinica,
            cpf,
            registro,
            tipo,
            valor_convertido,
            data,
            horario,
        )
        print("Consulta agendada com sucesso.")

    def alterar_consulta(self):
        cpf = input("CPF do paciente da consulta: ").strip()
        data_atual = input("Data atual (DD/MM/AAAA): ").strip()
        horario_atual = input("Horário atual (HH:MM): ").strip()

        nome_clinica = input("Novo nome da clínica: ").strip()
        registro = input("Novo registro do profissional: ").strip()
        tipo = input("Novo tipo de consulta: ").strip()
        valor = input("Novo valor da consulta: ").strip()
        nova_data = input("Nova data (DD/MM/AAAA): ").strip()
        novo_horario = input("Novo horário (HH:MM): ").strip()

        if not all([
            cpf, data_atual, horario_atual, nome_clinica,
            registro, tipo, valor, nova_data, novo_horario
        ]):
            raise ValueError("Todos os campos são obrigatórios.")

        valor_convertido = self.converter_valor(valor)

        self.__controlador.alterar_dados_consulta(
            cpf,
            data_atual,
            horario_atual,
            nome_clinica,
            registro,
            tipo,
            valor_convertido,
            nova_data,
            novo_horario,
        )
        print("Consulta alterada com sucesso.")

    def excluir_consulta(self):
        cpf = input("CPF do paciente: ").strip()
        data = input("Data da consulta (DD/MM/AAAA): ").strip()
        horario = input("Horário da consulta (HH:MM): ").strip()

        if not all([cpf, data, horario]):
            raise ValueError("Todos os campos são obrigatórios.")

        self.__controlador.excluir_consulta(cpf, data, horario)
        print("Consulta excluída com sucesso.")

    def listar_consultas(self):
        consultas = self.__controlador.listar_consultas()

        if not consultas:
            print("Nenhuma consulta cadastrada.")
            return

        print("\n===== CONSULTAS CADASTRADAS =====")
        for consulta in consultas:
            print(consulta)

    def menu_procedimentos(self):
        while True:
            print("\n===== PROCEDIMENTOS =====")
            print("1 - Adicionar procedimento")
            print("2 - Alterar procedimento")
            print("3 - Excluir procedimento")
            print("4 - Listar procedimentos")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "0":
                return

            try:
                if opcao == "1":
                    self.adicionar_procedimento()
                elif opcao == "2":
                    self.alterar_procedimento()
                elif opcao == "3":
                    self.excluir_procedimento()
                elif opcao == "4":
                    self.listar_procedimentos()
                else:
                    print("Opção inválida.")

            except (ErroClinica, ValueError, TypeError, AttributeError) as erro:
                print(f"\n[Erro] {erro}")

    def adicionar_procedimento(self):
        cpf, data, horario = self.dados_identificacao_consulta()
        descricao = input("Descrição do procedimento: ").strip()
        custo = input("Custo do procedimento: ").strip()
        registro = input("Registro do profissional responsável: ").strip()

        if not all([descricao, custo, registro]):
            raise ValueError("Todos os campos são obrigatórios.")

        custo_convertido = self.converter_valor(custo)

        self.__controlador.adicionar_procedimento_na_consulta(
            cpf, data, horario, descricao, custo_convertido, registro
        )
        print("Procedimento adicionado com sucesso.")

    def alterar_procedimento(self):
        cpf, data, horario = self.dados_identificacao_consulta()
        descricao_atual = input("Descrição atual: ").strip()
        nova_descricao = input("Nova descrição: ").strip()
        novo_custo = input("Novo custo: ").strip()
        novo_registro = input("Novo registro profissional: ").strip()

        if not all([
            descricao_atual, nova_descricao, novo_custo, novo_registro
        ]):
            raise ValueError("Todos os campos são obrigatórios.")

        custo_convertido = self.converter_valor(novo_custo)

        self.__controlador.alterar_procedimento_da_consulta(
            cpf,
            data,
            horario,
            descricao_atual,
            nova_descricao,
            custo_convertido,
            novo_registro,
        )
        print("Procedimento alterado com sucesso.")

    def excluir_procedimento(self):
        cpf, data, horario = self.dados_identificacao_consulta()
        descricao = input("Descrição do procedimento a excluir: ").strip()

        if not descricao:
            raise ValueError("A descrição do procedimento é obrigatória.")

        self.__controlador.excluir_procedimento_da_consulta(
            cpf, data, horario, descricao
        )
        print("Procedimento excluído com sucesso.")

    def listar_procedimentos(self):
        cpf, data, horario = self.dados_identificacao_consulta()

        procedimentos = self.__controlador.listar_procedimentos_da_consulta(
            cpf, data, horario
        )

        if not procedimentos:
            print("Nenhum procedimento associado a essa consulta.")
            return

        print("\n===== PROCEDIMENTOS DA CONSULTA =====")
        for procedimento in procedimentos:
            print(procedimento)

    @staticmethod
    def dados_identificacao_consulta():
        cpf = input("CPF do paciente: ").strip()
        data = input("Data da consulta (DD/MM/AAAA): ").strip()
        horario = input("Horário da consulta (HH:MM): ").strip()

        if not all([cpf, data, horario]):
            raise ValueError(
                "CPF, data e horário são obrigatórios."
            )

        return cpf, data, horario

    @staticmethod
    def converter_valor(valor_texto):
        valor_normalizado = valor_texto.strip().replace(",", ".")

        try:
            valor = float(valor_normalizado)
        except (ValueError, TypeError):
            raise ValueError("Informe um valor numérico válido.")

        if valor <= 0:
            raise ValueError("O valor deve ser maior que zero.")

        return valor