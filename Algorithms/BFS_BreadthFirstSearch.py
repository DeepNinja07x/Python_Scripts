from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex, neighbor):
        if vertex in self.graph:
            self.graph[vertex].append(neighbor)
        else:
            self.graph[vertex] = [neighbor]

    def bfs(self, start):
        visited = set()
        queue = deque()
        
        queue.append(start)
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 2)
    graph.add_edge(2, 0)
    graph.add_edge(2, 3)
    graph.add_edge(3, 3)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 7)
    graph.add_edge(7, 4)
    graph.add_edge(8, 9)
    graph.add_edge(9, 10)
    graph.add_edge(10, 11)
    graph.add_edge(11, 8)
    graph.add_edge(12, 13)
    graph.add_edge(13, 14)
    graph.add_edge(14, 15)
    graph.add_edge(15, 12)
    graph.add_edge(16, 17)
    graph.add_edge(17, 18)
    graph.add_edge(18, 19)
    graph.add_edge(19, 16)

    print("Breadth-First Traversal (starting from vertex 2):")
    graph.bfs(2)
    print("\n")

    print("Breadth-First Traversal (starting from vertex 9):")
    graph.bfs(9)
