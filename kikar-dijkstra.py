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

        while current_vertex is not None:
            path.add(current_vertex)
            current_vertex = previous_vertices[current_vertex]

        return distances[end], path


