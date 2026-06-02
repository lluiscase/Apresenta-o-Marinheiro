import sys
import time
import tracemalloc
from random import randint

n = 1500
class Graph:
    def __init__(self, v, e):
        self.v = v
        self.e = e

    def minDistance(self, dist, shortestPath):
        minimum = sys.maxsize
        minIndex = -1

        for v in range(self.v):
            if not shortestPath[v] and dist[v] < minimum:
                minimum = dist[v]
                minIndex = v

        return minIndex

    def dijkstra(self, src):
        tracemalloc.start()
        inicio = time.perf_counter()
        dist = [sys.maxsize] * self.v
        dist[src] = 0
        shortestPath = [False] * self.v

        for _ in range(self.v):
            u = self.minDistance(dist, shortestPath)

            if u == -1:
                break

            shortestPath[u] = True
            print(f"Visitando: {u}")
            print("Distâncias:", dist[:5])

            for v in range(self.v):
                if (
                    self.e[u][v] > 0
                    and not shortestPath[v]
                    and dist[v] > dist[u] + self.e[u][v]
                ):
                    dist[v] = dist[u] + self.e[u][v]
        fim = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Current memory usage: {current} KB")
        print(f"Peak memory usage: {peak} KB")
        print(f"Tempo: {fim - inicio:.8f} segundos")
        return dist
edges = [
    [randint(1,20) if i != j else 0 for j in range(n)]
    for i in range(n)
]
grafo = Graph(n,edges)

src = 0
print(grafo.dijkstra(src))