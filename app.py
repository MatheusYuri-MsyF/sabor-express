from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

# Cria um restaurante chamado "Praça" com categoria "Gourmet"
restaurante_praca = Restaurante('Praça', 'Gourmet')

# Cria uma bebida "Suco de Melancia" com preço, ingredientes e tamanho
bebida_suco = Bebida('Suco de Melancia',  5.0, 'Melancia', 'Grande')
# Aplica um desconto ao suco (método não definido aqui)
bebida_suco.aplicar_desconto()

# Cria um prato "Pãozinho fofo" com preço e descrição detalhada
prato_paozinho = Prato('Pãozinho fofo', 10.0, 'Tradicionalmente feito com pão de milho e coberto por um delicioso molho, o melhor de SP.')
# Aplica um desconto ao prato (método não definido aqui)
prato_paozinho.aplicar_desconto()

# Adiciona a bebida e o prato ao cardápio do restaurante
restaurante_praca.add_no_cardapio(bebida_suco)
restaurante_praca.add_no_cardapio(prato_paozinho)




def main():
   # Exibe o cardápio completo do restaurante
   restaurante_praca.exibir_cardapio
   


if __name__ == '__main__':
    main()
