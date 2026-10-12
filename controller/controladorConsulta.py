from datetime import date, datetime

class ControladorConsulta:
    def __init__(self):
        self.consultas = []

    def agendar_consulta(self, consulta):
        self.validar_consulta(consulta)

        if consulta is None:
            raise ValueError("Consulta não informada.")

        if consulta in self.consultas:
            raise ValueError("Consulta já agendada.")

        self.consultas.append(consulta)

    def excluir_consulta(self, consulta):
        if consulta is None:
            raise ValueError("Consulta não informada.")

        if consulta not in self.consultas:
            raise ValueError("Consulta não encontrada.")

        self.consultas.remove(consulta)

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
        if not self.consultas:
            print("Nenhuma consulta agendada.")
        else:
            return list(self.consultas)