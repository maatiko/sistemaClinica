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
        self.__controlador_relatorio = ControladorRelatorio(self.__controlador_clinica,self.__controlador_consulta,self.__controlador_pagamento)
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
            pass #menu relatorio
        else:
            print("\n[Erro] Opção inválida!")

    #Pontes para o Controlador Consulta
    def buscar_clinica(self, nome):
        return self.__controlador_clinica.buscar_clinica_nome(nome)

    def buscar_paciente_cpf(self, cpf):
        return self.__controlador_pessoa.buscar_paciente_cpf(cpf)

    def buscar_profissional_registro(self, registro):
        return self.__controlador_pessoa.buscar_profissional_registro(registro)