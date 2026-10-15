from datetime import date, datetime, time

from model.consulta import Consulta
from model.procedimento import Procedimento


class ControladorConsulta:

    def __init__(self, sistema):
        self.__sistema = sistema
        self.__consultas = []

    def agendar_consulta(
        self,
        nome_clinica,
        cpf_paciente,
        registro_profissional,
        tipo,
        valor,
        data_str,
        horario_str,
    ):
        if not all([
            nome_clinica,
            cpf_paciente,
            registro_profissional,
            tipo,
            valor,
            data_str,
            horario_str,
        ]):
            raise ValueError("Todos os campos da consulta são obrigatórios.")

        clinica = self.__sistema.buscar_clinica(nome_clinica)
        paciente = self.__sistema.buscar_paciente_cpf(cpf_paciente)
        profissional = self.__sistema.buscar_profissional_registro(
            registro_profissional
        )

        if clinica is None:
            raise ValueError("Clínica não encontrada.")
        if paciente is None:
            raise ValueError("Paciente não encontrado.")
        if profissional is None:
            raise ValueError("Profissional não encontrado.")

        data_consulta = self.__converter_data(data_str)
        horario_consulta = self.__converter_horario(horario_str)

        self.__verificar_expediente(clinica, horario_consulta)

        nova_consulta = Consulta(
            clinica,
            paciente,
            profissional,
            tipo,
            data_consulta,
            horario_consulta,
            valor,
        )

        if self.verificar_colisao(nova_consulta):
            raise ValueError(
                "Já existe uma consulta nesse horário para o paciente "
                "ou profissional."
            )

        self.__consultas.append(nova_consulta)
        return nova_consulta

    def excluir_consulta(self, cpf_paciente, data_str, horario_str):
        consulta = self.buscar_consulta(
            cpf_paciente, data_str, horario_str
        )

        if consulta is None:
            raise ValueError("Consulta não encontrada.")

        self.__consultas.remove(consulta)
        return consulta

    def listar_consultas(self):
        return self.__consultas.copy()

    def verificar_existencia_consulta(
        self, cpf_paciente, data_str, horario_str
    ):
        return self.buscar_consulta(
            cpf_paciente, data_str, horario_str
        ) is not None

    def buscar_consulta(self, cpf_paciente, data_str, horario_str):
        data_consulta = self.__converter_data(data_str)
        horario_consulta = self.__converter_horario(horario_str)

        for consulta in self.__consultas:
            if (
                consulta.paciente.cpf == cpf_paciente
                and consulta.data == data_consulta
                and consulta.horario == horario_consulta
            ):
                return consulta

        return None

    def verificar_colisao(self, nova_consulta, consulta_ignorada=None):
        for consulta in self.__consultas:
            if consulta is consulta_ignorada:
                continue

            mesmo_horario = (
                consulta.data == nova_consulta.data
                and consulta.horario == nova_consulta.horario
            )

            if not mesmo_horario:
                continue

            mesmo_profissional = (
                consulta.profissional.registro
                == nova_consulta.profissional.registro
            )

            mesmo_paciente = (
                consulta.paciente.cpf == nova_consulta.paciente.cpf
            )

            if mesmo_profissional or mesmo_paciente:
                return True

        return False

    def alterar_dados_consulta(
        self,
        cpf_paciente,
        data_atual,
        horario_atual,
        nome_clinica,
        registro_profissional,
        novo_tipo,
        novo_valor,
        nova_data,
        novo_horario,
    ):
        consulta = self.buscar_consulta(
            cpf_paciente, data_atual, horario_atual
        )

        if consulta is None:
            raise ValueError("Consulta não encontrada.")

        clinica = self.__sistema.buscar_clinica(nome_clinica)
        profissional = self.__sistema.buscar_profissional_registro(
            registro_profissional
        )

        if clinica is None:
            raise ValueError("Clínica não encontrada.")
        if profissional is None:
            raise ValueError("Profissional não encontrado.")

        data_convertida = self.__converter_data(nova_data)
        horario_convertido = self.__converter_horario(novo_horario)

        self.__verificar_expediente(clinica, horario_convertido)

        consulta_temporaria = Consulta(
            clinica,
            consulta.paciente,
            profissional,
            novo_tipo,
            data_convertida,
            horario_convertido,
            novo_valor,
        )

        if self.verificar_colisao(
            consulta_temporaria, consulta_ignorada=consulta
        ):
            raise ValueError(
                "Já existe uma consulta nesse horário para o paciente "
                "ou profissional."
            )

        consulta.clinica = clinica
        consulta.profissional = profissional
        consulta.tipo = novo_tipo
        consulta.data = data_convertida
        consulta.horario = horario_convertido
        consulta.valor_base = novo_valor

        return consulta

    def adicionar_procedimento_na_consulta(
        self,
        cpf_paciente,
        data_str,
        horario_str,
        descricao,
        custo,
        registro_prof,
    ):
        consulta = self.buscar_consulta(
            cpf_paciente, data_str, horario_str
        )

        if consulta is None:
            raise ValueError("Consulta não encontrada.")

        profissional = self.__sistema.buscar_profissional_registro(
            registro_prof
        )

        if profissional is None:
            raise ValueError("Profissional não encontrado.")

        procedimento = Procedimento(
            descricao, custo, profissional
        )

        consulta.adicionar_procedimento(procedimento)
        return procedimento

    def excluir_procedimento_da_consulta(
        self, cpf_paciente, data_str, horario_str, descricao
    ):
        consulta = self.buscar_consulta(
            cpf_paciente, data_str, horario_str
        )

        if consulta is None:
            raise ValueError("Consulta não encontrada.")

        for procedimento in consulta.procedimentos:
            if procedimento.descricao == descricao:
                consulta.remover_procedimento(procedimento)
                return procedimento

        raise ValueError("Procedimento não encontrado nessa consulta.")

    def alterar_procedimento_da_consulta(
        self,
        cpf_paciente,
        data_str,
        horario_str,
        descricao_atual,
        nova_descricao,
        novo_custo,
        novo_registro_prof,
    ):
        consulta = self.buscar_consulta(
            cpf_paciente, data_str, horario_str
        )

        if consulta is None:
            raise ValueError("Consulta não encontrada.")

        procedimento_alvo = None

        for procedimento in consulta.procedimentos:
            if procedimento.descricao == descricao_atual:
                procedimento_alvo = procedimento
                break

        if procedimento_alvo is None:
            raise ValueError("Procedimento não encontrado nessa consulta.")

        novo_profissional = self.__sistema.buscar_profissional_registro(
            novo_registro_prof
        )

        if novo_profissional is None:
            raise ValueError("Profissional não encontrado.")

        procedimento_alvo.descricao = nova_descricao
        procedimento_alvo.custo = novo_custo
        procedimento_alvo.profissional = novo_profissional

        return procedimento_alvo

    def listar_procedimentos_da_consulta(
        self, cpf_paciente, data_str, horario_str
    ):
        consulta = self.buscar_consulta(
            cpf_paciente, data_str, horario_str
        )

        if consulta is None:
            raise ValueError("Consulta não encontrada.")

        return consulta.procedimentos.copy()

    def __converter_data(self, data_informada):
        if isinstance(data_informada, datetime):
            data_informada = data_informada.date()

        if isinstance(data_informada, date):
            data_convertida = data_informada
        elif isinstance(data_informada, str):
            try:
                data_convertida = datetime.strptime(
                    data_informada.strip(), "%d/%m/%Y"
                ).date()
            except ValueError:
                raise ValueError(
                    "Data inválida. Informe a data no formato DD/MM/AAAA."
                )
        else:
            raise ValueError("A data informada é inválida.")

        if data_convertida < date.today():
            raise ValueError("Não é possível agendar uma consulta no passado.")

        return data_convertida

    def __converter_horario(self, horario_informado):
        if isinstance(horario_informado, datetime):
            horario_informado = horario_informado.time()

        if isinstance(horario_informado, time):
            return horario_informado

        if isinstance(horario_informado, str):
            try:
                return datetime.strptime(
                    horario_informado.strip(), "%H:%M"
                ).time()
            except ValueError:
                raise ValueError(
                    "Horário inválido. Informe o horário no formato HH:MM."
                )

        raise ValueError("O horário informado é inválido.")

    def __verificar_expediente(self, clinica, horario_consulta):
        try:
            abertura = datetime.strptime(
                clinica.horario_abertura, "%H:%M"
            ).time()
            fechamento = datetime.strptime(
                clinica.horario_fechamento, "%H:%M"
            ).time()
        except (TypeError, ValueError):
            raise ValueError(
                "Os horários de funcionamento da clínica são inválidos."
            )

        if not abertura <= horario_consulta <= fechamento:
            raise ValueError(
                "O horário da consulta está fora do expediente da clínica."
            )