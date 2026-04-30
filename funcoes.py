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
def calcula_pontos_soma(l):
    som=0
    for i in l:
        som+=i
    return som
#EX6
def calcula_pontos_sequencia_baixa(l):
    if 1 in l and 2 in l and 3 in l and 4 in l:
        return 15
    elif 2 in l and 3 in l and 4 in l and 5 in l:
        return 15
    elif 3 in l and 4 in l and 5 in l and 6 in l:
        return 15
    else:
        return 0
#EX7
def calcula_pontos_sequencia_alta(l):
    if 1 in l and 2 in l and 3 in l and 4 in l and 5 in l:
        return 30
    elif 2 in l and 3 in l and 4 in l and 5 in l and 6 in l:
        return 30
    else:
        return 0
#EX8
def calcula_pontos_full_house(n):
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
#EX9
def calcula_pontos_quadra(n):
    dic={}
    p=0
    for i in n:
        p+=i
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for m in dic.values():
        if m >=4:
            return p
    return 0
#EX10
def calcula_pontos_quina(n):
    dic={}
    p=0
    for i in n:
        p+=i
        if i not in dic:
            dic[i]=1
        else:
            ]            dic[i]+=1
    for m in dic.values():
        if m >=5:
            return 50
    return 0
#EX11
def calcula_pontos_regra_avancada(dados_rolados):
    dic = {"cinco_iguais": 0,"full_house": 0,"quadra": 0, "sem_combinacao": 0,"sequencia_alta": 0,"sequencia_baixa": 0}
    dic["cinco_iguais"] += calcula_pontos_quina(dados_rolados)
    dic["full_house"] += calcula_pontos_full_house(dados_rolados)
    dic["quadra"] += calcula_pontos_quadra(dados_rolados)
    dic["sem_combinacao"] += calcula_pontos_soma(dados_rolados)
    dic["sequencia_alta"] += calcula_pontos_sequencia_alta(dados_rolados)
    dic["sequencia_baixa"] += calcula_pontos_sequencia_baixa(dados_rolados)
    return dic
#EX12
def faz_jogada (l,s,d):
    if s.isdigit():
        a=(calcula_pontos_regra_simples(l))
        d['regra_simples'][int(s)]= a[int(s)]
    else:
        a= calcula_pontos_regra_avancada(l)
        d['regra_avancada'][s]=a[s]
    return d
