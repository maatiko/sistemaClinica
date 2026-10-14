from controller.controladorClinica import ControladorClinica
from controller.controladorConsulta import ControladorConsulta
from controller.controladorPagamento import ControladorPagamento
from controller.controladorRelatorio import ControladorRelatorio
from controller.controladorPessoa import ControladorPessoa
from view.telaSistema import TelaSistema


class ControladorSistema():
    def __init__(self):
        self.__controlador_clinica = ControladorClinica()
        self.__controlador_consulta = ControladorConsulta()
        self.__controlador_pagamento = ControladorPagamento()
        self.__controlador_relatorio = ControladorRelatorio(self.__controlador_clinica,self.__controlador_consulta,self.__controlador_pagamento)
        self.__controlador_pessoa = ControladorPessoa()
        self.__tela_sistema = TelaSistema()

    def iniciar(self):
        self.__tela_sistema.iniciar(self)