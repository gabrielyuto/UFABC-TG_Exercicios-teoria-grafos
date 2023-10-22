import sys
from pprint import pprint

def floyd_warshall(n, grafo):
    distancias = [[float('inf')] * n for _ in range(n)]
    caminho_minimo = [[-1] * n for _ in range(n)]

    for i in range(n):
        distancias[i][i] = 0

    for u, v, peso in grafo:
        distancias[u][v] = peso
        caminho_minimo[u][v] = u

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distancias[i][j] > distancias[i][k] + distancias[k][j]:
                    distancias[i][j] = distancias[i][k] + distancias[k][j]
                    caminho_minimo[i][j] = caminho_minimo[k][j]

    return distancias, caminho_minimo

n, m = map(int, input().split())
grafo = []

for _ in range(m):
    u, v, peso = map(int, input().split())
    grafo.append((u, v, peso))

distancias, caminho_minimo = floyd_warshall(n, grafo)

pprint(distancias, width=20)
pprint(caminho_minimo, width=20)
