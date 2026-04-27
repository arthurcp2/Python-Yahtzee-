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
#EX6
def calcula_pontos_sequencia_baixa (l):
    if 1 in l and 2 in l and 3 in l and 4 in l:
        return 15
    elif 2 in l and 3 in l and 4 in l and 5 in l:
        return 15
    elif 3 in l and 4 in l and 5 in l and 6 in l:
        return 15
    else:
        return 0
#EX7
def calcula_pontos_sequencia_alta (l):
    if 1 in l and 2 in l and 3 in l and 4 in l and 5 in l:
        return 30
    elif 2 in l and 3 in l and 4 in l and 5 in l and 6 in l:
        return 30
    else:
        return 0
#EX8
def calcula_pontos_full_house (n):
    dic={}
    cont=0
    p=0
    for i in n:
        p+=i
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for e in dic:
        cont +=1
    if cont!=2:
        return 0
    s=[]
    for m in dic.values():
        s.append(m)
    if s==[2,3] or s==[3,2]:
        return p
    return 0
