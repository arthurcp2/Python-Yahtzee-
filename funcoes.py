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
