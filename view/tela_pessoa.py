from datetime import datetime
from exception.excecoes import ErroClinica


class TelaPessoa:
    def __init__(self, controlador_pes):
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
            opcao = input("Insira sua opção: ").strip()

            if opcao == "1":
                try:
                    while True:
                        nome = input("Nome do Paciente: ")
                        if (
                            not nome.strip()
                            or len(nome.strip()) < 2
                            or not any(
                                letra.isalpha() for letra in nome
                            )
                        ):
                            print(
                                "ERRO: Nome inválido. "
                                "Digite um nome com letras. "
                                "Tente novamente."
                            )
                            continue
                        break

                    while True:
                        cpf = input("CPF do Paciente: ")
                        if not cpf.strip():
                            print("ERRO: O CPF é obrigatório.")
                            continue
                        if not cpf.isdigit() or len(cpf) != 11:
                            print(
                                "ERRO: CPF inválido. Digite os "
                                "11 números do CPF."
                            )
                            continue
                        break

                    while True:
                        telefone = input("Telefone do paciente: ")
                        if not telefone.strip():
                            print("ERRO: O telefone é obrigatório.")
                            continue
                        if (
                            not telefone.isdigit()
                            or len(telefone) not in (10, 11)
                        ):
                            print(
                                "ERRO: Telefone inválido. Digite "
                                "DDD e número, apenas com números."
                            )
                            continue
                        break

                    while True:
                        data_nascimento = input(
                            "Data de Nascimento do Paciente "
                            "(DD/MM/AAAA): "
                        )
                        try:
                            data_convertida = datetime.strptime(
                                data_nascimento, "%d/%m/%Y"
                            ).date()
                            break
                        except ValueError:
                            print(
                                "ERRO: Data inválida. Digite "
                                "no formato DD/MM/AAAA."
                            )

                    self.__controlador.adicionar_paciente(
                        nome, cpf, telefone, data_convertida
                    )
                    print("\nSucesso em adicionar o paciente!")

                except (ErroClinica, ValueError) as e:
                    print(f"\nERRO: {e}")

            elif opcao == "2":
                try:
                    cpf_pac = input(
                        "CPF do Paciente para ser excluído: "
                    )
                    self.__controlador.remover_paciente(cpf_pac)
                    print("Sucesso em excluir o paciente!")

                except (ErroClinica, ValueError) as e:
                    print(f"Erro: {e}")

            elif opcao == "3":
                try:
                    cpf_atual = input(
                        "CPF do Paciente para ser alterado: "
                    )
                    self.__controlador.verificar_existencia_paciente(
                        cpf_atual
                    )
                    print(
                        "CPF encontrado! Vamos alterar o cadastro:"
                    )

                    novo_nome = input("Nome do Paciente: ")
                    novo_cpf = input("CPF do Paciente: ")
                    novo_telefone = input("Telefone do paciente: ")
                    nova_data_nascimento = input(
                        "Data de Nascimento do Paciente: "
                    )

                    data_convertida = datetime.strptime(
                        nova_data_nascimento, "%d/%m/%Y"
                    ).date()

                    self.__controlador.alterar_dados_pessoa(
                        cpf_atual,
                        novo_nome,
                        novo_cpf,
                        novo_telefone,
                        data_convertida
                    )
                    print(
                        "Sucesso em alterar os dados do paciente!"
                    )

                except (ErroClinica, ValueError) as e:
                    print(f"Erro: {e}")

            elif opcao == "4":
                pacientes = self.__controlador.mostrar_pacientes()

                if not pacientes:
                    print("Não há pacientes cadastrados.")
                else:
                    print("\n--Lista Pacientes--")
                    for indice, paciente in enumerate(pacientes):
                        print(f"{indice + 1} {paciente}")

            elif opcao == "0":
                print("Retornando ao menu principal...")
                break

            else:
                print("Escolha inválida! Tente novamente!")

    def menu_profissional(self):
        while True:
            print("\n--- Menu de Profissional ---")
            print("Escolha uma opção:")
            print("1. Cadastrar Profissional")
            print("2. Excluir Profissional")
            print("3. Alterar Profissional")
            print("4. Listar Profissionais")
            print("0. Retornar ao menu")
            opcao = input("Insira sua opção: ").strip()

            if opcao == "1":
                try:
                    while True:
                        nome = input("Nome do Profissional: ")
                        if (
                            not nome.strip()
                            or len(nome.strip()) < 2
                            or not any(
                                letra.isalpha() for letra in nome
                            )
                        ):
                            print(
                                "ERRO: Nome inválido. "
                                "Digite um nome com letras."
                            )
                            continue
                        break

                    while True:
                        cpf = input("CPF do Profissional: ")
                        if not cpf.strip():
                            print("ERRO: O CPF é obrigatório.")
                            continue
                        if not cpf.isdigit() or len(cpf) != 11:
                            print(
                                "ERRO: CPF inválido. Digite os "
                                "11 números do CPF."
                            )
                            continue
                        break

                    while True:
                        telefone = input("Telefone do Profissional: ")
                        if not telefone.strip():
                            print("ERRO: O telefone é obrigatório.")
                            continue
                        if (
                            not telefone.isdigit()
                            or len(telefone) not in (10, 11)
                        ):
                            print(
                                "ERRO: Telefone inválido. Digite "
                                "DDD e número, apenas com números."
                            )
                            continue
                        break

                    while True:
                        registro = input(
                            "Registro do Profissional: "
                        )
                        if len(registro.strip()) < 2:
                            print(
                                "ERRO: Registro inválido. "
                                "Digite novamente."
                            )
                            continue
                        break

                    while True:
                        especialidade = input(
                            "Especialidade do Profissional: "
                        )
                        if len(especialidade.strip()) < 2:
                            print(
                                "ERRO: Especialidade inválida. "
                                "Digite novamente."
                            )
                            continue
                        break

                    self.__controlador.adicionar_profissional(
                        nome,
                        cpf,
                        telefone,
                        especialidade,
                        registro
                    )
                    print(
                        "\nSucesso em adicionar o profissional!"
                    )

                except (ErroClinica, ValueError) as e:
                    print(f"\nERRO: {e}")

            elif opcao == "2":
                try:
                    cpf_prof = input(
                        "CPF do Profissional para ser excluído: "
                    )
                    self.__controlador.remover_profissional(cpf_prof)
                    print("Sucesso em remover o profissional!")

                except (ErroClinica, ValueError) as e:
                    print(f"Erro: {e}")

            elif opcao == "3":
                try:
                    cpf_atual = input(
                        "CPF do Profissional para ser alterado: "
                    )
                    self.__controlador.verificar_existencia_profissional(
                        cpf_atual
                    )
                    print(
                        "CPF encontrado! Vamos alterar o cadastro:"
                    )

                    novo_nome = input("Nome do Profissional: ")
                    novo_cpf = input("CPF do Profissional: ")
                    novo_telefone = input("Telefone do Profissional: ")
                    novo_registro = input(
                        "Registro do Profissional: "
                    )
                    nova_especialidade = input(
                        "Especialidade do Profissional: "
                    )

                    self.__controlador.alterar_dados_pessoa(
                        cpf_atual,
                        novo_nome,
                        novo_cpf,
                        novo_telefone,
                        nova_especialidade=nova_especialidade,
                        novo_registro=novo_registro
                    )
                    print(
                        "Sucesso em alterar os dados do profissional!"
                    )

                except (ErroClinica, ValueError) as e:
                    print(f"Erro: {e}")

            elif opcao == "4":
                profissionais = (
                    self.__controlador.mostrar_profissionais()
                )

                if not profissionais:
                    print("Não há profissionais cadastrados.")
                else:
                    print("\n--Lista Profissionais--")
                    for indice, prof in enumerate(profissionais):
                        print(f"{indice + 1} {prof}")

            elif opcao == "0":
                print("Retornando ao menu principal...")
                break

            else:
                print("Escolha inválida! Tente novamente!")