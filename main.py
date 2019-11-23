from datetime import datetime

import networkx as nx
from tabulate import tabulate

# import snap
# from scipy.stats import mode
# from sklearn.cross_validation import KFold
from helperFunctions.importFiles import import_files
from helperFunctions.makeGraph import make_graph
from bigraph import bigraph as pr


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
    G = make_graph(df)
    graphEdges = G.edges
    print(G.__dict__)
    # print(set(n for n,d in G.nodes(data=True)))# if d['bipartite']==0))

    # nx.write_gexf(G, './outputs/graph.gexf')
    # nodes = [{'left': str(i), 'right': str(G.node[i]['bipartite'])}
    #          for i in G.nodes()]
    # links = [{'source': int(u[0]), 'target': int(u[1])}
    #          for u in G.edges()]
    # open('./outputs/graph2.json', 'w')
    # with open('./outputs/graph2.json', 'w') as f:
    #     json.dump({'nodes': nodes, 'links': links},
    #               f, indent=4)
    # print("num of nodes: {}\nnum of edges: {}".format( G.nodes.__len__(), G.edges.__len__()))
    # print("num of SNP: {}\nnum of Cancer: {}".format({n for n, d in G.nodes(data=True) if d['bipartite']==0}.__len__(), {n for n, d in G.nodes(data=True) if d['bipartite']==1}.__len__()))
    snp = {n for n, d in G.nodes(data=True) if d['bipartite'] == 0}.__len__()
    cancer = {n for n, d in G.nodes(data=True) if d['bipartite'] == 1}.__len__()
    headers = ['Number of nodes', 'Number of edges', 'SNP', 'Cancer']
    table = [[G.nodes.__len__(), G.edges.__len__(), snp, cancer]]
    print(tabulate(table, headers, tablefmt="fancy_grid"))
    # clustering_coefficient = nx.algorithms.bipartite.average_clustering(G)
    # print("\nclustering coefficient: ", clustering_coefficient)
    print(nx.number_connected_components(G))
    # evaluation_result = ev.evaluate(G, k=4, method='cn')
    # df = pd.DataFrame(evaluation_result)
    # print(df)
    pr.cn_predict(G)
    pr.jc_predict(G)
    pr.aa_predict(G)
    pr.pa_predict(G)


if __name__ == '__main__':
    main()
