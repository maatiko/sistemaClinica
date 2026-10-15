from datetime import date, datetime
from model.consulta import Consulta
from model.procedimento import Procedimento
from view.tela_consulta import TelaConsulta

class ControladorConsulta:
    def __init__(self,controlador_sistema):
        self.__consultas = []
        self.__tela_consulta= TelaConsulta(self)
        self.__sistema = controlador_sistema

    def abrir_tela(self):
        self.__tela_consulta.menu_consulta()

    def agendar_consulta(self, nome_clinica, cpf_paciente, registro_profissional,tipo, valor, data_str, horario_str):
        clinica = self.__sistema.buscar_clinica(nome_clinica)
        if not clinica:
            raise ValueError(f"Clínica '{nome_clinica}' não cadastrada.")

        paciente = self.__sistema.buscar_paciente_cpf(cpf_paciente)
        if not paciente:
            raise ValueError(f"Paciente com CPF '{cpf_paciente}' não encontrado.")

        profissional = self.__sistema.buscar_profissional_registro(registro_profissional)
        if not profissional:
            raise ValueError(f"Profissional (Registro: '{registro_profissional}') não encontrado.")

        data_conv = self.__converter_data(data_str)
        horario_conv = self.__converter_horario(horario_str)
        
        self.__verificar_expediente(clinica, horario_conv)

        nova_consulta = Consulta(clinica, paciente, profissional,tipo, data_conv, horario_conv, valor )
        self.__verificar_colisao(nova_consulta)

        self.__consultas.append(nova_consulta)
        return True
    
    
    def adicionar_procedimento_na_consulta(self, cpf, data_str, horario_str, desc, custo, registro_prof):
        prof = self.__sistema.buscar_profissional_por_registro(registro_prof)
        if not prof:
            raise ValueError("Profissional do procedimento não encontrado.")
            
        data_conv = self.__converter_data(data_str)
        hor_conv = self.__converter_horario(horario_str)
        
        consulta = self.__encontrar_consulta(cpf, data_conv, hor_conv)
        if not consulta:
            raise ValueError("Consulta não encontrada.")
            
        proc = Procedimento(desc, custo, prof)
        consulta.adicionar_procedimento(proc)
        return True
    
    def excluir_procedimento_da_consulta(self, cpf_paciente, data_str, horario_str, descricao_procedimento):
        data_conv = self.__converter_data(data_str)
        hor_conv = self.__converter_horario(horario_str)
        
        consulta = self.__encontrar_consulta(cpf_paciente, data_conv, hor_conv)
        if not consulta:
            raise ValueError("Consulta não encontrada.")

        procedimento_alvo = None
        for procedimento in consulta.procedimentos:
            if procedimento.descricao.strip().lower() == descricao_procedimento.strip().lower():
                procedimento_alvo = procedimento
                break
                
        if not procedimento_alvo:
            raise ValueError(f"Procedimento '{descricao_procedimento}' não encontrado nesta consulta.")

        consulta.remover_procedimento(procedimento_alvo)
        return True

    def alterar_procedimento_da_consulta(self, cpf, data_str, hor_str, desc_atual, nova_desc, novo_custo, novo_registro_prof):
        data_conv = self.__converter_data(data_str)
        hor_conv = self.__converter_horario(hor_str)
        consulta = self.__encontrar_consulta(cpf, data_conv, hor_conv)
        if not consulta:
            raise ValueError("Consulta não encontrada.")

        procedimento_alvo = None
        for procedimento in consulta.procedimentos:
            if procedimento.descricao.strip().lower() == desc_atual.strip().lower():
                procedimento_alvo = procedimento
                break
                
        if not procedimento_alvo:
            raise ValueError(f"Procedimento '{desc_atual}' não encontrado nesta consulta.")

        if novo_registro_prof != procedimento_alvo.profissional.registro:
            novo_profissional = self.__sistema.buscar_profissional_por_registro(novo_registro_prof)
            if not novo_profissional:
                raise ValueError("Novo profissional informado não encontrado no sistema.")
            procedimento_alvo.profissional = novo_profissional

        procedimento_alvo.descricao = nova_desc
        procedimento_alvo.custo = novo_custo
        return True

    def listar_procedimentos_da_consulta(self, cpf, data_str, horario_str):
        data_conv = self.__converter_data(data_str)
        hor_conv = self.__converter_horario(horario_str)
        
        consulta = self.__encontrar_consulta(cpf, data_conv, hor_conv)
        if not consulta:
            raise ValueError("Consulta não encontrada.")
            
        return consulta.procedimentos
    
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


    def __encontrar_consulta(self, cpf_paciente, data_convertida, horario_convertido):
        if not cpf_paciente or not data_convertida or not horario_convertido:
            return None

        for consulta in self.__consultas:
            if (consulta.paciente.cpf == cpf_paciente and 
                consulta.data == data_convertida and 
                consulta.horario == horario_convertido):
                return consulta
                
        return None
    
    def __converter_data(self, data_consulta):
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

    def __converter_horario(self, horario_str):
        if not horario_str:
            raise ValueError("Horário não informado.")
        
        try:
            return datetime.strptime(horario_str, "%H:%M").time()
        except ValueError:
            raise ValueError("Formato de horário inválido. Use HH:MM (ex: 14:30).")


    def listar_consultas(self):
            return list(self.consultas)

    def __verificar_expediente(self, clinica, horario_consulta):
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
    