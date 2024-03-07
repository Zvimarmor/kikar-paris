import time
import sys
from kikar_dijkstra import Graph

def build_graph():
    # args = ["python", "kikar_dijkstra.py", number of vertices, 
    # edges(list of pairs of 4 numbers - v, u, current time, total time), start, end]
    junction = Graph(sys.argv[2])
    
    # Parse the string representation of edges into a list
    edges_str = sys.argv[2].split( )
    edges = [(int(edges_str[i]), int(edges_str[i+1]), int(edges_str[i+2],int(edges_str[i+3]), int(edges_str[i+4]), int(edges_str[i+5])))\
               for i in range(0, len(edges_str), 6)]

    for edge in edges:
        junction.add_edge(edge[0], edge[1],edge[2])


def run_program(junction):
    for edge in junction.edges:
        if edge[2] <= 0:
            if edge[4] == 0:
                junction.change_weight(edge[0], edge[1], edge[3], edge[3], edge[4], 1)
            if edge[4] == 1:
                junction.change_weight(edge[0], edge[1], edge[4], edge[3], edge[4], 0)
            
        junction.change_weight(edge[0], edge[1], edge[2]-1, edge[3], edge[4], edge[5])

    answer = junction.dijkstra(int(sys.argv[3]), int(sys.argv[4]))
    print(answer)

build_graph()
run_program()

while True:
    run_program()

    # Sleep for one second before running the program again
    time.sleep(1)


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