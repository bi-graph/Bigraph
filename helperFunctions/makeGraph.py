def make_graph(df):
    """

    :param df:
    :return:
    """
    nodeList = []
    G = nx.Graph()
    G.add_nodes_from(df['SNP'], bipartite=0)
    G.add_nodes_from(df['Cancer'], bipartite=1)