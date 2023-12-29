<h1>Desafio 18 - Verificação de Disponibilidade de Carro em Estoque</h1>
<p>
Este código visa criar um sistema simples para verificar a disponibilidade de carros em um estoque com base na escolha do usuário.
</p>

<h4>Passos:</h4>

<ol>
<h2><li>Estoque de Carros:</li></h2>

<ul>
<li>Inicializa um estoque de carros representado por uma lista.</li>
</ul>

    estoque_carros = ['BMWX6', 'BMWI5', 'BMWI8']

<h2><li>Entrada do Usuário:</li></h2>
<ul>
<li>Utiliza a função input para permitir que o usuário escolha um carro.</li>
<li>Converte a entrada para maiúsculas usando upper() para garantir correspondência insensível a maiúsculas e minúsculas.</li>
</ul>

    comprar_carro = input("Qual carro você deseja? ").upper()

<h2><li>Verificação de Disponibilidade:</li></h2>
<ul>
<li>Utiliza uma estrutura condicional (if) para verificar se o carro escolhido pelo usuário está presente no estoque.</li>
<li>Em caso afirmativo, exibe a mensagem 'Este carro está disponível'.</li>
<li>Em caso contrário, exibe a mensagem 'Desculpe, este carro não está disponível'.</li>
</ul>

    if comprar_carro in estoque_carros:
        print('Este carro está disponível')
    else:
        print('Desculpe, este carro não está disponível.')
</ol>

<h3>Mensagens Personalizadas:</h3>
<li><b>Disponível:</b> Se o carro escolhido estiver no estoque.</li>
<li><b>Indisponível:</b> Se o carro escolhido não estiver no estoque.</li>

<h3>Interatividade:</h3>
<p>O código fornece uma experiência interativa ao informar ao usuário sobre a disponibilidade do carro escolhido, tornando o processo de seleção de carro mais informativo.</p>

<h3>Conclusão:</h3>
<p>Ao executar este código, o usuário receberá uma mensagem indicando se o carro desejado está disponível no estoque, simplificando a decisão de compra.</p>