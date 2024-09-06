class Avaliacao:
    """Representa uma avaliação de um produto ou serviço.

    Uma avaliação é composta por um cliente e uma nota numérica.

    Args:
        cliente (str): Nome do cliente que realizou a avaliação.
        nota (float): Nota atribuída pelo cliente, geralmente em uma escala de 1 a 5.
    """
    def __init__(self, cliente, nota):
        """Inicializa uma nova instância de Avaliação.

        Args:
            cliente (str): Nome do cliente que realizou a avaliação.
            nota (float): Nota atribuída pelo cliente, geralmente em uma escala de 1 a 5.
        """
        self._cliente = cliente
        self._nota = nota
