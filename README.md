# Kikar Paris Traffic Simulator

## Description
The Kikar Paris Traffic Simulator is a Python program designed to simulate pedestrian traffic flow and traffic light management in an urban environment represented by a graph structure. The program aims to find the shortest path for pedestrians to navigate from one side of a given junction to the other side, considering the current traffic conditions, including the status of traffic lights.

The idea for this simulator originated from living near Paris Square, also known as France Square, which is one of the most complex junctions for pedestrians in Jerusalem.

## How It Works
The program utilizes Dijkstra's algorithm to find the shortest path between nodes in a graph from vertex A to vertex B. In the context of the Kikar Paris Traffic Simulator, Dijkstra's algorithm is employed to find the shortest route for pedestrians to travel while considering the current traffic conditions and the status of traffic lights.

The graph structure represents the road network of the simulated junction, where each vertex represents an intersection, and each edge represents a crosswalk. Each edge in the graph contains information about the status of the traffic light, the current time, the duration of red and green light cycles, and the status of the traffic light at that crosswalk.

The simulation progresses over time, with the program updating the status of traffic lights and recalculating the shortest paths for pedestrians accordingly. Pedestrians travel along the shortest paths determined by Dijkstra's algorithm, navigating through crosswalks based on the current state of traffic lights.

## Usage
To use the Kikar Paris Traffic Simulator, follow these steps:

1. Clone the project repository from GitHub.
2. Navigate to the project directory.
3. Ensure you have Python installed on your system.
4. Install the required dependencies by running `pip install -r requirements.txt`.
5. Run the main program `kikar_time.py` with the appropriate command-line arguments, including the number of vertices, the list of edges (in the format `[vertex A, vertex B, current time, red light time, green light time, current status - R/G]`), the starting vertex, and the destination vertex.
6. Observe the program's output, which includes the shortest path between the specified vertices and the time taken to traverse that path.

## Purpose
The Kikar Paris Traffic Simulator serves as a tool for understanding and analyzing traffic patterns and traffic light management strategies in a controlled environment. By simulating traffic flow and the effects of different traffic light timings, the program can help urban planners and traffic engineers optimize traffic management systems, reduce congestion, and improve overall traffic efficiency in real-world cities.
