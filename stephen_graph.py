"""
Author: Stephen Thomas
Date Created: 23 December 2017
Basic implementation of an undirected graph
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