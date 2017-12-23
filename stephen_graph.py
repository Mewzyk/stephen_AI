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
        if (edge.size() == 2):
            left = edge.pop()
            right = edge.pop()

            if left in self.__graph_dict and right in self.__graph_dict:
                self.__graph_dict[left].append(right)
                self.__graph_dict[right].append(left)

if __name__ == "__main__":
    print("hello world!")