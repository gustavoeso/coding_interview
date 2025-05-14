def group_anagrams(words):
    """
    Agrupa palavras que são anagramas entre si usando ordenação externa e comparação manual.

    :param words: Lista de palavras
    :return: Lista de listas com grupos de anagramas
    """
    # Etapa 1: Cria lista auxiliar com (palavra original, palavra ordenada)
    reorganizadas = []
    for palavra in words:
        chave = ''.join(sorted(palavra))
        reorganizadas.append((palavra, chave))

    # Etapa 2: Agrupa no dicionário com base em chaves iguais consecutivas
    grupos = {}
    for palavra, chave in reorganizadas:
        if chave not in grupos:
            grupos[chave] = [palavra]
        else:
            grupos[chave].append(palavra)

    # Etapa 4: Retorna apenas os valores agrupados
    return list(grupos.values())


entrada = ["eat", "tea", "tan", "ate", "nat", "bat"]
saida = group_anagrams(entrada)
print(saida)