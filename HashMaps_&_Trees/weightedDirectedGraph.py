from collection import WeightedGraph
from hash_map import HashMap
import sys

class weightedDirectedGraph(WeightedGraph):

    def __init__(self):
        # So the data structure used here is dictionary, because when I wrote my map the hash
        # function was ment to be used with integers, and now when I try to use it here
        # amen inch gmpuma
        # I just know that we needed to write self._graph = HashMap() and change all the
        # append and pop functions to put and get functions

        self._graph = {}

    def __str__(self):
        my_list = []
        for v in self._graph:
            my_list.append(f"{v} -> {self._graph[v]}")
        return "\n".join(my_list)

    def shortest_path_using_djikstra(self):
        costs, parents = self.djikstra("1")
        print(costs)

    def print(self) -> None:
        print(self._graph)

    def is_empty(self) -> bool:
        return len(self._graph) == 0

    def empty(self) -> None:
        self._graph = {}

    def size(self):
        return len(self._graph)

    def __len__(self):
        return len(self._graph)


    def add_vertex(self, vertex: object) -> bool:
        if vertex in self._graph:
            return False
        self._graph[vertex] = {}
        return True

    def remove_vertex(self, vertex: object)-> bool:
        if vertex not in self._graph:
            return False
        # get_neighbors
        neighbors = self._graph[vertex]
        # remove from the graph
        self._graph.pop(vertex)
        # remove connection
        for n in neighbors:
            self._graph[n].pop(vertex)

    def add_edge(self, vertex1: object, vertex2: object, weight:int) -> bool:
        if vertex1 not in self._graph or vertex2 not in self._graph:
            return False
        if vertex2 in self._graph[vertex1] or vertex1 in self._graph[vertex2]:
            return False
        self._graph[vertex1][vertex2] = weight
        self._graph[vertex2][vertex1] = weight
        return True

    def remove_edge(self, vertex1: object, vertex2: object) -> bool:
        if vertex1 not in self._graph or vertex2 not in self._graph:
            return False
        if vertex2 not in self._graph[vertex1] or vertex1 not in self._graph[vertex2]:
            return False
        self._graph[vertex1].pop(vertex2)
        self._graph[vertex2].pop(vertex1)
        return True

    def djikstra(self, start: object):
        if start not in self._graph:
            return None

        costs = {v: sys.maxsize for v in self._graph}
        costs[start] = 0
        parents = {v: None for v in self._graph}
        visited = []

        while len(visited) < len(self._graph):
            min_node = None
            min_cost_value = sys.maxsize
            for v in self._graph:
                if v not in visited and costs[v] < min_cost_value:
                    min_node = v
                    min_cost_value = costs[v]

            for n in self._graph[min_node]:
                if n not in visited and costs[min_node] + self._graph[min_node][n] < costs[n]:
                    costs[n] = costs[min_node] + self._graph[min_node][n]
                    parents[n] = min_node

            visited.append(min_node)

        return costs, parents




print("____________________________")
print("Testing weightedDirectedGraph")
print("____________________________")

american_univeristy = weightedDirectedGraph()
american_univeristy.add_vertex("1")
american_univeristy.add_vertex("2")
american_univeristy.add_vertex("3")

american_univeristy.add_edge("1", "2", 1)
american_univeristy.add_edge("1", "3", 2)
american_univeristy.add_edge("2", "3", 3)

print(american_univeristy)

print("____________________________")
print("____________________________")
print("____________________________")
print("Shortest path using djikstra")

american_univeristy.shortest_path_using_djikstra()