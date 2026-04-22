def calcula_pontos_regra_simples(lnu):
    dic={1:0,2:0,3:0,4:0,5:0,6:0}
    for i in lnu:
        if i in dic:
            dic[i]+=i
    return dic
