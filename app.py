from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato


restaurante_praca = Restaurante('Praça', 'Gourmet')

bebida_suco = Bebida('Suco de Melancia',  5.0, 'Melancia', 'Grande')
bebida_suco.aplicar_desconto()

prato_paozinho = Prato('Pãozinho fofo', 10.0, 'Tradicionalmente feito com pão de milho e coberto por um delicioso molho, o melhor de SP.')
prato_paozinho.aplicar_desconto()

restaurante_praca.add_no_cardapio(bebida_suco)
restaurante_praca.add_no_cardapio(prato_paozinho)




def main():
   restaurante_praca.exibir_cardapio
   


if __name__ == '__main__':
    main()
