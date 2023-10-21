n, k = map(int, input().split())
lista_zero_um = [0] * n
lista_prioridade = [0] * n
chaves = list(map(int, input().split()))

def insere(lista_zero_um, lista_prioridade, chaves, i):
    lista_zero_um[i] = 1
    lista_prioridade[i] = chaves[i]
    return lista_zero_um

def minimo(lista_prioridade):
    valores_nao_zero = [valor for valor in lista_prioridade if valor != 0]
    valor_minimo = min(valores_nao_zero)
    indice_valor_minimo = lista_prioridade.index(valor_minimo)

    return indice_valor_minimo

def extraiMinimo(lista_prioridade, lista_zero_um):
    indice_valor_minimo = minimo(lista_prioridade)
    valor_minimo = lista_prioridade[indice_valor_minimo]
    lista_zero_um[indice_valor_minimo] = 0
    lista_prioridade[indice_valor_minimo] = 0
    
    return lista_zero_um, indice_valor_minimo, valor_minimo

def busca(i, lista_zero_um):
    if(lista_zero_um[i] == 1):
        return 1
    else:
        return 0 

def vazio(lista_zero_um):
    if(all(val == 0 for val in lista_zero_um)):
        return True
    else:
        return False

for _ in range(k):
    operacao = input().split()
    if operacao[0] == 'I':
        i = int(operacao[1])
        fila = insere(lista_zero_um, lista_prioridade, chaves, i)
        print(fila)
    elif operacao[0] == 'M':
        index_minimo = minimo(lista_prioridade)
        print(f"{index_minimo} {chaves[index_minimo]} {lista_zero_um}")
    elif operacao[0] == 'E':
        retorno_lista_zero_um, indice_valor_minimo, valor_minimo = extraiMinimo(lista_prioridade, lista_zero_um)
        print(f"{indice_valor_minimo} {valor_minimo} {retorno_lista_zero_um}")
    elif operacao[0] == 'B':
        i = int(operacao[1])
        resultado = busca(i, lista_zero_um)
        print(f"{resultado} {lista_zero_um}")     
    elif operacao[0] == 'V':
        resultado = vazio(lista_zero_um)
        print(f"{resultado} {lista_zero_um}")
