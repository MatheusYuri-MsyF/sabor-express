from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    """Representa uma sobremesa no cardápio, herdando de ItemCardapio.
    Args:
        nome (str): Nome da sobremesa.
        preco (float): Preço da sobremesa.
        descricao (str): Descrição detalhada da sobremesa.
        tipo (str): Tipo da sobremesa (bolo, torta, mousse, etc).
        tamanho (str): Tamanho da sobremesa (individual, médio, grande, etc).
    """
    def __init__(self, nome, preco, descricao, tipo, tamanho):
        """Inicializa uma nova instância de Sobremesa.
        Args:
            nome (str): Nome da sobremesa.
            preco (float): Preço da sobremesa.
            descricao (str): Descrição detalhada da sobremesa.
            tipo (str): Tipo da sobremesa (bolo, torta, mousse, etc).
            tamanho (str): Tamanho da sobremesa (individual, médio, grande, etc).
        """
        super().__init__(nome, preco) # Chama o construtor da classe pai
        self.descricao = descricao
        self.tipo = tipo
        self.tamanho = tamanho

    def __str__(self):
        """Retorna uma representação em string da sobremesa, utilizando apenas o nome.
        Returns:
            str: Nome da sobremesa.
        """
        return self._nome

    def aplicar_desconto(self):
        """Aplica um desconto de 15% no preço da sobremesa."""
        self._preco -= (self._preco * 0.15)
