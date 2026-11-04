from view.tela_tipo_atendimento import TelaTipoAtendimento
from model.tipo_atendimento import TipoAtendimento

class ControladorTipoAtendimento:
    def __init__(self):
        self.__tipos_atendimentos = []
        self.__tela = TelaTipoAtendimento(self)
    
    def abrir_tela(self):
        self.__tela.menu_tipo_atendimento()

    def adicionar_tipo_atendimento(self, nome, descricao, valor):
        if any(tipo.nome.casefold() == nome.strip().casefold() for tipo in self.__tipos_atendimentos):
            raise ValueError(f"O Tipo de Atendimento '{nome}' já está cadastrado.")

        novo_tipo = TipoAtendimento(nome, descricao, valor)
        self.__tipos_atendimentos.append(novo_tipo)
        return novo_tipo

    def buscar_tipo_atendimento(self, nome):
        if isinstance(nome, str):
            for tipo in self.__tipos_atendimentos:
                if tipo.nome.casefold() == nome.strip().casefold():
                    return tipo
        raise ValueError(f"Tipo de Atendimento '{nome}' não encontrado.")

    def remover_tipo_atendimento(self, nome_remover):
        tipo = self.buscar_tipo_atendimento(nome_remover)
        self.__tipos_atendimentos.remove(tipo)
        return True

    def alterar_tipo_atendimento(self, nome_atual, novo_nome, nova_descricao, novo_valor):
        tipo = self.buscar_tipo_atendimento(nome_atual)
        if novo_nome.strip().casefold() != tipo.nome.casefold() and any(
            outro.nome.casefold() == novo_nome.strip().casefold()
            for outro in self.__tipos_atendimentos
        ):
            raise ValueError(f"O Tipo de Atendimento '{novo_nome}' já está cadastrado.")

        tipo.nome = novo_nome
        tipo.descricao = nova_descricao
        tipo.valor = novo_valor
        return tipo

    def listar_tipo_atendimento(self):
        return list(self.__tipos_atendimentos)