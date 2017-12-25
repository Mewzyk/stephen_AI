from stephen_graph import Graph
from stephen_dfs import dfs

if __name__ == "__main__":
    main_graph = Graph()
    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    edges = [['a', 'b'], ['b', 'c'], ['c', 'd'], ['d', 'e'], ['e', 'f'], ['f', 'g'], ['g', 'h']]
    for vertex in vertices:
        main_graph.add_vertex(vertex)

    for edge in edges:
        main_graph.add_edge(edge)

    main_graph.print_graph()

    start = main_graph.graph_dict['e']
    end = main_graph.graph_dict['h']

    print('Printing Path: ')
    print(dfs(start, end))
