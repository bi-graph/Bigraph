import json
from datetime import datetime

import networkx as nx

# import snap
# from scipy.stats import mode
# from sklearn.cross_validation import KFold
from helperFunctions.importFiles import import_files
from helperFunctions.makeGraph import make_graph


def complement_graph(G):
    return nx.complement(G)


def main():
    """
    Link prediction on a bipartite network
    :return:
    """
    start_time = datetime.now()

    print('Running...', "\n")
    df, df_nodes = import_files()
    G = make_graph(df, df_nodes)
    graphEdges = G.edges
    print(G.__dict__)
    print(nx.nodes(G))

    nx.write_gexf(G, './outputs/graph.gexf')
    nodes = [{'left': str(i), 'right': str(G.node[i]['bipartite'])}
             for i in G.nodes()]
    links = [{'source': int(u[0]), 'target': int(u[1])}
             for u in G.edges()]
    open('./outputs/graph2.json', 'w')
    with open('./outputs/graph2.json', 'w') as f:
        json.dump({'nodes': nodes, 'links': links},
                  f, indent=4)
    clustering_coefficient = nx.algorithms.bipartite.average_clustering(G)
    print("\nclustering coefficient: ", clustering_coefficient)


if __name__ == '__main__':
    main()
