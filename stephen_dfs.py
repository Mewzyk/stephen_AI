"""
Stack Implmentation of DFS
Designed to work with the graph implemntation in stephen_graph.py
@Date: 23 December 2017
@Author: Stephen Thomas
"""

"""
Params ->
@start_node: node to start DFS on
@dest_node: node attempting to find a path to

Output ->
List containing visited nodes
"""
def depth_first_search(start_node, dest_node, graph):
    visited = []
    stack = [start_node]

    curr_node = stack.pop(0)
    visited.append(curr_node)
    while curr_node is not None:
        for vertex in graph.__graph_dict[curr_node]:
            if vertex not in visited:
                stack.insert(0, vertex)

        if curr_node is dest_node:
            break
        else:
            curr_node = stack.pop(0)
            visited.append(curr_node)

    return visited