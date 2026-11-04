from controller.controlador_clinica import ControladorClinica
from controller.controlador_atendimento import ControladorAntedimento
from controller.controlador_pagamento import ControladorPagamento
from controller.controlador_relatorio import ControladorRelatorio
from controller.controlador_pessoa import ControladorPessoa
from controller.controlador_tipo_atendimento import ControladorTipoAtendimento
from view.tela_sistema import TelaSistema


class ControladorSistema():
    def __init__(self):
        self.__controlador_pessoa = ControladorPessoa()
        self.__controlador_clinica = ControladorClinica()
        self.__controlador_atendimento = ControladorAntedimento(self)
        self.__controlador_pagamento = ControladorPagamento(self)
        self.__controlador_relatorio = ControladorRelatorio(self)
        self.__controlador_tipo_atendimento = ControladorTipoAtendimento()
        self.__tela_sistema = TelaSistema(self)

    def iniciar(self):
        try:
            self.__tela_sistema.iniciar()
        except Exception as erro:
            print(f"\n[Erro] Não foi possível iniciar o sistema: {erro}")

    def abrir_menu(self, opcao):
        try:
            if opcao == "1":
                self.__controlador_clinica.abrir_tela()
            elif opcao == "2":
                self.__controlador_pessoa.abrir_tela()
            elif opcao == "3":
                self.__controlador_tipo_atendimento.abrir_tela()
            elif opcao == "4":
                self.__controlador_atendimento.abrir_tela()
            elif opcao == "5":
                self.__controlador_pagamento.abrir_tela()
            elif opcao == "6":
                self.__controlador_relatorio.abrir_tela()
            
            else:
                print("\n[Erro] Opção inválida!")

        except ValueError as erro:
            print(f"\n[Erro] Valor inválido: {erro}")
        except TypeError as erro:
            print(f"\n[Erro] Tipo de dado inválido: {erro}")
        except AttributeError as erro:
            print(f"\n[Erro] Problema ao acessar um método ou atributo: {erro}")
        except Exception as erro:
            print(f"\n[Erro] Não foi possível abrir o menu: {erro}")

    # Pontes para o Controlador Consulta
    def buscar_clinica(self, nome):
        return self.__controlador_clinica.buscar_clinica_nome(nome)

    def buscar_paciente_cpf(self, cpf):
        return self.__controlador_pessoa.buscar_paciente_cpf(cpf)

    def buscar_profissional_registro(self, registro):
        return self.__controlador_pessoa.buscar_profissional_registro(registro)

    def buscar_tipo_atendimento(self, nome):
        return self.__controlador_tipo_atendimento.buscar_tipo_atendimento(nome)

    def buscar_consulta(self, cpf, data_str, horario_str):
        return self.__controlador_consulta.buscar_consulta(cpf, data_str, horario_str)

    def obter_todas_consultas(self):
        return self.__controlador_consulta.listar_consultas()

    @property
    def controlador_clinica(self):
        return self.__controlador_clinica

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    @property
    def controlador_consulta(self):
        return self.__controlador_atendimento

    @property
    def controlador_pagamento(self):
        return self.__controlador_pagamento

    @property
    def controlador_tipo_atendimento(self):
        return self.__controlador_tipo_atendimento