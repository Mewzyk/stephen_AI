"""
Author: Stephen Thomas
Date Created: 23 December 2017
Basic implementation of an undirected graph
Github Link: https://github.com/Mewzyk/stephen_AI.git
"""

class Node:
    def __init__(self, key, neighbors = []):
        self.key = key
        self.neighbors = set(neighbors)

class Graph:
    def __init__(self, graph_dict = None):
        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def vertices(self):
        return list(self.graph_dict.keys())

    def add_vertex(self, vertex):
            if vertex not in self.graph_dict:
                self.graph_dict[vertex] = Node(vertex)

    def add_edge(self, edge):
        edge = set(edge)
        if len(edge) == 2:
            left = edge.pop()
            right = edge.pop()

            if left in self.graph_dict and right in self.graph_dict:
                self.graph_dict[left].neighbors.add(self.graph_dict[right])
                self.graph_dict[right].neighbors.add(self.graph_dict[left])

    def print_graph(self):
        print('Printing Vertices: ')
        print(self.graph_dict.keys(), '\n')

        print('Printing Edges: ')
        for key in self.graph_dict.keys():
            output = []
            for edge in self.graph_dict[key].neighbors:
                output.append(edge.key)
            print(key, '<-->', output)

if __name__ == "__main__":
    main_graph = Graph()
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    edges = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f'], ['f', 'g'], ['g', 'h']]

    for vertex in vertices:
        main_graph.add_vertex(vertex)

    for edge in edges:
        main_graph.add_edge(edge)

    main_graph.print_graph()