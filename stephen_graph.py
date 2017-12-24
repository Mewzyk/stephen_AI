"""
Author: Stephen Thomas
Date Created: 23 December 2017
Basic implementation of an undirected graph
Github Link: https://github.com/Mewzyk/stephen_AI.git
"""

class Graph:
    def __init__(self, graph_dict = None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def add_vertex(self, vertex):
            if vertex not in self.__graph_dict:
                self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        if len(edge) == 2:
            left = edge.pop()
            right = edge.pop()

            if left in self.__graph_dict and right in self.__graph_dict:
                self.__graph_dict[left].append(right)
                self.__graph_dict[right].append(left)

    def print_graph(self):
        print('Printing Vertices:')
        print(self.__graph_dict.keys())
        print('Printing Edges:')
        for vertex in self.__graph_dict.keys():
            print(vertex, '<---->', self.__graph_dict[vertex])

if __name__ == "__main__":
    main_graph = Graph()
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    edges = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f'], ['f', 'g'], ['g', 'h']]

    for vertex in vertices:
        main_graph.add_vertex(vertex)

    for edge in edges:
        main_graph.add_edge(edge)

    main_graph.print_graph()