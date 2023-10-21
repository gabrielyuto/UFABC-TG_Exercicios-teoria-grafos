
n, m = map(int, input().split()) 
lista_adjacencia = [[] for _ in range(n)]

for _ in range(m):
    inicio, fim, peso = map(int, input().split())
    lista_adjacencia[inicio].append((fim, peso))

for i in range(n):
    print(f"{i}: ", end="")
    for vizinho, peso in lista_adjacencia[i]:
        print(f"{vizinho}({peso})", end=" ")
    print()
