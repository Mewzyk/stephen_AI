"""
Queue Implementation of BFS
Designed to work with the graph implemntation in stephen_graph.py
@Date: 30 December 2017
@Author: Breanna Baltaxe
"""

"""
Params ->
@start_node: node to start BFS on
@dest_node: node attempting to find a path to

Output ->
List containing visited nodes
"""
def bfs(start_node, dest_node):

    # visited: set of visited nodes
    # path: nodes encountered in order
    # queue: queue to hold ordering neighbors
    visited = set()
    path = []
    queue = []
    visited.add(start_node)
    path.append(start_node.key)

    for neighbor in start_node.neighbors:
        queue.append(neighbor)

    while queue:
        cur_node = queue.pop(0)
        visited.add(cur_node)
        path.append(cur_node.key)
        if cur_node is dest_node:
            return path

        for neighbor in cur_node.neighbors:
            if neighbor not in visited:
                queue.append(neighbor)

