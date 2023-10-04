from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited)

g = Graph()

edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (3, 8), (4, 9), (4, 10), (5, 11), (5, 12), 
         (6, 3), (6, 4), (6, 13), (6, 14), (7, 8), (7, 9), (8, 9)]

for edge in edges:
    g.add_edge(edge[0], edge[1])

print("Depth-First Traversal (starting from vertex 0):")
visited = [False] * 15
g.dfs(0, visited)
