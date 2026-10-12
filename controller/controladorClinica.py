from model import Clinica
class ControladorClinica:
    def __init__(self):
        self.__clinicas = []

    def adicionar_clinica(self,nome,localizacao,descricao,horario_abertura,horario_fechamento):
        clinica_adicionada = Clinica(nome,localizacao,descricao,horario_abertura,horario_fechamento)
        if clinica_adicionada is None:
            raise ValueError("Clínica não informada.")
        elif any(c.nome == clinica_adicionada.nome for c in self.__clinicas):
            raise ValueError("Já existe uma clínica com esse nome.")
        else:
            self.__clinicas.append(clinica_adicionada)
            return True

    def excluir_clinica(self, nome_clinica):
        if nome_clinica is None:
            raise ValueError("Clínica não informada.")

        if nome_clinica not in self.__clinicas:
            raise ValueError("Clínica não encontrada.")

        self.__clinicas.remove(nome_clinica)

    def listar_clinicas(self):
        if not self.__clinicas:
            print("Nenhuma clínica cadastrada.")
        else:
            return list(self.__clinicas)