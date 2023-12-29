'''
Para este desafio, imagine que temos uma loja de carros. Vamos criar uma 
lista com os carros que você tem em estoque:
"BMW X6 - BMW I5 - BMW I8"

Peça ao usuário para que ele insira o nome do carro que deseja comprar.

Vamos verificar a disponibilidade no estoque da loja.

retorno para o usuário:

- Este carro está dispónivel 
- Desculpe, este carro não está dispónivel.

'''

#Criar um estoque de carro:
estoque_carros = ['BMWX6', 'BMWI5', 'BMWI8']

#Entrada do usuário:
comprar_carro = input("Qual carro você deseja? ").upper()

#Verificar diponibilidade no estoque.
if comprar_carro in estoque_carros:
    #Saida.
    print('Esté carro está dispónivel')
else:
    print('Desculpe, este carro não está dísponivel.')




