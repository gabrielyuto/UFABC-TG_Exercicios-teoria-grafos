import heapq

def prim(grafo, root):
    n = len(grafo)
    chaves = [float('inf')] * n
    parent = [-1] * n
    in_mst = [False] * n

    chaves[root] = 0
    min_heap = [(0, root)]

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        in_mst[u] = True

        for v, w in grafo[u]:
            if not in_mst[v] and w < chaves[v]:
                chaves[v] = w
                parent[v] = u
                heapq.heappush(min_heap, (w, v))

    return chaves, parent

n, m, r = map(int, input().split())
grafo = [[] for _ in range(n)]

for _ in range(m):
    u, v, w = map(int, input().split())
    grafo[u].append((v, w))
    grafo[v].append((u, w))

keys, parent = prim(grafo, r)

print(keys)
print(parent)
