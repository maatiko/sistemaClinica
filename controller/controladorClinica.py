
from model.clinica import Clinica
from view.tela_clinica import TelaClinica
from exception.excecoes import (
    ClinicaDuplicadaException,
    ClinicaNaoInformadaException,
    ClinicaNaoEncontradaException,
)


class ControladorClinica:
    def __init__(self):
        self.__clinicas = []
        self.__tela_clinica = TelaClinica(self)

    @staticmethod
    def __normalizar_nome(nome):
        if nome is None or not isinstance(nome, str) or not nome.strip():
            raise ClinicaNaoInformadaException(
                "O nome da clínica é obrigatório."
            )
        return nome.strip().casefold()

    def abrir_tela(self):
        self.__tela_clinica.menu_clinica()

    def adicionar_clinica(
        self, nome, localizacao, descricao,
        horario_abertura, horario_fechamento
    ):
        nome_normalizado = self.__normalizar_nome(nome)

        for clinica in self.__clinicas:
            if clinica.nome.strip().casefold() == nome_normalizado:
                raise ClinicaDuplicadaException(
                    f"Já existe uma clínica cadastrada com o nome "
                    f"'{nome.strip()}'. Escolha outro nome."
                )

        if not localizacao or not localizacao.strip():
            raise ClinicaNaoInformadaException(
                "A localização da clínica é obrigatória."
            )

        if not descricao or not descricao.strip():
            raise ClinicaNaoInformadaException(
                "A descrição da clínica é obrigatória."
            )

        if not horario_abertura or not horario_abertura.strip():
            raise ClinicaNaoInformadaException(
                "O horário de abertura é obrigatório."
            )

        if not horario_fechamento or not horario_fechamento.strip():
            raise ClinicaNaoInformadaException(
                "O horário de fechamento é obrigatório."
            )

        clinica = Clinica(
            nome.strip(),
            localizacao.strip(),
            descricao.strip(),
            horario_abertura.strip(),
            horario_fechamento.strip()
        )

        self.__clinicas.append(clinica)
        return True

    def excluir_clinica(self, nome_clinica):
        nome_normalizado = self.__normalizar_nome(nome_clinica)

        clinica = next(
            (
                c for c in self.__clinicas
                if c.nome.strip().casefold() == nome_normalizado
            ),
            None
        )

        if clinica is None:
            raise ClinicaNaoEncontradaException(
                f"Não existe uma clínica cadastrada com o nome "
                f"'{nome_clinica.strip()}'."
            )

        self.__clinicas.remove(clinica)
        return True

    def listar_clinicas(self):
        return list(self.__clinicas)

    def alterar_dados_clinica(
        self, nome_atual, novo_nome, nova_localizacao,
        nova_descricao, novo_horario_abertura,
        novo_horario_fechamento
    ):
        nome_atual_normalizado = self.__normalizar_nome(nome_atual)
        novo_nome_normalizado = self.__normalizar_nome(novo_nome)

        clinica = next(
            (
                c for c in self.__clinicas
                if c.nome.strip().casefold() == nome_atual_normalizado
            ),
            None
        )

        if clinica is None:
            raise ClinicaNaoEncontradaException(
                f"Não foi encontrada uma clínica com o nome "
                f"'{nome_atual.strip()}'."
            )

        for outra_clinica in self.__clinicas:
            if (
                outra_clinica is not clinica
                and outra_clinica.nome.strip().casefold()
                == novo_nome_normalizado
            ):
                raise ClinicaDuplicadaException(
                    f"Não é possível alterar o nome para "
                    f"'{novo_nome.strip()}': esse nome já está cadastrado."
                )

        if not nova_localizacao or not nova_localizacao.strip():
            raise ClinicaNaoInformadaException(
                "A nova localização da clínica é obrigatória."
            )

        if not nova_descricao or not nova_descricao.strip():
            raise ClinicaNaoInformadaException(
                "A nova descrição da clínica é obrigatória."
            )

        if not novo_horario_abertura or not novo_horario_abertura.strip():
            raise ClinicaNaoInformadaException(
                "O novo horário de abertura é obrigatório."
            )

        if not novo_horario_fechamento or not novo_horario_fechamento.strip():
            raise ClinicaNaoInformadaException(
                "O novo horário de fechamento é obrigatório."
            )

        clinica.nome = novo_nome.strip()
        clinica.localizacao = nova_localizacao.strip()
        clinica.descricao = nova_descricao.strip()
        clinica.horario_abertura = novo_horario_abertura.strip()
        clinica.horario_fechamento = novo_horario_fechamento.strip()

        return True

    def verificar_existencia(self, nome_clinica):
        nome_normalizado = self.__normalizar_nome(nome_clinica)

        existe = any(
            c.nome.strip().casefold() == nome_normalizado
            for c in self.__clinicas
        )

        if not existe:
            raise ClinicaNaoEncontradaException(
                f"Não existe uma clínica cadastrada com o nome "
                f"'{nome_clinica.strip()}'."
            )

        return True

    def buscar_clinica_nome(self, nome_clinica):
        nome_normalizado = self.__normalizar_nome(nome_clinica)

        return next(
            (
                c for c in self.__clinicas
                if c.nome.strip().casefold() == nome_normalizado
            ),
            None
        )