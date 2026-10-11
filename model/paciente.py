from abstractPessoa import Pessoa

class Paciente(Pessoa):

    def __init__(self, nome, cpf, telefone):
        super().__init__(nome, cpf, telefone)