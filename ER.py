import re

entrada = open('lista.txt', 'r')
er_nome = '[Oo]i, eu sou [oa] |[Ee]u sou [oa] |[Ss]ou [oa] |(\w+)'
er_verbo = '[Gg]ostaria de |e [Gg]ostaria de |e [Qq]ueria |\w+'
comprar = 0
saber = 0;
ver = 0;
vender = 0;
nomes = []
verbos = []
produtos = []
total = [];
nomes_dinamico = []
lista_comprados = []
dic_nome = {}
dic_acao = {}
dic_produto = {}
acoes = ['comprar', 'saber', 'ver', 'vender']
produtos = ['teclado', 'mouse', 'monitor', 'cpu']
precos = {"teclado": 100, "mouse": 50, "monitor":500, "cpu":800}
linhas = entrada.readlines();

for linha in linhas:
    nome = linha.split('.')[0]
    verbo = linha.split('.')[1]
    padrao_verbo = re.findall(er_verbo, verbo)
    verbo = padrao_verbo[1]
    verbos.append(verbo)
    padrao_nome = re.findall(er_nome, nome)
    nome = padrao_nome[1]
    nomes.append(nome)
    for prod in produtos:
        if prod in linha:
            string = nome, verbo, prod  
            total.append(string)

def cont_nomes():     
    for est in total:
        if est[0] not in nomes_dinamico:
            nomes_dinamico.append(est[0]) 

    for nome in nomes_dinamico:        
        dic_nome[nome] = nomes.count(nome)
    return dic_nome

def cont_acoes():    
    acoes_dinamico = []
    for est in total:
        if est[1] not in acoes_dinamico:
            acoes_dinamico.append(est[1]) 

    for acao in acoes_dinamico:        
        dic_acao[acao] = verbos.count(acao)
    return dic_acao

def cont_prod():    
    prod_dinamico = []
    for est in total:
        prod_dinamico.append(est[2]) 
    
    for produto in produtos:        
        dic_produto[produto] = prod_dinamico.count(produto)

    return dic_produto

def acoes_max_min():
    maior = -999
    menor = 999
    tupla_acao_maior = ()
    tupla_acao_menor = ()
    for e in dic_acao.items():
        if int(e[1]) >= maior:
            maior = int(e[1])
            tupla_acao_maior = e
        if int(e[1]) <= menor:
            menor = int(e[1])
            tupla_acao_menor = e
    return tupla_acao_maior, tupla_acao_menor

def produto_max_min():
    maior = -999
    menor = 999
    tupla_prod_maior = ()
    tupla_prod_menor = ()
    for e in dic_produto.items():
        if int(e[1]) >= maior:
            maior = int(e[1])
            tupla_prod_maior = e
        if int(e[1]) <= menor:
            menor = int(e[1])
            tupla_prod_menor = e
    return tupla_prod_maior, tupla_prod_menor

def cliente_max_min():
    maior = -999
    menor = 999
    tupla_cliente_maior = ()
    tupla_cliente_menor = ()
    for e in dic_nome.items():
        if int(e[1]) >= maior:
            maior = int(e[1])
            tupla_cliente_maior = e
        if int(e[1]) <= menor:
            menor = int(e[1])
            tupla_cliente_menor = e
    return tupla_cliente_maior, tupla_cliente_menor

def total_comprados():
    total = 0
    for l in lista_comprados:
        quant1 = 0
        soma1 = 0
        for p in precos.items():
            if l[2]==p[0]:
                quant1+=1
                soma1+=p[1]
        total += quant1*soma1
    return total

def quantidade_comprar():    
    lista_nomes = []
    dic_n = {}
    for comprar in total:
        if comprar[1] == 'comprar':
            lista_comprados.append(comprar)

    for item in lista_comprados:
        lista_nomes.append(item[0])     
    for nome in nomes_dinamico:        
        dic_n[nome] = lista_nomes.count(nome)

    maior = -999
    menor = 999
    tupla_compra_maior = ()
    tupla_compra_menor = ()
    for e in dic_n.items():
        if int(e[1]) >= maior:
            maior = int(e[1])
            tupla_compra_maior = e
        if int(e[1]) <= menor:
            menor = int(e[1])
            tupla_compra_menor = e
    return tupla_compra_maior, tupla_compra_menor

print("Quantidade de interações por cliente:",cont_nomes())
print("Quantidade de solicitações por ação:",cont_acoes())
print("Quantidade total de solicitações por produto:",cont_prod())
print("Ação com a maior e a menor quantidade de solicitação envolvida:",acoes_max_min())
print("Produto com a maior e a menor quantidade de solicitações envolvidas:",produto_max_min())
print("Cliente com a maior e a menor quantidade de solicitações efetuadas:",cliente_max_min())
print("Cliente que realizou a maior e a menor quantidade de solicitação (comprar):",quantidade_comprar())
total_comprados()
