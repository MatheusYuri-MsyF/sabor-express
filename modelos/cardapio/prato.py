from modelos.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    """Representa um prato no cardápio, herdando de ItemCardapio.
    Args:
        nome (str): Nome do prato.
        preco (float): Preço do prato.
        descricao (str): Descrição detalhada do prato.
    """
    def __init__(self, nome, preco, descricao):
        """Inicializa uma nova instância de Prato.
        Args:
            nome (str): Nome do prato.
            preco (float): Preço do prato.
            descricao (str): Descrição detalhada do prato.
        """
        super().__init__(nome, preco) # Chama o construtor da classe pai
        self.descricao = descricao

    def __str__(self):
        """Retorna uma representação em string do prato, utilizando apenas o nome.
        Returns:
            str: Nome do prato.
        """
        return self._nome

    def aplicar_desconto(self):
        """Aplica um desconto de 5% no preço do prato."""
        self._preco -= (self._preco * 0.05)
