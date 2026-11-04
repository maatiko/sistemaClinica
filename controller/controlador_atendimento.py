from datetime import date, datetime
from model.atendimento import Atendimento
from model.procedimento import Procedimento
from view.tela_atendimento import TelaAtendimento

class ControladorAntedimento:
    def __init__(self,controlador_sistema):
        self.__consultas = []
        self.__proximo_id_atendimento = 1
        self.__tela= TelaAtendimento(self)
        self.__sistema = controlador_sistema

    def abrir_tela(self):
        self.__tela.menu_consulta()

    def agendar_consulta(
        self,
        nome_clinica,
        cpf_paciente,
        registro_profissional,
        tipo,
        data_str,
        horario_inicio_str,
        horario_fim_str,):
        clinica = self.__sistema.buscar_clinica(nome_clinica)
        if (
            not nome_clinica
            or not cpf_paciente
            or not registro_profissional
            or not tipo
            or not data_str
            or not horario_inicio_str
            or not horario_fim_str
        ):
            raise ValueError("Todos os campos do agendamento são obrigatórios.")
        
        if not clinica:
            raise ValueError(f"Clínica '{nome_clinica}' não cadastrada.")

        paciente = self.__sistema.buscar_paciente_cpf(cpf_paciente)
        if not paciente:
            raise ValueError(f"Paciente com CPF '{cpf_paciente}' não encontrado.")

        profissional = self.__sistema.buscar_profissional_registro(registro_profissional)
        if not profissional:
            raise ValueError(f"Profissional (Registro: '{registro_profissional}') não encontrado.")

        tipo_atendimento = self.__sistema.buscar_tipo_atendimento(tipo)
        data_conv = self.__converter_data(data_str)
        horario_inicio = self.__converter_horario(horario_inicio_str)
        horario_fim = self.__converter_horario(horario_fim_str)
        self.__validar_intervalo(horario_inicio, horario_fim)
        
        self.__verificar_expediente(clinica, horario_inicio, horario_fim)

        nova_consulta = Atendimento(
            clinica,
            paciente,
            profissional,
            tipo_atendimento,
            data_conv.strftime("%d/%m/%Y"),
            horario_inicio.strftime("%H:%M"),
            horario_fim.strftime("%H:%M"),
            self.__proximo_id_atendimento,
        )
        self.__verificar_colisao(nova_consulta)

        self.__consultas.append(nova_consulta)
        self.__proximo_id_atendimento += 1
        return nova_consulta.id_atendimento
    
    
    def adicionar_procedimento_na_consulta(self, id_atendimento, desc, custo, registro_prof):
        consulta = self.buscar_consulta_por_id(id_atendimento)
        prof = self.__sistema.buscar_profissional_registro(registro_prof)
        if not prof:
            raise ValueError("Profissional do procedimento não encontrado.")
            
        proc = Procedimento(desc, custo, prof)
        consulta.adicionar_procedimento(proc)
        return True
    
    def excluir_procedimento_da_consulta(self, id_atendimento, descricao_procedimento):
        consulta = self.buscar_consulta_por_id(id_atendimento)

        procedimento_alvo = None
        for procedimento in consulta.procedimentos:
            if procedimento.descricao.strip().lower() == descricao_procedimento.strip().lower():
                procedimento_alvo = procedimento
                break
                
        if not procedimento_alvo:
            raise ValueError(f"Procedimento '{descricao_procedimento}' não encontrado nesta consulta.")

        consulta.remover_procedimento(procedimento_alvo)
        return True

    def alterar_procedimento_da_consulta(
        self,
        id_atendimento,
        desc_atual,
        nova_desc,
        novo_custo,
        novo_registro_prof,
    ):
        consulta = self.buscar_consulta_por_id(id_atendimento)

        procedimento_alvo = None
        for procedimento in consulta.procedimentos:
            if procedimento.descricao.strip().lower() == desc_atual.strip().lower():
                procedimento_alvo = procedimento
                break
                
        if not procedimento_alvo:
            raise ValueError(f"Procedimento '{desc_atual}' não encontrado nesta consulta.")

        if novo_registro_prof != procedimento_alvo.profissional.registro:
            novo_profissional = self.__sistema.buscar_profissional_registro(novo_registro_prof)
            if not novo_profissional:
                raise ValueError("Novo profissional informado não encontrado no sistema.")
            procedimento_alvo.profissional = novo_profissional

        procedimento_alvo.descricao = nova_desc
        procedimento_alvo.custo = novo_custo
        return True

    def listar_procedimentos_da_consulta(self, id_atendimento):
        consulta = self.buscar_consulta_por_id(id_atendimento)
        return consulta.procedimentos
    
    def __verificar_colisao(self, nova_consulta, consulta_ignorada=None):
        for consulta in self.__consultas:
            if consulta is consulta_ignorada or consulta.data != nova_consulta.data:
                continue

            inicio_existente = self.__converter_horario(consulta.horario)
            fim_existente = self.__converter_horario(consulta.horario_fim)
            inicio_novo = self.__converter_horario(nova_consulta.horario)
            fim_novo = self.__converter_horario(nova_consulta.horario_fim)
            ha_sobreposicao = inicio_novo < fim_existente and fim_novo > inicio_existente

            if not ha_sobreposicao:
                continue
            if consulta.paciente == nova_consulta.paciente:
                raise ValueError("O paciente já possui um atendimento neste intervalo.")
            if consulta.profissional == nova_consulta.profissional:
                raise ValueError("O profissional já possui um atendimento neste intervalo.")
    
    def excluir_consulta(self, id_atendimento):
        consulta = self.buscar_consulta_por_id(id_atendimento)
        self.__consultas.remove(consulta)
        return True



    def listar_consultas(self):
            return list(self.__consultas)

   
    def alterar_dados_consulta(self,id_atendimento,nova_data,novo_horario_inicio,novo_horario_fim,):
        consulta = self.buscar_consulta_por_id(id_atendimento)
        nova_data_conv = self.__converter_data(nova_data)
        novo_hor_inicio = self.__converter_horario(novo_horario_inicio)
        novo_hor_fim = self.__converter_horario(novo_horario_fim)
        self.__validar_intervalo(novo_hor_inicio, novo_hor_fim)

        nova_consulta = Atendimento(
            consulta.clinica,
            consulta.paciente,
            consulta.profissional,
            consulta.tipo,
            nova_data_conv.strftime("%d/%m/%Y"),
            novo_hor_inicio.strftime("%H:%M"),
            novo_hor_fim.strftime("%H:%M"),
            consulta.id_atendimento,
        )
        self.__verificar_expediente(consulta.clinica, novo_hor_inicio, novo_hor_fim)
        self.__verificar_colisao(nova_consulta, consulta)
        consulta.data = nova_data_conv.strftime("%d/%m/%Y")
        consulta.horario = novo_hor_inicio.strftime("%H:%M")
        consulta.horario_fim = novo_hor_fim.strftime("%H:%M")
        return True

    def verificar_existencia_consulta(self, id_atendimento):
        self.buscar_consulta_por_id(id_atendimento)
        return True

    def buscar_consulta(self, id_atendimento):
        return self.buscar_consulta_por_id(id_atendimento)

    def buscar_consulta_por_id(self, id_atendimento):
        try:
            id_validado = int(id_atendimento)
        except (TypeError, ValueError):
            raise ValueError("O ID do atendimento deve ser um número inteiro.")

        if id_validado <= 0 or str(id_atendimento).strip() != str(id_validado):
            raise ValueError("O ID do atendimento deve ser um número inteiro positivo.")

        for consulta in self.__consultas:
            if consulta.id_atendimento == id_validado:
                return consulta
                
        raise ValueError(f"Atendimento com ID {id_validado} não encontrado.")
    
    def __converter_data(self, data_consulta):
        if isinstance(data_consulta, str):
            try:
                data_consulta = datetime.strptime(data_consulta, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("Data inválida. Use o formato DD/MM/AAAA.")
        elif isinstance(data_consulta, datetime):
            data_consulta = data_consulta.date()

        return data_consulta

    def __converter_horario(self, horario_str):
        if not horario_str:
            raise ValueError("Horário não informado.")
        
        try:
            return datetime.strptime(horario_str, "%H:%M").time()
        except ValueError:
            raise ValueError("Formato de horário inválido. Use HH:MM (ex: 14:30).")

    def __validar_intervalo(self, horario_inicio, horario_fim):
        if horario_fim <= horario_inicio:
            raise ValueError("O horário de fim deve ser posterior ao horário de início.")

    def __verificar_expediente(self, clinica, horario_inicio, horario_fim):
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

        if abertura >= fechamento:
            raise ValueError("O horário de funcionamento da clínica está configurado incorretamente.")

        if horario_inicio < abertura or horario_fim > fechamento:
            raise ValueError(
                f"Horário fora do expediente! A {clinica.nome} funciona de "
                f"{abertura.strftime('%H:%M')} às {fechamento.strftime('%H:%M')}."
            )