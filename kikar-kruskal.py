import sys

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight 

    def dijkstra(self, start, end):
        distances = [float('inf')] * self.vertices
        distances[start] = 0
        path = [-1] * self.vertices 

        # Initialize set to keep track of visited nodes
        visited = set()

        while len(visited) < self.vertices:
            # Find the vertex with the minimum distance value
            min_distance = float('inf')
            min_vertex = -1
            for v in range(self.vertices):
                if distances[v] < min_distance and v not in visited:
                    min_distance = distances[v]
                    min_vertex = v

            # Mark the selected vertex as visited
            visited.add(min_vertex)

            if min_vertex == end:
                break

            # Update distance values of the adjacent vertices
            for v in range(self.vertices):
                if (
                    self.graph[min_vertex][v] > 0
                    and v not in visited
                    and distances[v] > distances[min_vertex] + self.graph[min_vertex][v]
                ):
                    distances[v] = distances[min_vertex] + self.graph[min_vertex][v]
                    path[v] = min_vertex  # Update the path with the previous vertex

        # Reconstruct the path
        actual_path = []
        current_vertex = end
        while current_vertex != -1:
            actual_path.insert(0, current_vertex)
            current_vertex = path[current_vertex]

        return distances[end], actual_path



