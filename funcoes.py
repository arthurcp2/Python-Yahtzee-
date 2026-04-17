def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    lista_dados = []
    dados_no_estoque.append(dados_rolados[dado_para_guardar])
    del dados_rolados[dado_para_guardar]
    lista_dados.append(dados_rolados)
    lista_dados.append(dados_no_estoque)
    return lista_dados