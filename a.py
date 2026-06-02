import sys
import time
import tracemalloc
from random import randint

n = 1500

class Graph:
    def __init__(self, v, e):
        self.v = v
        self.e = e

    def heuristic(self, node, goal):
        # Heurística simples
        return abs(goal - node)

    def minDistance(self, g, visited, goal):
        minimum = sys.maxsize
        minIndex = -1

        for v in range(self.v):
            if not visited[v]:
                f = g[v] + self.heuristic(v, goal)

                if f < minimum:
                    minimum = f
                    minIndex = v

        return minIndex

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

        visited = [False] * self.v
        parent = [-1] * self.v

        while True:
            u = self.minDistance(g, visited, destination)

            if u == -1:
                break

            print(f"Visitando: {u}")
            print("Custos g:", g[:5])

            if u == destination:
                break

            visited[u] = True

            for v in range(self.v):
                if self.e[u][v] > 0 and not visited[v]:

                    new_cost = g[u] + self.e[u][v]

                    if new_cost < g[v]:
                        g[v] = new_cost
                        parent[v] = u

        fim = time.perf_counter()

        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print(f"\nMemória atual: {current} bytes")
        print(f"Pico de memória: {peak} bytes")
        print(f"Tempo: {fim - inicio:.8f} segundos")

        if g[destination] == sys.maxsize:
            print("Destino não alcançável")
            return None

        path = self.reconstruct_path(parent, destination)

        print(f"\nMenor custo: {g[destination]}")
        print(f"Caminho: {path}")

        return path, g[destination]


edges = [
    [randint(1, 20) if i != j else 0 for j in range(n)]
    for i in range(n)
]

grafo = Graph(n, edges)

src = 0
destination = 14

resultado = grafo.a_star(src, destination)

print("\nResultado:", resultado)