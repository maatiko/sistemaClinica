from controller.controladorClinica import ControladorClinica
from controller.controladorConsulta import ControladorConsulta
from controller.controladorPagamento import ControladorPagamento
from controller.controladorRelatorio import ControladorRelatorio
from controller.controladorPessoa import ControladorPessoa
from view.telaSistema import TelaSistema


class ControladorSistema():
    def __init__(self):
        self.__controlador_pessoa = ControladorPessoa()
        self.__controlador_clinica = ControladorClinica()
        self.__controlador_consulta = ControladorConsulta(self)
        self.__controlador_pagamento = ControladorPagamento()
        self.__controlador_relatorio = ControladorRelatorio(self)
        self.__tela_sistema = TelaSistema(self)
   

    def iniciar(self):
        self.__tela_sistema.iniciar()

    def abrir_menu(self,opcao):
        if opcao == "1":
            self.__controlador_clinica.abrir_tela()
        elif opcao == "2":
            self.__controlador_pessoa.abrir_tela()
        elif opcao == "3":
            self.__controlador_consulta.abrir_tela()
        elif opcao  == "4":
            pass #menu de pagamento
        elif opcao =="5":
            self.__controlador_relatorio.abrir_tela()
        else:
            print("\n[Erro] Opção inválida!")

    #Pontes para o Controlador Consulta
    def buscar_clinica(self, nome):
        return self.__controlador_clinica.buscar_clinica_nome(nome)

    def buscar_paciente_cpf(self, cpf):
        return self.__controlador_pessoa.buscar_paciente_cpf(cpf)

    def buscar_profissional_registro(self, registro):
        return self.__controlador_pessoa.buscar_profissional_registro(registro)

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
        return self.__controlador_consulta

    @property
    def controlador_pagamento(self):
        return self.__controlador_pagamento