from datetime import datetime
class TelaSistema:
    def __init__(self,ControladorSistema):
        self.__sistema = ControladorSistema

    def iniciar(self):
        while True:
            print("\n"+"*" * 40)
            print("SISTEMA DE GESTÃO CLÍNICAS")
            print("-"*40)
            print("Gostaria de acessar:")
            print("1. Menu das Clínicas")
            print("2. Menu de Paciente/Profissionais ")
            print("3. Menu de Consultas")
            print("4. Menu de Pagamento")
            print("5. Menu de Relatórios")
            print("0. Sair")
            print("="*40)

            opcao = input("Selecione uma opção:").strip()

            if opcao == "0":
                print("Encerrando o Sistema.")
                break
            self.__sistema.abrir_menu(opcao)