import networkx as nx


def make_graph(dataframe):
    """
    Make a graph based on the input dataframe
    :param dataframe: Bipartite graph dataframe
    :return: Generated networkx graph
    """
    nodeList = []
    G = nx.Graph()
    G.add_nodes_from(dataframe['SNP'], bipartite=0)
    G.add_nodes_from(dataframe['Cancer'], bipartite=1)
    for i in dataframe.iterrows():
        nodeList.append(i[1][0])
        nodeList.append(i[1][1])

    G.add_edges_from(add_to_list(dataframe))
    isolates = nx.isolates(G)
    # G.remove_nodes_from(isolates)
    print('Graph made successfully', "\n")
    return G
