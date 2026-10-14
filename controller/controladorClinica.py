from model.clinica import Clinica
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
        if nome_clinica is None or nome_clinica.strip() == "":
            raise ValueError("Clínica não informada.")
        
        clinica_encontrada = None
        for clinica in self.__clinicas:
            if clinica.nome == nome_clinica:
                clinica_encontrada = clinica
        if clinica_encontrada is None:
            raise ValueError("Clínica não encontrada.")
            
        self.__clinicas.remove(clinica_encontrada)
        return True

    def listar_clinicas(self):
        return self.__clinicas

    def alterar_dados_clinica(self, nome_atual, novo_nome, nova_localizacao,
                              nova_descricao, novo_horario_abertura,
                              novo_horario_fechamento):
        if nome_atual is None:
            raise ValueError("Clínica não informada.")

        clinica = next(
            (c for c in self.__clinicas if c.nome == nome_atual),
            None
        )

        if clinica is None:
            raise ValueError("Clínica não encontrada.")

        if novo_nome != nome_atual and any(
            c.nome == novo_nome for c in self.__clinicas
        ):
            raise ValueError("Já existe uma clínica com esse nome.")

        clinica.nome = novo_nome
        clinica.localizacao = nova_localizacao
        clinica.descricao = nova_descricao
        clinica.horario_abertura = novo_horario_abertura
        clinica.horario_fechamento = novo_horario_fechamento

        return True

    def verificar_existencia(self, nome_clinica):
        if nome_clinica is None or nome_clinica.strip() == "":
            raise ValueError("Clínica não informada.")
        
        existe = any(c.nome == nome_clinica for c in self.__clinicas)
        
        if not existe:
            raise ValueError("Clínica não encontrada.")
        return True