Kikar Paris Traffic Simulator Readme
The Kikar Paris Traffic Simulator is a Python program designed to simulate traffic flow and traffic light management in an urban environment represented by a graph structure.
The program aims to model a fictional cityscape, where traffic lights at various intersections govern the movement of vehicles along roads.

How It Works
The program utilizes Dijkstra's algorithm for pathfinding, which is a widely-used algorithm for finding the shortest path between nodes in a graph.
In the context of the Kikar Paris Traffic Simulator, Dijkstra's algorithm is employed to find the shortest route for vehicles to travel from one point to another
while considering the current traffic conditions, including the status of traffic lights.

The graph structure represents the road network of the simulated city, where each vertex represents an intersection and each edge represents a road connecting two intersections. Additionally,
each edge in the graph contains information about the current time, the duration of red and green light cycles, and the status of the traffic light at that intersection.

The simulation progresses over time, with the program updating the status of traffic lights and recalculating the shortest paths for vehicles accordingly.
Vehicles travel along the shortest paths determined by Dijkstra's algorithm, navigating through intersections based on the current state of traffic lights.

Usage
To use the Kikar Paris Traffic Simulator, follow these steps:

Clone the project repository from GitHub.
Navigate to the project directory.
Ensure you have Python installed on your system.
Install the required dependencies by running pip install -r requirements.txt.
Run the main program kikar_time.py with the appropriate command-line arguments, including the number of vertices, the list of edges, the starting vertex,
and the destination vertex.
Observe the program's output, which includes the shortest path between the specified vertices and the time taken to traverse that path.
Purpose
The Kikar Paris Traffic Simulator serves as a tool for understanding and analyzing traffic patterns and traffic light management strategies in a controlled environment.
By simulating traffic flow and the effects of different traffic light timings, the program can help urban planners and traffic engineers optimize traffic management systems,
reduce congestion, and improve overall traffic efficiency in real-world cities.
