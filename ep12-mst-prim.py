import heapq

def mst_prim(grafo, raiz):
    n = len(grafo)
    chaves = [float('inf')] * n
    pais = [-1] * n
    in_mst = [False] * n

    chaves[raiz] = 0
    min_heap = [(0, raiz)]

    while min_heap:
        peso, u = heapq.heappop(min_heap)
        in_mst[u] = True

        for v, w in grafo[u]:
            if not in_mst[v] and w < chaves[v]:
                chaves[v] = w
                pais[v] = u
                heapq.heappush(min_heap, (w, v))

    return chaves, pais

def main():
    n, m, r = map(int, input().split())
    grafo = [[] for _ in range(n)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        grafo[u].append((v, w))
        grafo[v].append((u, w))

    chaves, pais = mst_prim(grafo, r)

    print(chaves)
    print(pais)


if __name__ == "__main__":
    main()
