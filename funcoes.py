#EX1
import random
def rolar_dados(n):
    l = []
    for i in range(n):
        l.append(random.randint(1, 6))
    return l
#EX2
def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    lista_dados = []
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    del dados_rolados[dado_para_guardar]
    lista_dados.append(dados_rolados)
    lista_dados.append(dados_no_estoque)
    return lista_dados
#EX3
def remover_dado(lrolados,lestoque,irem):
    lrolados.append(lestoque[irem])
    del lestoque[irem]
    return [lrolados,lestoque]
#EX4
def calcula_pontos_regra_simples(lnu):
    dic={1:0,2:0,3:0,4:0,5:0,6:0}
    for i in lnu:
        if i in dic:
            dic[i]+=i
    return dic
#EX5
def calcula_pontos_soma (l):
    som=0
    for i in l:
        som+=i
    return som
