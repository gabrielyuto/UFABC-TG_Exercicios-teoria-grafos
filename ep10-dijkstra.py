import heapq

def dijkstra(grafo, inicio):
  n = len(grafo)
  distancia = [float('inf')] * n
  distancia[inicio] = 0
  caminho = [-1] * n
  fila = [(0, inicio)]

  while fila:
    dist, u = heapq.heappop(fila)

    if dist > distancia[u]:
      continue

    for v, peso in grafo[u]:
      if distancia[u] + peso < distancia[v]:
        distancia[v] = distancia[u] + peso
        caminho[v] = u
        heapq.heappush(fila, (distancia[v], v))

  return distancia, caminho

n, m, s = map(int, input().split())
grafo = [[] for _ in range(n)]

for _ in range(m):
  u, v, peso = map(int, input().split())
  grafo[u].append((v, peso))

distancias, caminho = dijkstra(grafo, s)

print(distancias)
print(caminho)



