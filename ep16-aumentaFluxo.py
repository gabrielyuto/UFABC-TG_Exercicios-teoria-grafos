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

# def ford_fulkerson():
   

def main():
  n, m, s, t = map(int, input().split())
  grafo = [[0] * n for _ in range(n)]
  resultado = []
  matrix_fluxo = [[0] * n for _ in range(n)]
  matrix_adjacencia_residual = [[0] * n for _ in range(n)]

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

      matrix_fluxo[inicio][fim] = peso
  
  menores_valores = [vetor[2] for vetor in resultado if len(vetor) > 2]
  menor_valor = min(menores_valores)

  for index, valor in enumerate(menor_caminho):
    if (index < len(menor_caminho)-1): 
      inicio = valor
      fim = menor_caminho[index + 1]
      peso = grafo[inicio][fim]

      matrix_fluxo[inicio][fim] = menor_valor
      matrix_adjacencia_residual[inicio][fim] = grafo[inicio][fim] - menor_valor

  for index, value in enumerate(grafo):
    for posicao in value:
      if(matrix_adjacencia_residual[index][posicao] == 0): 
        matrix_adjacencia_residual[index][posicao] = grafo[index][posicao] 
    
  print(grafo)  
  print(resultado)
  print(menor_valor)
  print(matrix_fluxo)
  print(matrix_adjacencia_residual)

if __name__ == "__main__":
    main()

