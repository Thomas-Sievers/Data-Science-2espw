array = list(range(10000))

# Retorna o index que o alvo se localiza
def busca_binaria_achar_porcentagem(lista, alvo):
    l, h = 0, len(lista) - 1
    while l <= h:
        m = (l + h) // 2
        if lista[m] == alvo:
            return (m / len(lista)) * 100
        elif lista[m] < alvo:
            l = m + 1
        else:
            h = m - 1
    return -1

print("Porcentagem do alvo: ", busca_binaria_achar_porcentagem(array, 5300), "%")