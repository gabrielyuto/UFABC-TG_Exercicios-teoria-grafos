def cria_grafo(n, m):
  grafo = [[] for _ in range(n)]
  
  for _ in range(m):
    u, v = map(int, input().split())
    grafo[u].append(v)
  
  return grafo  

def grafo_transposto(grafo):
  n = len(grafo)

  grafo_transposto = [[] for _ in range(n)]

  for u in range(n):
      for v in grafo[u]:
          grafo_transposto[v].append(u)

  return grafo_transposto

def dfs(grafo, v, visitado, descoberto, finalizado, tempo):
    visitado[v] = True
    tempo += 1
    descoberto[v] = tempo
    
    for u in grafo[v]:
      if not visitado[u]:
        tempo = dfs(grafo, u, visitado, descoberto, finalizado, tempo)
    
    tempo += 1
    finalizado[v] = tempo
    return tempo

def dfs_transposto(grafo, v, visitado_t, descoberto_t, finalizado_t, tempo_t):
    visitado_t[v] = True
    tempo_t += 1
    descoberto_t[v] = tempo_t
    
    print(f"({v}", end=" ")

    for u in grafo[v]:
      if not visitado_t[u]:
        tempo_t = dfs_transposto(grafo, u, visitado_t, descoberto_t, finalizado_t, tempo_t)
    
    tempo_t += 1
    finalizado_t[v] = tempo_t

    print(f"{v})", end=" ")        
    
    return tempo_t
 

# Encontrar o índice do maior tempo finalização do grafo
n, m = map(int, input().split())
grafo = cria_grafo(n, m)

visitado = [False] * n
descoberto = [0] * n
finalizado = [0] * n
tempo = 0

for v in range(n):
  if not visitado[v]:      
    tempo = dfs(grafo, v, visitado, descoberto, finalizado, tempo)

lista_ordenada_finalizados = []

for i in range(len(finalizado)):
    maior = max(finalizado)
    indice = finalizado.index(maior)
    lista_ordenada_finalizados.append(indice)
    finalizado[indice] = -1 

# Grafo Transposto
grafo_t = grafo_transposto(grafo)

visitado_t = [False] * n
descoberto_t = [0] * n
finalizado_t = [0] * n
tempo_t = 0

for v in lista_ordenada_finalizados:
  if not visitado_t[v]:      
    tempo_t = dfs_transposto(grafo_t, v, visitado_t, descoberto_t, finalizado_t, tempo_t)
 