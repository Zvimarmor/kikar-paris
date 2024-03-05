import heapq

class Graph:
    def __init__(self, num_vertices):
        self.vertices = set()
        self.edges = {}

    def add_edge(self, u, v, weight):
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges.setdefault(u, []).append((v, weight))
        self.edges.setdefault(v, []).append((u, weight))
        #this two lines are simetric because the graph isn't directed

    def dijkstra(self, start, end):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0

        previous_vertices = {vertex: None for vertex in self.vertices}

        vertices = [(0, start)]

        while vertices:
            current_distance, current_vertex = heapq.heappop(vertices)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.edges.get(current_vertex, []):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(vertices, (distance, neighbor))
                    #pushes the neighbor into the "distance" heap

        path = set()
        current_vertex = end

        if current_vertex not in previous_vertices:
            return -1, []

        while current_vertex is not None:
            path.add(current_vertex)
            current_vertex = previous_vertices[current_vertex]

        return distances[end], path

#check what is the shortest path from the start to the end
# Graph 1
g1 = Graph(6)
g1.add_edge(0, 1, 5)
g1.add_edge(0, 2, 10)
g1.add_edge(1, 2, 3)
g1.add_edge(1, 3, 8)
g1.add_edge(2, 3, 1)
g1.add_edge(3, 4, 2)
print(g1.dijkstra(0, 5))  # Expected: (16, [0, 2, 3, 4, 5])

# Graph 2
g2 = Graph(8)
g2.add_edge(0, 1, 2)
g2.add_edge(0, 2, 5)
g2.add_edge(1, 2, 2)
g2.add_edge(1, 3, 1)
g2.add_edge(2, 4, 6)
g2.add_edge(3, 4, 3)
g2.add_edge(3, 5, 8)
g2.add_edge(4, 6, 7)
g2.add_edge(5, 6, 4)
g2.add_edge(5, 7, 2)
g2.add_edge(6, 7, 5)
print(g2.dijkstra(0, 7))  # Expected: (15, [0, 2, 4, 6, 7])

# Graph 3
g3 = Graph(5)
g3.add_edge(0, 1, 3)
g3.add_edge(0, 2, 2)
g3.add_edge(1, 2, 1)
g3.add_edge(1, 3, 5)
g3.add_edge(2, 3, 2)
g3.add_edge(2, 4, 4)
g3.add_edge(3, 4, 1)
print(g3.dijkstra(0, 4))  # Expected: (6, [0, 2, 4])

# Graph 4
g4 = Graph(7)
g4.add_edge(0, 1, 2)
g4.add_edge(0, 2, 4)
g4.add_edge(1, 2, 1)
g4.add_edge(1, 3, 7)
g4.add_edge(2, 4, 3)
g4.add_edge(3, 4, 1)
g4.add_edge(3, 5, 5)
g4.add_edge(4, 6, 2)
g4.add_edge(5, 6, 10)
print(g4.dijkstra(0, 6))  # Expected: (8, [0, 2, 4, 6])
