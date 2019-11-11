import networkx as nx


def make_graph(df):
    """

    :param df:
    :return:
    """
    nodeList = []
    G = nx.Graph()
    G.add_nodes_from(df['SNP'], bipartite=0)
    G.add_nodes_from(df['Cancer'], bipartite=1)
    for i in df.iterrows():
        nodeList.append(i[1][0])
        nodeList.append(i[1][1])

    G.add_edges_from(add_to_list(df))
    isolates = nx.isolates(G)
    # G.remove_nodes_from(isolates)
    print('Graph made successfully', "\n")
    return G
