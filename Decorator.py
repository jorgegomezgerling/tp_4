from abc import ABC, abstractmethod

# Interfaz Component
class Component(ABC):
    @abstractmethod
    def obtener_valor(self) -> int:
        pass

# Clase base Numero que implementa Component
class Numero(Component):
    def __init__(self, valor: int):
        self.valor = valor

    def obtener_valor(self) -> int:
        return self.valor

# Clase base para los decoradores
class OperacionDecorator(Component):
    def __init__(self, componente: Component):
        self.componente = componente

    def obtener_valor(self) -> int:
        return self.componente.obtener_valor()

# Clases concretas de los decoradores
class SumarDos(OperacionDecorator):
    def obtener_valor(self) -> int:
        return super().obtener_valor() + 2

class MultiplicarPorDos(OperacionDecorator):
    def obtener_valor(self) -> int:
        return super().obtener_valor() * 2

class DividirPorTres(OperacionDecorator):
    def obtener_valor(self) -> int:
        return super().obtener_valor() // 3

# Uso del patrón Decorator
if __name__ == "__main__":
    numero = Numero(10)
    print(f"Número original: {numero.obtener_valor()}")

    # Agregar decoradores para realizar las operaciones
    numero_modificado = DividirPorTres(MultiplicarPorDos(SumarDos(numero)))
    print(f"Número modificado: {numero_modificado.obtener_valor()}")
