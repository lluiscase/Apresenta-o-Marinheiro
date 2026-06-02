from math import inf
from random import randint
import time
import tracemalloc

class AdjancencyMatrix:
    def __init__(self, n):
        self.weight = [[inf for _ in range(n)] for _ in range(n)]

        for i in range(n):
            self.weight[i][i] = 0

        self.vertices = n

    def set_edge(self, i, j, w):
        self.weight[i][j] = w


def floyd_warshall(adj):
    dist = [row[:] for row in adj.weight]

    for k in range(adj.vertices):
        for i in range(adj.vertices):
            for j in range(adj.vertices):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

n = 500

adj = AdjancencyMatrix(n)

for i in range(n):
    for j in range(n):
        if i != j:
            adj.set_edge(i, j, randint(1, 20))

tracemalloc.start()

inicio = time.perf_counter()

distancias = floyd_warshall(adj)

fim = time.perf_counter()

current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Tempo de execução: {fim - inicio:.8f} segundos")

print("\nPrimeiras 5 linhas da matriz de menores distâncias:\n")
print(f"Memória atual: {current / 1024:.2f} KB")
print(f"Pico de memória: {peak / 1024:.2f} KB")
for linha in distancias[:5]:
    print(linha[:5])