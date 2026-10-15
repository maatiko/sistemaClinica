from model.paciente import Paciente
from model.profissional import Profissional
from view.tela_pessoa import TelaPessoa

class ControladorPessoa:
    def __init__(self):
        self.__pacientes = []
        self.__profissionais = []
        self.__tela_pessoa = TelaPessoa(self)

    def abrir_tela(self):
        self.__tela_pessoa.menu_principal_pessoa()

    def adicionar_paciente(self, nome, cpf, telefone, data_nascimento):
        if any(p.cpf == cpf for p in self.__pacientes + self.__profissionais):
            raise ValueError("Já existe uma pessoa com esse CPF.")

        paciente = Paciente(nome, cpf, telefone, data_nascimento)
        self.__pacientes.append(paciente)

        return True

    def remover_paciente(self, cpf):
        if cpf is None :
            raise ValueError("Paciente não informado.")

        paciente = next(
            (p for p in self.__pacientes if p.cpf == cpf),
            None
        )

        if paciente is None:
            raise ValueError("Paciente não encontrado.")

        self.__pacientes.remove(paciente)

        return True

    def adicionar_profissional(self, nome, cpf, telefone, especialidade, registro):
        if any(p.cpf == cpf for p in self.__pacientes + self.__profissionais):
            raise ValueError("Já existe uma pessoa com esse CPF.")

        profissional = Profissional(
            nome, cpf, telefone, especialidade, registro
        )
        self.__profissionais.append(profissional)

        return True

    def remover_profissional(self, cpf):
        if cpf is None:
            raise ValueError("Profissional não informado.")

        profissional = next(
            (p for p in self.__profissionais if p.cpf == cpf),
            None
        )

        if profissional is None:
            raise ValueError("Profissional não encontrado.")

        self.__profissionais.remove(profissional)

        return True

    def mostrar_pacientes(self):
        return self.__pacientes

    def mostrar_profissionais(self):
        return self.__profissionais

    
    def alterar_dados_pessoa(
        self, cpf_atual, novo_nome, novo_cpf, novo_telefone,
        nova_data_nascimento=None, nova_especialidade=None,
        novo_registro=None
    ):
        if cpf_atual is None:
            raise ValueError("Pessoa não informada.")

        pessoa = next(
            (
                p for p in self.__pacientes + self.__profissionais
                if p.cpf == cpf_atual
            ),
            None
        )

        if pessoa is None:
            raise ValueError("Pessoa não encontrada.")

        if novo_cpf != cpf_atual and any(
            p.cpf == novo_cpf
            for p in self.__pacientes + self.__profissionais
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

    def verificar_existencia_paciente(self,cpf_paciente):
        if cpf_paciente is None or cpf_paciente.strip() == "":
            raise ValueError("Paciente não informada.")
        
        existe = any(c.cpf == cpf_paciente for c in self.__pacientes)
        
        if not existe:
            raise ValueError("Paciente não encontrado.")
        return True

    def verificar_existencia_profissional(self,cpf_profissional):
        if cpf_profissional is None or cpf_profissional.strip() == "":
            raise ValueError("Profissional não informado.")
        
        existe = any(c.registro == cpf_profissional for c in self.__profissionais)
        
        if not existe:
            raise ValueError("Profissional não encontrado.")
        return True

    def buscar_paciente_cpf(self,cpf):
        if not cpf:
            return None

        for paciente in self.__pacientes:
            if paciente.cpf == cpf:
                return paciente

    def buscar_profissional_registro(self,registro):
            if not registro:
                return None
    
            for profissional in self.__profissionais:
                if profissional.registro == registro:
                    return profissional