from graph_code.stephen_graph import Graph
from graph_code.stephen_dfs import dfs

if __name__ == "__main__":
    main_graph = Graph()

    vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
    edges = [['a', 'b'], ['a', 'c'], ['b', 'd'], ['d', 'h'], ['b', 'e'], ['c', 'f'], ['c', 'g'], ['e', 'i']]

    for vertex in vertices:
        main_graph.add_vertex(vertex)

    for edge in edges:
        main_graph.add_edge(edge)

    print('==================================')
    main_graph.print_graph()


    start = main_graph.graph_dict['i']
    end = main_graph.graph_dict['f']

    print('\nPrinting Path: ')
    print(dfs(start, end))
