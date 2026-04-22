def remover_dado(lrolados,lestoque,irem):
    lrolados.append(lestoque[irem])
    del lestoque[irem]
    return [lrolados,lestoque]
