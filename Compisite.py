from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

class Pieza(Component):
    def operation(self) -> str:
        return "Pieza"

class PiezaSimple(Pieza):
    pass

class Subconjunto(Pieza):
    def __init__(self) -> None:
        self._children: List[Pieza] = []

    def add(self, pieza: Pieza) -> None:
        self._children.append(pieza)

    def remove(self, pieza: Pieza) -> None:
        self._children.remove(pieza)

    def operation(self) -> str:
        results = []
        for pieza in self._children:
            results.append(pieza.operation())
        return f"Subconjunto({', '.join(results)})"

if __name__ == "__main__":
    # Crear piezas simples
    pieza1 = PiezaSimple()
    pieza2 = PiezaSimple()
    pieza3 = PiezaSimple()
    pieza4 = PiezaSimple()
    
    # Crear subconjuntos
    subconjunto1 = Subconjunto()
    subconjunto2 = Subconjunto()
    subconjunto3 = Subconjunto()
    subconjunto4 = Subconjunto()
    
    # Agregar piezas a los subconjuntos
    subconjunto1.add(pieza1)
    subconjunto1.add(pieza2)
    subconjunto1.add(pieza3)
    subconjunto1.add(pieza4)
    
    subconjunto2.add(pieza1)
    subconjunto2.add(pieza2)
    subconjunto2.add(pieza3)
    subconjunto2.add(pieza4)
    
    subconjunto3.add(pieza1)
    subconjunto3.add(pieza2)
    subconjunto3.add(pieza3)
    subconjunto3.add(pieza4)
    
    subconjunto4.add(pieza1)
    subconjunto4.add(pieza2)
    subconjunto4.add(pieza3)
    subconjunto4.add(pieza4)
    
    # Crear el producto principal
    producto_principal = Subconjunto()
    producto_principal.add(subconjunto1)
    producto_principal.add(subconjunto2)
    producto_principal.add(subconjunto3)
    
    # Mostrar la configuración
    print(producto_principal.operation())

    # Agregar el subconjunto opcional adicional
    subconjunto_opcional = Subconjunto()
    subconjunto_opcional.add(pieza1)
    subconjunto_opcional.add(pieza2)
    subconjunto_opcional.add(pieza3)
    subconjunto_opcional.add(pieza4)

    producto_principal.add(subconjunto_opcional)

    # Mostrar la configuración actualizada
    print(producto_principal.operation())
