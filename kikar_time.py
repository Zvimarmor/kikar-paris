import time
import sys
from kikar_dijkstra import Graph

def build_graph():
    # args = ["python", "kikar_dijkstra.py", number of vertices, 
    # edges(list of pairs of 4 numbers - v, u, current time, total time), start, end]
    junction = Graph(sys.argv[2])
    
    # Parse the string representation of edges into a list
    edges_str = sys.argv[2].split( )
    edges = [(int(edges_str[i]), int(edges_str[i+1]), int(edges_str[i+2])) for i in range(0, len(edges_str), 4)]

    for edge in edges:
        junction.add_edge(edge[0], edge[1],edge[2])


def run_program(junction):
    for edge in junction.edges:
        junction.change_weight(edge[0], edge[1], edge[2]-1)

    answer = junction.dijkstra(int(sys.argv[3]), int(sys.argv[4]))
    print(answer)
    
run_program()
    

while True:
    run_program()

    # Sleep for one second before running the program again
    time.sleep(1)