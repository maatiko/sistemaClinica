
from model.paciente import Paciente
from model.profissional import Profissional


class ControladorPessoa:
    def __init__(self):
        self.pacientes = []
        self.profissionais = []

    def adicionar_paciente(self, nome, cpf, telefone, data_nascimento):
        if any(p.cpf == cpf for p in self.pacientes + self.profissionais):
            raise ValueError("Já existe uma pessoa com esse CPF.")

        paciente = Paciente(nome, cpf, telefone, data_nascimento)
        self.pacientes.append(paciente)

        return True

    def remover_paciente(self, cpf):
        if cpf is None:
            raise ValueError("Paciente não informado.")

        paciente = next(
            (p for p in self.pacientes if p.cpf == cpf),
            None
        )

        if paciente is None:
            raise ValueError("Paciente não encontrado.")

        self.pacientes.remove(paciente)

        return True

    def adicionar_profissional(self, nome, cpf, telefone, especialidade, registro):
        if any(p.cpf == cpf for p in self.pacientes + self.profissionais):
            raise ValueError("Já existe uma pessoa com esse CPF.")

        profissional = Profissional(
            nome, cpf, telefone, especialidade, registro
        )
        self.profissionais.append(profissional)

        return True

    def remover_profissional(self, cpf):
        if cpf is None:
            raise ValueError("Profissional não informado.")

        profissional = next(
            (p for p in self.profissionais if p.cpf == cpf),
            None
        )

        if profissional is None:
            raise ValueError("Profissional não encontrado.")

        self.profissionais.remove(profissional)

        return True

    def mostrar_pacientes(self):
        if not self.pacientes:
            return []

        return list(self.pacientes)

    def mostrar_profissionais(self):
        if not self.profissionais:
            return []

        return list(self.profissionais)

    
    def alterar_dados_pessoa(
        self, cpf_atual, novo_nome, novo_cpf, novo_telefone,
        nova_data_nascimento=None, nova_especialidade=None,
        novo_registro=None
    ):
        if cpf_atual is None:
            raise ValueError("Pessoa não informada.")

        pessoa = next(
            (
                p for p in self.pacientes + self.profissionais
                if p.cpf == cpf_atual
            ),
            None
        )

        if pessoa is None:
            raise ValueError("Pessoa não encontrada.")

        if novo_cpf != cpf_atual and any(
            p.cpf == novo_cpf
            for p in self.pacientes + self.profissionais
        ):
            raise ValueError("Já existe uma pessoa com esse CPF.")

        if isinstance(pessoa, Paciente) and nova_data_nascimento is None:
            raise ValueError("Data de nascimento não informada.")

        if isinstance(pessoa, Profissional) and (
            nova_especialidade is None or novo_registro is None
        ):
            raise ValueError("Especialidade e registro são obrigatórios.")

        pessoa.nome = novo_nome
        pessoa.cpf = novo_cpf
        pessoa.telefone = novo_telefone

        if isinstance(pessoa, Paciente):
            pessoa.data_nascimento = nova_data_nascimento

        elif isinstance(pessoa, Profissional):
            pessoa.especialidade = nova_especialidade
            pessoa.registro = novo_registro

        return True