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
def dfs(start_node, dest_node, visited=None, path=None):
    if visited is None:
        visited = set()
        path = []

    visited.add(start_node)
    path.append(start_node.key)

    if start_node is dest_node: return path

    for neighbor in start_node.neighbors:
        if neighbor not in visited:
            dfs(neighbor, dest_node, visited, path)

        if dest_node.key in path: return path
