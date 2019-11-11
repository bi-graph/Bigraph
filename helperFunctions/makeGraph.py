import networkx as nx


def make_graph(
        dataframe: dict,
        left_bipartite: str = "SNP",
        right_bipartite: str = "Cancer"):
    """
    Make a graph based on the input dataframe
    :param left_bipartite: Left part of the graph
    :param right_bipartite: Right part of the graph
    :param dataframe: Bipartite graph dataframe
    :return: Generated networkx graph
    """
    node_list = []
    graph = nx.Graph()
    graph.add_nodes_from(dataframe[left_bipartite], bipartite=0)
    graph.add_nodes_from(dataframe[right_bipartite], bipartite=1)
    for node in dataframe.iterrows():
        node_list.append(node[1][0])
        node_list.append(node[1][1])

    graph.add_edges_from(add_to_list(dataframe))
    isolates = nx.isolates(graph)
    # graph.remove_nodes_from(isolates)
    print('Graph made successfully', "\n")
    return graph
