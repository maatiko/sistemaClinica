from datetime import date, datetime
from model.consulta import Consulta

class ControladorConsulta:
    def __init__(self):
        self.__consultas = []

    def agendar_consulta(self, clinica,paciente,profissional,tipo,valor,data,horario):
        
        self.validar_dados_consulta(clinica,paciente,profissional,tipo,valor,data,horario)
        data_convertida = self.__converter_data(data)
        nova_consulta = Consulta(clinica,paciente,profissional,tipo,valor,data,horario)
        self.__verificar_colisao(nova_consulta)
        
        self.__consultas.append(nova_consulta)

    def verificar_colisao(self,nova_consulta):
        for consulta in self.__consultas:
            if (consulta.profissional == nova_consulta.profissional and 
                consulta.data == nova_consulta.data and 
                consulta.horario == nova_consulta.horario):
                raise ValueError("Confluto de Horário")

    def excluir_consulta(self, cpf_paciente, data_str, horario_str):
        data_conv = self.__converter_data(data_str)
        horario_conv = self.__converter_horario(horario_str)

        consulta_encontrada = None
        for consulta in self.__consultas:
            if consulta.paciente.cpf == cpf_paciente and consulta.data == data_conv and consulta.horario == horario_conv:
                consulta_encontrada = consulta
                break

        if not consulta_encontrada:
            raise ValueError("Nenhuma consulta encontrada com esses dados.")

        self.__consultas.remove(consulta_encontrada)
        return True


    def converter_data(self, data_consulta):
        if isinstance(data_consulta, str):
            try:
                data_consulta = datetime.strptime(data_consulta, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("Data inválida. Use o formato DD/MM/AAAA.")
        elif isinstance(data_consulta, datetime):
            data_consulta = data_consulta.date()

        if data_consulta < date.today():
            raise ValueError("A data da consulta não pode estar no passado.")
        
        return data_consulta

    def converter_horario(self, horario_str):
        if not horario_str:
            raise ValueError("Horário não informado.")
        
        try:
            return datetime.strptime(horario_str, "%H:%M").time()
        except ValueError:
            raise ValueError("Formato de horário inválido. Use HH:MM (ex: 14:30).")
        
    def validar_consulta(self, consulta):
        if consulta is None:
            raise ValueError("Consulta não informada.")

        if consulta.clinica is None:
            raise ValueError("A consulta precisa de uma clínica.")

        if consulta.paciente is None:
            raise ValueError("A consulta precisa de um paciente.")

        if consulta.profissional is None:
            raise ValueError("A consulta precisa de um profissional.")

        if not consulta.tipo:
            raise ValueError("Informe o tipo de atendimento.")

        if consulta.valor < 0:
            raise ValueError("O valor não pode ser negativo.")

        data_consulta = consulta.data 

        if isinstance(data_consulta, str):
            try:
                data_consulta = datetime.strptime(data_consulta, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("data inválida. Use DD/MM/AAAA.")

        if isinstance(data_consulta, datetime):
            data_consulta = data_consulta.date()

        if data_consulta < date.today():
            raise ValueError("A data da consulta não pode estar no passado.")

        if not consulta.paciente.verificar_idade(consulta.paciente.idade):
            raise ValueError("O paciente precisa ter mais de 18 anos.")

        return True

    def listar_consultas(self):
            return list(self.consultas)

    def verificar_expediente(self, clinica, horario_consulta):
        try:
            if isinstance(clinica.horario_abertura, str):
                abertura = datetime.strptime(clinica.horario_abertura, "%H:%M").time()
            else:
                abertura = clinica.horario_abertura
                
            if isinstance(clinica.horario_fechamento, str):
                fechamento = datetime.strptime(clinica.horario_fechamento, "%H:%M").time()
            else:
                fechamento = clinica.horario_fechamento
        except ValueError:
            raise ValueError("O horário de funcionamento da clínica está em um formato inválido no sistema.")

        if horario_consulta < abertura or horario_consulta > fechamento:
            raise ValueError(
                f"Horário fora do expediente! A {clinica.nome} funciona de "
                f"{abertura.strftime('%H:%M')} às {fechamento.strftime('%H:%M')}."
            )
    def alterar_dados_consulta(self, cpf, data_atual, hor_atual, nova_data, novo_horario):
        data_conv_atual = self.__converter_data(data_atual)
        hor_conv_atual = self.__converter_horario(hor_atual)
        nova_data_conv = self.__converter_data(nova_data)
        novo_hor_conv = self.__converter_horario(novo_horario)

        consulta = None
        for c in self.__consultas:
            if c.paciente.cpf == cpf and c.data == data_conv_atual and c.horario == hor_conv_atual:
                consulta = c
                break
                
        if not consulta:
            raise ValueError("Consulta não encontrada para alteração.")

        self.__verificar_expediente(consulta.clinica, novo_hor_conv)

        for c in self.__consultas:
            if c != consulta: 
                if (c.profissional == consulta.profissional and 
                    c.data == nova_data_conv and 
                    c.horario == novo_hor_conv):
                    raise ValueError("O profissional já possui outra consulta neste novo horário.")

        consulta.data = nova_data_conv
        consulta.horario = novo_hor_conv
        return True

    def verificar_existencia_consulta(self, cpf, data_str, horario_str):
        data_conv = self.__converter_data(data_str)
        horario_conv = self.__converter_horario(horario_str)

        for consulta in self.__consultas:
            if consulta.paciente.cpf == cpf and consulta.data == data_conv and consulta.horario == horario_conv:
                return True 
                
        raise ValueError("Consulta não encontrada com esses dados.")