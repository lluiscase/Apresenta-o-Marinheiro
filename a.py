import sys
import heapq
import math
import time
import tracemalloc
from random import randint, uniform

n = 1500

class Graph:
    def __init__(self, v, e, positions):
        self.v = v
        self.e = e
        self.positions = positions

    def heuristic(self, node, goal):
        x1, y1 = self.positions[node]
        x2, y2 = self.positions[goal]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def reconstruct_path(self, parent, destination):
        path = []
        current = destination
        while current != -1:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path

    def a_star(self, src, destination):
        tracemalloc.start()
        inicio = time.perf_counter()

        g = [sys.maxsize] * self.v
        g[src] = 0
        parent = [-1] * self.v

        heap = [(self.heuristic(src, destination), 0, src)]
        visited = [False] * self.v

        while heap:
            f_atual, custo_g, u = heapq.heappop(heap)

            if visited[u]:
                continue
            visited[u] = True

            print(f"Visitando: {u}")
            print("Custos g:", g[:5])

            if u == destination:
                break

            for v in range(self.v):
                if self.e[u][v] > 0 and not visited[v]:
                    novo_g = g[u] + self.e[u][v]
                    if novo_g < g[v]:
                        g[v] = novo_g
                        parent[v] = u
                        f = novo_g + self.heuristic(v, destination)
                        heapq.heappush(heap, (f, novo_g, v))

        fim = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"\nMemória atual: {current / 1024:.2f} KB")
        print(f"Pico de memória: {peak / 1024:.2f} KB")
        print(f"Tempo: {fim - inicio:.8f} segundos")

        if g[destination] == sys.maxsize:
            print("Destino não alcançável")
            return None

        path = self.reconstruct_path(parent, destination)
        print(f"Menor custo: {g[destination]}")
        print(f"Caminho: {path}")

        return path, g[destination]


edges = [
    [randint(1, 20) if i != j else 0 for j in range(n)]
    for i in range(n)
]

positions = [(uniform(0, 100), uniform(0, 100)) for _ in range(n)]

grafo = Graph(n, edges, positions)

src = 0
destination = 14

resultado = grafo.a_star(src, destination)
print("\nResultado:", resultado)