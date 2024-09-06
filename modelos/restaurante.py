from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    """Representa um restaurante, com informações como nome, categoria, status, avaliações e cardápio.

    A classe `Restaurante` mantém uma lista de todos os restaurantes criados.
    """
    restaurantes = []

    def __init__(self, nome, categoria):
        """Inicializa um novo restaurante.

        Args:
            nome (str): Nome do restaurante.
            categoria (str): Categoria do restaurante (e.g., ITALIANA, BRASILEIRA).
        """
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        #Retorna uma representação em string do restaurante, mostrando nome e categoria.
        return f' {self._nome} | {self._categoria}'

    @classmethod
    def listar_restaurantes(cls): 
        #Método de classe para listar todos os restaurantes, exibindo nome, categoria, média de avaliações e status.
        print(
            f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}\n")
        for restaurante in cls.restaurantes:
            print(
                f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_de_avaliacoes ).ljust(25)} | {restaurante.ativo}")

    @property
    def ativo(self):
        #Propriedade que retorna uma representação visual do status do restaurante (⌧ para ativo, ☐ para inativo).
        return '⌧' if self._ativo else '☐'

    def alternar_estado(self):
        #Alterna o estado do restaurante entre ativo e inativo.
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        #Adiciona uma nova avaliação ao restaurante.
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_de_avaliacoes(self):
        """Calcula a média das avaliações do restaurante.
    Percorre a lista de avaliações, soma as notas e calcula a média.
    Dividi a média por 2 para obter uma escala de 0 a 5 (assumindo que as notas variam de 1 a 10).
    Retorna '-' se não houver avaliações.

    Returns:
        float: Média das avaliações do restaurante (de 0 a 5).
    """
        if not self._avaliacao:
            return '-'
        somatorio = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade = len(self._avaliacao) 
        media = somatorio/quantidade
        media_limitada = round(media/2, 1)
        return media_limitada
    
    def add_no_cardapio(self,item):
        #Adiciona um item ao cardápio do restaurante, verificando se o item é uma instância de ItemCardapio.
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self): 
    #Exibe o cardápio do restaurante, formatando a saída de acordo com o tipo de item (prato ou bebida).
            print(f'Cardapio do Restaurante {self._nome}\n')
            for i,item in enumerate(self._cardapio, start=1):
                if hasattr(item,'descricao'):
                    mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                    print(mensagem_prato)
                else:
                    mensagem_bebida= f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                    print(mensagem_bebida)


    



   
