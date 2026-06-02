import sys
import heapq
import time
import tracemalloc
from random import randint

n = 1500

class Graph:
    def __init__(self, v, e):
        self.v = v
        self.e = e

    def dijkstra(self, src):
        tracemalloc.start()
        inicio = time.perf_counter()

        dist = [sys.maxsize] * self.v
        dist[src] = 0

        heap = [(0, src)]

        while heap:
            custo_atual, u = heapq.heappop(heap)

            if custo_atual > dist[u]:
                continue

            print(f"Visitando: {u}")
            print("Distâncias:", dist[:5])

            for v in range(self.v):
                if self.e[u][v] > 0:
                    novo_custo = dist[u] + self.e[u][v]
                    if novo_custo < dist[v]:
                        dist[v] = novo_custo
                        heapq.heappush(heap, (novo_custo, v))

        fim = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"\nMemória atual: {current / 1024:.2f} KB")
        print(f"Pico de memória: {peak / 1024:.2f} KB")
        print(f"Tempo: {fim - inicio:.8f} segundos")

        return dist


edges = [
    [randint(1, 20) if i != j else 0 for j in range(n)]
    for i in range(n)
]

grafo = Graph(n, edges)

src = 0
distancias = grafo.dijkstra(src)
print("\nPrimeiras 5 distâncias a partir do nó 0:", distancias[:5])