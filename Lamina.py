from __future__ import annotations
from abc import ABC, abstractmethod


class Lamina(ABC):
    """
    La abstracción Lamina representa las láminas de acero.
    """

    def __init__(self, espesor: float, ancho: float, laminador: Laminador) -> None:
        self.espesor = espesor
        self.ancho = ancho
        self.laminador = laminador

    @abstractmethod
    def producir(self) -> str:
        pass


class Lamina5Metros(Lamina):
    """
    Implementación concreta de Lamina para láminas de 5 metros.
    """

    def producir(self) -> str:
        return f"Lámina de {self.espesor}'' x {self.ancho} metros producida en el laminador de 5 metros."


class Lamina10Metros(Lamina):
    """
    Implementación concreta de Lamina para láminas de 10 metros.
    """

    def producir(self) -> str:
        return f"Lámina de {self.espesor}'' x {self.ancho} metros producida en el laminador de 10 metros."


class Laminador(ABC):
    """
    La abstracción Laminador representa los trenes laminadores.
    """

    def __init__(self, lamina: Lamina) -> None:
        self.lamina = lamina

    @abstractmethod
    def producir_lamina(self) -> str:
        pass


class Laminador5Metros(Laminador):
    """
    Implementación concreta de Laminador para el laminador de 5 metros.
    """

    def producir_lamina(self) -> str:
        return "Iniciando producción en el laminador de 5 metros.\n" + self.lamina.producir()


class Laminador10Metros(Laminador):
    """
    Implementación concreta de Laminador para el laminador de 10 metros.
    """

    def producir_lamina(self) -> str:
        return "Iniciando producción en el laminador de 10 metros.\n" + self.lamina.producir()


def client_code(laminador: Laminador) -> None:
    """
    El código del cliente interactúa con la abstracción Laminador.
    """

    print(laminador.producir_lamina())


if __name__ == "__main__":
    # Ejemplo de uso

    lamina_5m = Lamina5Metros(0.5, 1.5, Laminador5Metros)
    lamina_10m = Lamina10Metros(0.5, 1.5, Laminador10Metros)

    laminador_5m = Laminador5Metros(lamina_5m)
    laminador_10m = Laminador10Metros(lamina_10m)

    client_code(laminador_5m)
    client_code(laminador_10m)
