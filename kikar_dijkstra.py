import heapq

GREEN = 1
RED = 0

class Graph:
    def __init__(self, num_vertices):
        self.vertices = set()
        self.edges = {}

    def add_edge(self, u, v, current_time, red_light_time, green_light_time, status): #status is -1 for red and <=0 for green
        self.vertices.add(u)
        self.vertices.add(v)
        self.edges.setdefault(u, []).append((v, current_time, red_light_time, green_light_time, status))
        self.edges.setdefault(v, []).append((u, current_time, red_light_time, green_light_time, status))
        #this two lines are simetric because the graph isn't directed

    def change_weight(self, u, v, current_time, red_light_time, green_light_time ,status):
        for i, (neighbor, w, red_light_time, green_light_time, status) in enumerate(self.edges[u]):
            if neighbor == v:
                self.edges[u][i] = (neighbor, current_time, red_light_time, green_light_time, status)
                break
        for i, (neighbor, w, red_light_time, green_light_time, status) in enumerate(self.edges[v]):
            if neighbor == u:
                self.edges[v][i] = (neighbor, current_time, red_light_time, green_light_time, status)
                break

    def dijkstra(self, start, end):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        distances[start] = 0

        previous_vertices = {vertex: None for vertex in self.vertices}

        vertices = [(0, start)]

        while vertices:
            current_distance, current_vertex = heapq.heappop(vertices)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, current_time, red_light_time, green_light_time, status in self.edges[current_vertex]:
                distance = current_distance + current_time

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_vertices[neighbor] = current_vertex
                    heapq.heappush(vertices, (distance, neighbor))
                    #pushes the neighbor into the "distance" heap

        path = []
        current_vertex = end

        if current_vertex not in previous_vertices:
            return -1, []

        while current_vertex is not None:
            path.insert(0, current_vertex)
            current_vertex = previous_vertices[current_vertex]

        return distances[end], path

# # Test cases
# # 1. The graph is a line
# line = Graph(3)
# line.add_edge(0, 1, 10, 10, 10, 0)
# line.add_edge(1, 2, 10, 10, 10, 1)
# print(line.dijkstra(0, 2))  # Expected: (20, [0, 1, 2])

# # 2. The graph is a tree
# tree = Graph(5)
# tree.add_edge(0, 1, 10, 10, 10, 0)
# tree.add_edge(0, 2, 10, 10, 10, 1)
# tree.add_edge(1, 3, 10, 10, 10, 0)
# tree.add_edge(1, 4, 10, 10, 10, 1)
# print(tree.dijkstra(0, 4))  # Expected: (20, [0, 1, 4])

# # 3. The graph is a star
# star = Graph(5)
# star.add_edge(0, 1, 10, 10, 10, "red")
# star.add_edge(0, 2, 10, 10, 10, "green")
# star.add_edge(0, 3, 10, 10, 10, "red")
# star.add_edge(0, 4, 10, 10, 10, "green")
# print(star.dijkstra(0, 4))  # Expected: (10, [0, 4])

# # 4. The graph is a square
# square = Graph(4)
# square.add_edge(0, 1, 10, 10, 10, "red")
# square.add_edge(1, 2, 10, 10, 10, "green")
# square.add_edge(2, 3, 10, 10, 10, "red")
# square.add_edge(3, 0, 10, 10, 10, "green")
# print(square.dijkstra(0, 2))  # Expected: (20, [0, 1, 2])
    
# # Test cases
# # 5. The graph is a complex graph with a cycle and 20 vertices
# complex_graph = Graph(20)
# complex_graph.add_edge(0, 1, 10, 10, 10, RED)
# complex_graph.add_edge(1, 2, 10, 10, 10, "green")
# complex_graph.add_edge(2, 3, 10, 10, 10, "red")
# complex_graph.add_edge(3, 4, 10, 10, 10, "green")
# complex_graph.add_edge(4, 5, 10, 10, 10, "red")
# complex_graph.add_edge(5, 6, 10, 10, 10, "green")
# complex_graph.add_edge(6, 7, 10, 10, 10, "red")
# complex_graph.add_edge(7, 8, 10, 10, 10, "green")
# complex_graph.add_edge(8, 9, 10, 10, 10, "red")
# complex_graph.add_edge(9, 10, 10, 10, 10, "green")
# complex_graph.add_edge(10, 11, 10, 10, 10, "red")
# complex_graph.add_edge(11, 12, 10, 10, 10, "green")
# complex_graph.add_edge(12, 13, 10, 10, 10, "red")
# complex_graph.add_edge(13, 14, 10, 10, 10, "green")
# complex_graph.add_edge(14, 15, 10, 10, 10, "red")
# complex_graph.add_edge(15, 16, 10, 10, 10, "green")
# complex_graph.add_edge(16, 17, 10, 10, 10, "red")
# complex_graph.add_edge(17, 18, 10, 10, 10, "green")
# complex_graph.add_edge(18, 19, 10, 10, 10, "red")
# complex_graph.add_edge(19, 0, 10, 10, 10, "green")
# print(complex_graph.dijkstra(0, 19))  # Expected: (10, [0, 1])

# #real nubers of kikar paris
# kikar_paris = Graph(6)
# kikar_paris.add_edge(0, 1, 40, 40, 60, RED)
# kikar_paris.add_edge(1, 2, 17, 107, 13, GREEN)
# kikar_paris.add_edge(0, 3, 14, 108, 10, GREEN)
# kikar_paris.add_edge(2, 4, 19, 38, 81, RED)
# kikar_paris.add_edge(3, 5, 12, 96, 22, GREEN)
# kikar_paris.add_edge(4, 6, 14, 76, 4, RED)
# kikar_paris.add_edge(5, 6, 0, 82, 38, GREEN)
# print(kikar_paris.dijkstra(0, 5))  # Expected: (33, [2, 4, 5, 3])
