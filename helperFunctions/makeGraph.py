import networkx as nx


def make_graph(dataframe):
    """
    Make a graph based on the input dataframe
    :param dataframe: Bipartite graph dataframe
    :return: Generated networkx graph
    """
    nodeList = []
    graph = nx.Graph()
    graph.add_nodes_from(dataframe['SNP'], bipartite=0)
    graph.add_nodes_from(dataframe['Cancer'], bipartite=1)
    for node in dataframe.iterrows():
        nodeList.append(node[1][0])
        nodeList.append(node[1][1])

    graph.add_edges_from(add_to_list(dataframe))
    isolates = nx.isolates(graph)
    # graph.remove_nodes_from(isolates)
    print('Graph made successfully', "\n")
    return graph
