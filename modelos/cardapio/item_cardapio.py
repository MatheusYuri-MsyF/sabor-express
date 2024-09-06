from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    """Classe abstrata que representa um item de cardápio de forma genérica.

    Esta classe serve como base para outras classes mais específicas, como Bebida, Prato,
    Sobremesa, etc. Define os atributos básicos de um item de cardápio e um método abstrato
    para aplicar descontos, que deverá ser implementado pelas classes filhas.
    """
    def __init__(self, nome, preco):
        """Inicializa um novo item de cardápio.
        Args:
            nome (str): Nome do item.
            preco (float): Preço do item.
        """
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        """Método abstrato para aplicar um desconto no preço do item.

        Este método deve ser implementado pelas classes filhas para definir a lógica
        específica de cálculo do desconto para cada tipo de item.
        """
        pass
    
