class ErroClinica(Exception):
    """Classe-base para erros esperados do sistema."""


class ErroValidacao(ErroClinica):
    pass


class DadosInvalidos(ErroValidacao):
    pass


class CampoObrigatorio(ErroValidacao):
    pass


class DataInvalida(ErroValidacao):
    pass


class HorarioInvalido(ErroValidacao):
    pass


class ValorInvalido(ErroValidacao):
    pass


class IdadeInvalida(ErroValidacao):
    pass


class ErroCadastro(ErroClinica):
    pass


class RegistroDuplicado(ErroCadastro):
    pass


class PessoaDuplicada(RegistroDuplicado):
    pass


class ClinicaDuplicada(RegistroDuplicado):
    pass


class ConsultaDuplicada(RegistroDuplicado):
    pass


class RegistroNaoEncontrado(ErroClinica):
    pass


class ClinicaNaoEncontrada(RegistroNaoEncontrado):
    pass


class PessoaNaoEncontrada(RegistroNaoEncontrado):
    pass


class PacienteNaoEncontrado(PessoaNaoEncontrada):
    pass


class ProfissionalNaoEncontrado(PessoaNaoEncontrada):
    pass


class ConsultaNaoEncontrada(RegistroNaoEncontrado):
    pass


class PagamentoNaoEncontrado(RegistroNaoEncontrado):
    pass


class ErroConsulta(ErroClinica):
    pass


class ConflitoHorario(ErroConsulta):
    pass


class ForaDoExpediente(ErroConsulta):
    pass


class ConsultaInvalida(ErroConsulta):
    pass


class ErroPagamento(ErroClinica):
    pass


class PagamentoInvalido(ErroPagamento):
    pass


class ModalidadePagamentoInvalida(PagamentoInvalido):
    pass


class DadosPixInvalidos(PagamentoInvalido):
    pass


class DadosCartaoInvalidos(PagamentoInvalido):
    pass


class PagamentoAcimaDoSaldo(PagamentoInvalido):
    pass


class SemSaldoDevedor(ErroPagamento):
    pass


class SaldoDevedorInexistente(ErroPagamento):
    pass


class DataPagamentoInvalida(PagamentoInvalido):
    pass