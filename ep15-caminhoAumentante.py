from collections import deque

def bfs(grafo, inicio, fim):
  parentes = {}
  fila = deque()
  fila.append(inicio)

  while fila:
      node = fila.popleft()
      if node == fim:
          caminho = []
          while node is not None:
              caminho.append(node)
              node = parentes.get(node)
          return list(reversed(caminho))
      
      for index, peso_vizinho in enumerate(grafo[node]):
        if (peso_vizinho > 0):
          if index not in parentes:
            parentes[index] = node
            fila.append(index)

  return None

def main():
  n, m, s, t = map(int, input().split())
  grafo = [[0] * n for _ in range(n)]
  resultado = []

  for _ in range(m):
    u, v, peso = map(int, input().split())
    grafo[u][v] = peso

  menor_caminho = bfs(grafo, s, t)

  for index, valor in enumerate(menor_caminho):
    if (index < len(menor_caminho)-1): 
      inicio = valor
      fim = menor_caminho[index + 1]
      peso = grafo[inicio][fim]

      response = [inicio, fim, peso]
      resultado.append(response)

  maiores_valores = [vetor[2] for vetor in resultado if len(vetor) > 2]
  maior_valor = min(maiores_valores)

  print(resultado)
  print(maior_valor)

if __name__ == "__main__":
    main()

