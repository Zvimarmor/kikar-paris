import time
import subprocess
import sys
from kikar_dijkstra import Graph


def run_program():
    # args = ["python", "kikar_dijkstra.py", number of vertices, edges, start, end]
    junction = Graph(sys.argv[2])
    
    # Parse the string representation of edges into a list
    edges_str = sys.argv[2].split( )
    edges = [(int(edges_str[i]), int(edges_str[i+1]), int(edges_str[i+2])) for i in range(0, len(edges_str), 3)]

    for edge in edges:
        junction.add_edge(*edge)

    print(junction.dijkstra(int(sys.argv[3]), int(sys.argv[4])))

run_program()
    

while True:
    run_program()

    # Sleep for one second before running the program again
    time.sleep(1)
