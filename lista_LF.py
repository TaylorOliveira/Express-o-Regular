#esse script cria a lista de frases que vão virar estatistica
import random
acoes = ['comprar', 'saber', 'ver', 'vender']
nomes = ['Lucas', 'Taylor', 'Joao', 'Maria', 'Juliana', 'Erika']
produtos = ['teclado', 'mouse', 'monitor', 'cpu']

arq = open('lista.txt','w')

for i in range(70):
    acao = random.choice(acoes)
    produto = random.choice(produtos)
    nome = random.choice(nomes)
    if acao == 'saber':
        arq.write('Oi, eu sou o  {0}. Gostaria de {1} o preço de um {2} \n'.format(nome, acao, produto))
    else:
        arq.write('Eu sou o {0}. Gostaria de {1} um {2} \n'.format(nome, acao, produto))

arq.close()
print ("Lista criada.")
