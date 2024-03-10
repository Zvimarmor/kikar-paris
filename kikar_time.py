import time
import sys
from kikar_dijkstra import Graph

def build_graph():
    # args = ["python", "kikar_dijkstra.py", number of vertices, 
    # edges(list of pairs of 4 numbers - v, u, current time, total time), start, end]
    junction = Graph(sys.argv[1])
    edges_str = sys.argv[2].split(" ")
    
    # Ensure that the length of the edges_str is a multiple of 6
    if len(edges_str) % 6 != 0:
        print("Invalid number of arguments in edges list.")
        sys.exit(1)

    # Convert string values to integers and add edges to the graph
    for i in range(0, len(edges_str), 6):
        u, v, current_time, red_light_time, green_light_time, status = map(int, edges_str[i:i+6])
        junction.add_edge(u, v, current_time, red_light_time, green_light_time, status)

    return junction


def run_program(junction):
    for vertex, edges in junction.edges.items():
        for i, (neighbor, current_time, red_light_time, green_light_time, status) in enumerate(edges):
            if status > 0:  # if the status is green
                junction.change_weight(vertex, neighbor, 0, red_light_time, green_light_time, status - 1)
            elif status == 0:  # if the status is the end of the green light
                junction.change_weight(vertex, neighbor, red_light_time, red_light_time, green_light_time, -1)
            elif status < 0 and current_time <= 0:  # if the status is red and the time is over
                junction.change_weight(vertex, neighbor, 0, red_light_time, green_light_time, green_light_time)
            elif status < 0 and current_time > 0:  # if the status is red and the time is not over
                junction.change_weight(vertex, neighbor, current_time - 1, red_light_time, green_light_time, -1)

    answer = junction.dijkstra(int(sys.argv[3]), int(sys.argv[4]))
    print(answer)

junction = build_graph()
run_program(junction)

while True:
    run_program(junction)

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