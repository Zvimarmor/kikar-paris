Kikar Paris Traffic Simulator Readme
The Kikar Paris Traffic Simulator is a Python program designed to simulate traffic flow and traffic light management in an urban environment represented by a graph structure.
The program aims to find the shortest way for padestrians from one side of given junction (by graph) to the wanted other side of the junction.
The idea for this simulator began from living next to Paris Square, or France Square, which is one of the most complex junction for padestrians in Jerusalem, and it got it name due to this reason.

How It Works
The program utilizes Dijkstra's algorithm for finding the shortest path between nodes in a graph from vertex a to b.
In the context of the Kikar Paris Traffic Simulator, Dijkstra's algorithm is employed to find the shortest route for the user (a padestrian) to travel from one point to another while considering the current traffic conditions, including the status of traffic lights- red or green.

The graph structure represents the road network of the simulated junction, where each vertex represents an intersection and each edge represents a crosswalk.
Additionally,each edge in the graph contains information about the status of the traffic light, the current time for green if the status is red, the duration of red and green light cycles, and the status of the traffic light at that crosswalk.

The simulation progresses over time, with the program updating the status of traffic lights and recalculating the shortest paths for padestrians accordingly.
padestrians travel along the shortest paths determined by Dijkstra's algorithm, navigating through crosswalk based on the current state of traffic lights.

Usage
To use the Kikar Paris Traffic Simulator, follow these steps:

Clone the project repository from GitHub.
Navigate to the project directory.
Ensure you have Python installed on your system.
Install the required dependencies by running pip install -r requirements.txt.
Run the main program kikar_time.py with the appropriate command-line arguments, including: the number of vertices, the list of edges 
(in a [vertex a,vertex b,current_time,red_light_time,green_light_time,current status- R\G]), the starting vertex,
and the destination vertex.
Observe the program's output, which includes the shortest path between the specified vertices and the time taken to traverse that path.

Purpose
The Kikar Paris Traffic Simulator serves as a tool for understanding and analyzing traffic patterns and traffic light management strategies in a controlled environment.
By simulating traffic flow and the effects of different traffic light timings, the program can help urban planners and traffic engineers optimize traffic management systems,
reduce congestion, and improve overall traffic efficiency in real-world cities.
