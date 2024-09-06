from modelos.cardapio.item_cardapio import ItemCardapio


class Bebida(ItemCardapio):
    """Representa um item de bebida no cardápio, herdando de ItemCardapio.
    Args:
        nome (str): Nome da bebida.
        preco (float): Preço da bebida.
        sabor (str): Sabor da bebida.
        tamanho (str): Tamanho da bebida (pequeno, médio, grande, etc).
    """
    def __init__(self, nome, preco, sabor, tamanho):
        """Inicializa uma nova instância de Bebida.
        Args:
            nome (str): Nome da bebida.
            preco (float): Preço da bebida.
            sabor (str): Sabor da bebida.
            tamanho (str): Tamanho da bebida.
        """
        super().__init__(nome,preco) # Chama o construtor da classe pai
        self._sabor = sabor
        self.tamanho = tamanho

    def __str__(self):
        """Retorna uma representação em string da bebida, utilizando apenas o nome.
        Returns:
            str: Nome da bebida.
        """
        return self._nome
    
    def aplicar_desconto(self):
        """Aplica um desconto de 8% no preço da bebida."""
        self._preco -= (self._preco * 0.08)
