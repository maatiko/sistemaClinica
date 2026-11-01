from controller.controlador_sistema import ControladorSistema
from seeder.seeder import popular_sistema

if __name__ == "__main__":
    sistema = ControladorSistema()
    popular_sistema(sistema)#fazer testes mais rápidos
    sistema.iniciar()