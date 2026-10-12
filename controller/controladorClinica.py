class ControladorClinica:
    def __init__(self):
        self.clinicas = []

    def adicionar_clinica(self, clinica):
        if clinica is None:
            raise ValueError("Clínica não informada.")

        if any(c.nome == clinica.nome for c in self.clinicas):
            raise ValueError("Já existe uma clínica com esse nome.")

        self.clinicas.append(clinica)

    def excluir_clinica(self, clinica):
        if clinica is None:
            raise ValueError("Clínica não informada.")

        if clinica not in self.clinicas:
            raise ValueError("Clínica não encontrada.")

        self.clinicas.remove(clinica)

    def listar_clinicas(self):
        if not self.clinicas:
            print("Nenhuma clínica cadastrada.")
        else:
            return list(self.clinicas)