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
        self.__tela_sistema = TelaSistema(self)

    def iniciar(self):
        self.__tela_sistema.iniciar()

    @property
    def controlador_clinica(self):
        return self.__controlador_clinica

    @property
    def controlador_consulta(self):
        return self.__controlador_consulta

    @property 
    def controlador_pagamento(self):
        return self.__controlador_pagamento

    @property
    def controlador_relatorio(self):
        return self.__controlador_relatorio

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    def agendar_consulta(self, cpf_paciente, registro_profissional,nome_clinica,tipo,valor,data,horario):
        clinica_encontrada = self.controlador_clinica.buscar_clinica_por_nome(nome_clinica)
        if not clinica_encontrada:
            raise ValueError(f"Clínica '{nome_clinica}' não cadastrada no sistema.")

        paciente_encontrado = self.controlador_pessoa.buscar_paciente_por_cpf(cpf_paciente)
        if not paciente_encontrado:
            raise ValueError(f"Paciente com CPF '{cpf_paciente}' não encontrado.")

        profissional_encontrado = self.controlador_pessoa.buscar_profissional_por_registro(registro_profissional)
        if not profissional_encontrado:
            raise ValueError(f"Profissional com registro '{registro_profissional}' não encontrado.")

        self.controlador_consulta.agendar_consulta(
            clinica_encontrada, 
            paciente_encontrado, 
            profissional_encontrado, 
            tipo, 
            valor, 
            data, 
            horario
        )

    def excluir_consulta(self, cpf_paciente, data_str, horario_str):
        return self.controlador_consulta.excluir_consulta(cpf_paciente, data_str, horario_str)

def alterar_consulta(self, cpf_paciente, data_atual, horario_atual, nova_data, novo_horario):
        return self.controlador_consulta.alterar_dados_consulta(
            cpf_paciente, data_atual, horario_atual, nova_data, novo_horario
        )