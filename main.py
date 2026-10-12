from controller import (
    controladorConsulta,
    controladorRelatorio,
    controladorClinica,
    controladorPessoa,
    controladorPagamento
)
from view import telaSistema

if __name__ == "__main__":
  clinica_ctrl = controladorClinica()
  consulta_ctrl = controladorConsulta()
  pagamento_ctrl = controladorPagamento()
  relatorio_ctrl = controladorRelatorio()
  pessoa_ctrl = controladorPessoa()

  tela_sistema = telaSistema(
      clinica_ctrl, consulta_ctrl, pagamento_ctrl, relatorio_ctrl,pessoa_ctrl
  )

  tela_sistema.iniciar()