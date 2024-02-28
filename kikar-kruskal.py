#write me the kruskal algorithm and add description

#Kruskal's algorithm is a minimum-spanning-tree 
#algorithm which finds an edge of the least possible 
#weight that connects any two trees in the forest. 
#It is a greedy algorithm in graph theory as it finds a minimum spanning 
#tree for a connected weighted graph adding increasing cost arcs at each step.
# This means it finds a subset of the edges that forms a tree that includes every vertex,
# where the total weight of all the edges in the tree is minimized. If the graph is not connected,
# then it finds a minimum spanning forest (a minimum spanning tree for each connected component).

#The algorithm operates by sorting all the edges in non-decreasing order of their weight.
# Then, it iterates through the sorted edges and adds the edge to the minimum spanning tree 
#if it doesn't form a cycle with the edges that are already in the minimum spanning tree. 
#The algorithm uses a disjoint-set data structure to determine whether adding an edge forms a cycle.


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        #print("Edges in the constructed MST:")
        #for u, v, weight in result:
        #    print("%d -- %d == %d" % (u, v, weight))

        return result

    def v_to_v_quick(self, v1, v2):
        MST = self.kruskal()
        answer = 0
        shortest_way = []

        for e in MST:
            if v1 == e[0] and v2 == e[1]:
                answer += e[2]
                shortest_way.append(e)
                v1 = e[1]

            elif v1 == e[0] and v2 != e[1]:
                self.v_to_v_quick(v1 = e[1], v2= v2)

        print("Edges in the constructed MST:")
        for e in shortest_way:
            print("%d to %d (%d minutes)" % (e[0], e[1], e[2]))
        print("the way will take %d minutes" % answer)


        


        

        


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)
g.kruskal()
g.v_to_v_quick(0, 1)
# Output:
# Edges in the constructed MST:
# 2 -- 3 == 4
# 0 -- 3 == 5
# 0 -- 1 == 10
# Time complexity: O(E log E) or O(E log V)
# Space complexity: O(E + V)
