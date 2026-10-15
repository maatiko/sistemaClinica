from exception.excecoes import ErroClinica


class TelaSistema:

    def __init__(self, controlador_sistema):
        self.__sistema = controlador_sistema

    def iniciar(self):
        while True:
            print("\n===== SISTEMA DE CLÍNICA =====")
            print("1 - Clínicas")
            print("2 - Pessoas")
            print("3 - Consultas")
            print("4 - Pagamentos")
            print("5 - Relatórios")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "0":
                print("Encerrando o sistema.")
                break

            try:
                self.__sistema.abrir_menu(opcao)
            except (ErroClinica, ValueError, TypeError, AttributeError) as erro:
                print(f"\n[Erro] {erro}")
            except Exception as erro:
                print(f"\n[Erro inesperado] {erro}")