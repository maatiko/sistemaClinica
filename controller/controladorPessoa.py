class ControladorPessoa:
    def __init__(self):
        self.pacientes = []
        self.profissionais = []  

    def adicionar_paciente(self, paciente):
        if paciente is None:
            raise ValueError("Paciente não Informado.")

        if any(p.cpf == paciente.cpf for p in self.pacientes + self.profissionais):
            raise ValueError("Já existe uma pessoa com esse CPF.")

        self.pacientes.append(paciente)

    def remover_paciente(self, paciente):
        if paciente is None:
            raise ValueError("Paciente não Informado.")

        if paciente not in self.pacientes:
            raise ValueError("Paciente não encontrado.")

        self.pacientes.remove(paciente)

    def adicionar_profissional(self, profissional):
        if profissional is None:
            raise ValueError("Profissional não Informado.")

        if any(p.cpf == profissional.cpf for p in self.pacientes + self.profissionais):
            raise ValueError("Já existe uma pessoa com esse CPF.")

        self.profissionais.append(profissional)

    def remover_profissional(self, profissional):
        if profissional is None:
            raise ValueError("Profissional não Informado.")

        if profissional not in self.profissionais:
            raise ValueError("Profissional não encontrado.")

        self.profissionais.remove(profissional)

    def mostrar_pacientes(self):
        if not self.pacientes:
            print("Nenhum paciente cadastrado.")
        else:
            return list(self.pacientes)

    def mostrar_profissionais(self):
        if not self.profissionais:
            print("Nenhum profissional cadastrado.")
        else:
            return list(self.profissionais)

    def alterar_dados_pessoa(self, cpf_atual, novo_nome, novo_cpf,
                             novo_telefone, nova_data_nascimento):
        if cpf_atual is None:
            raise ValueError("Pessoa não informada.")

        pessoa = next(
            (p for p in self.pacientes + self.profissionais
             if p.cpf == cpf_atual),
            None
        )

        if pessoa is None:
            raise ValueError("Pessoa não encontrada.")

        if novo_cpf != cpf_atual and any(
            p.cpf == novo_cpf
            for p in self.pacientes + self.profissionais
        ):
            raise ValueError("Já existe uma pessoa com esse CPF.")

        pessoa.nome = novo_nome
        pessoa.cpf = novo_cpf
        pessoa.telefone = novo_telefone
        pessoa.data_nascimento = nova_data_nascimento

        return True