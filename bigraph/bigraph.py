from _operator import itemgetter
from collections import defaultdict
from datetime import datetime

import networkx as nx

from bigraph.algorithms import jaccard, adamic_adar, common_neighbors, preferential_attachment, katz_similarity

from bigraph.preprocessing import get_adjacents


def jc_predict(G: object) -> dict:
    """
    Compute the Jaccard-Needham dissimilarity between two 1-D arrays.
    :param G: Networkx bipartite graph
    :return: A dictionary containing the Jaccard distance between vectors `left_element` and `right_element`.
    """
    start_jc = datetime.now()

    # print('Jaccard prediction starting...')
    dictionary = {}
    out = open('./predictions/jaccard.csv', 'w')
    outN = open('./predictions/jaccard_with_name.csv', 'w')
    hop2s = dict()
    neighbors = dict()
    jaccard_sim = defaultdict(dict)
    left_set = [n for n, d in G.nodes(data=True) if d['bipartite'] == 0]
    right_set = [n for n, d in G.nodes(data=True) if d['bipartite'] == 1]

    out.write('(left_element, right_element)')
    out.write(",")
    out.write('Probability')
    out.write("\n")

    # outN.write('(left_element, right_element)')
    # outN.write(",")
    # outN.write('Probability')
    # outN.write("\n")

    exception_count = 0
    for left_element in left_set:
        hop2s[left_element] = get_adjacents(G, list(set(G[left_element])), 1)
        for right_element in right_set:
            neighbors[right_element] = list(set(G[right_element]))
            if not (left_element, right_element) in G.edges:
                try:
                    jaccard_sim[left_element][right_element] = jaccard(hop2s[(left_element)],
                                                                       neighbors[(right_element)])
                    if jaccard_sim[left_element][right_element] > 0:
                        dictionary.update({(left_element, right_element): jaccard_sim[left_element][right_element]})
                except:
                    exception_count += 1
                    print(exception_count)
    for k, v in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
        # print(k[0],v)
        out.write(str((k[0], k[1])))
        out.write(",")
        out.write(str(jaccard_sim[k[0]][k[1]]))
        out.write("\n")
        # outN.write(str((df_nodes[k[0]], df_nodes[k[1]])))
        # outN.write(",")
        # outN.write(str(jaccard_sim[k[0]][k[1]]))
        # outN.write("\n")

    # print('Jaccard prediction finished sucnessfully')
    _time = start_jc - datetime.now()
    print('Jaccard Executed in {} seconds'.format(_time), "\n")

    return dictionary


def aa_predict(G: object) -> dict:
    """
    Compute the Jaccard-Needham dissimilarity between two 1-D arrays.
    :param G: Networkx bipartite graph
    :return: A dictionary containing the Adamic-adar score for `left_element` and `right_element`.
    """
    start_aa = datetime.now()

    # print('Adamic_adar prediction starting...')

    out = open('./predictions/adamic_adar.csv', 'w')
    outN = open('./predictions/adamic_adar_with_name.csv', 'w')
    hop2s = dict()
    neighbors = dict()
    aa_sim = defaultdict(dict)
    sortDic = {}
    left_set = [n for n, d in G.nodes(data=True) if d['bipartite'] == 0]
    right_set = [n for n, d in G.nodes(data=True) if d['bipartite'] == 1]
    dictionary = {}

    out.write('(left_element, right_element)')
    out.write(",")
    out.write('Probability')
    out.write("\n")

    # outN.write('(left_element, right_element)')
    # outN.write(",")
    # outN.write('Probability')
    # outN.write("\n")

    exception_count = 0
    for left_element in left_set:
        hop2s[left_element] = get_adjacents(G, list(set(G[left_element])), 1)
        for right_element in right_set:
            neighbors[right_element] = list(set(G[right_element]))
            if not (left_element, right_element) in G.edges:
                try:
                    aa_sim[left_element][right_element] = adamic_adar(hop2s[(left_element)],
                                                                      neighbors[(right_element)], G)
                    if aa_sim[left_element][right_element] > 0:
                        # print(left_element, right_element, aa_sim[left_element][right_element])
                        dictionary.update({(left_element, right_element): aa_sim[left_element][right_element]})
                except:
                    exception_count += 1
                    print(exception_count)

    for k, v in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
        # print(k[0],v)
        out.write(str((k[0], k[1])))
        out.write(",")
        out.write(str(aa_sim[k[0]][k[1]]))
        out.write("\n")

        # outN.write(str((df_nodes[k[0]], df_nodes[k[1]])))
        # outN.write(",")
        # outN.write(str(aa_sim[k[0]][k[1]]))
        # outN.write("\n")
    # print('Adamic-adar prediction finished sucnessfully')

    _time = start_aa - datetime.now()
    print('Adamic-adar Executed in {} seconds'.format(_time), "\n")
    return dictionary


def cn_predict(G: object) -> dict:
    """
    Return the common neighbors of two nodes in a graph.
    :param G: Networkx bipartite graph
    :return: A dictionary containing the Common neighbours score for `left_element` and `right_element`.
    """
    start_cn = datetime.now()

    # print('Common neighbor prediction starting...')

    out = open('./predictions/common_neighbor.csv', 'w')
    outN = open('./predictions/common_neighbor_with_name.csv', 'w')
    hop2s = dict()
    neighbors = dict()
    cn_sim = defaultdict(dict)
    sortDic = {}

    left_set = [n for n, d in G.nodes(data=True) if d['bipartite'] == 0]
    right_set = [n for n, d in G.nodes(data=True) if d['bipartite'] == 1]

    dictionary = {}
    out.write('(left_element, right_element)')
    out.write(",")
    out.write('Probability')
    out.write("\n")

    # outN.write('(left_element, right_element)')
    # outN.write(",")
    # outN.write('Probability')
    # outN.write("\n")

    for left_element in left_set:
        # print('snp {} -- '.format(len(G[left_element])))
        hop2s[left_element] = get_adjacents(G, list(set(G[left_element])), 1)
        # print('snp hop 2 {} -- '.format(len(hop2s[left_element])))
        for right_element in right_set:
            # print('cancer {} -- '.format(len(G[right_element])))
            neighbors[right_element] = list(set(G[right_element]))
            if not (left_element, right_element) in G.edges:
                cn_sim[left_element][right_element] = common_neighbors(hop2s[left_element],
                                                                       neighbors[right_element])

                # if (left_element, right_element) in edge_subset:
                #   print((left_element, right_element), cn_sim[left_element][right_element])
                if cn_sim[left_element][right_element] > 0:
                    dictionary.update({(left_element, right_element): cn_sim[left_element][right_element]})

    for k, v in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
        # print(k[0],v)
        out.write(str((k[0], k[1])))
        out.write(",")
        out.write(str(cn_sim[k[0]][k[1]]))
        out.write("\n")

        #     outN.write(str((df_nodes[k[0]], df_nodes[k[1]])))
        #     outN.write(",")
        #     outN.write(str(cn_sim[k[0]][k[1]]))
        #     outN.write("\n")
    # print('Common neighbor prediction finished sucnessfully')

    _time = start_cn - datetime.now()
    print('Common neighbours Executed in {} seconds'.format(_time), "\n")

    return dictionary


def pa_predict(G: object) -> dict:
    """
    Compute the preferential attachment score of all node pairs.
    :param G: Networkx bipartite graph
    :return: A dictionary containing the Preferential attachment score for `left_element` and `right_element`.
    """
    start_pa = datetime.now()
    # print('Preferential_attachment prediction starting...')
    dictionary = {}
    out = open('./predictions/preferential_attachment.csv', 'w')
    outN = open('./predictions/preferential_attachment_with_name.csv', 'w')
    hop2s = dict()
    neighbors_right_element = dict()
    neighbors_left_element = dict()
    pa_sim = defaultdict(dict)
    sortDic = {}
    left_set = [n for n, d in G.nodes(data=True) if d['bipartite'] == 0]
    right_set = [n for n, d in G.nodes(data=True) if d['bipartite'] == 1]

    out.write('(left_element, right_element)')
    out.write(",")
    out.write('Probability')
    out.write("\n")

    # outN.write('(left_element, right_element)')
    # outN.write(",")
    # outN.write('Probability')
    # outN.write("\n")

    for left_element in left_set:
        # hop2s[left_element] = get_adjacents(G, list(set(G[left_element])), 1)
        neighbors_left_element[left_element] = list(set(G[left_element]))
        for right_element in right_set:
            neighbors_right_element[right_element] = list(set(G[right_element]))
            if not (left_element, right_element) in G.edges:
                pa_sim[left_element][right_element] = preferential_attachment(
                    neighbors_left_element[(left_element)], neighbors_right_element[(right_element)])
                if pa_sim[left_element][right_element] > 0:
                    dictionary.update({(left_element, right_element): pa_sim[left_element][right_element]})

    for k, v in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
        # print(k[0],v)
        out.write(str((k[0], k[1])))
        out.write(",")
        out.write(str(pa_sim[k[0]][k[1]]))
        out.write("\n")

        # outN.write(str((df_nodes[k[0]], df_nodes[k[1]])))
        # outN.write(",")
        # outN.write(str(pa_sim[k[0]][k[1]]))
        # outN.write("\n")
    # print('Preferential_attachment prediction finished sucnessfully')

    _time = start_pa - datetime.now()
    print('Preferential attachment Executed in {} seconds'.format(_time), "\n")

    return dictionary


def katz_predict(G: object, df_nodes: dict) -> dict:
    """
    Compute the Katz similarity score of all node pairs.
    :param G: Networkx bipartite graph
    :param df_nodes: Graph nodes
    :return: A dictionary containing the Preferential attachment score for `left_element` and `right_element`.
    """
    start_pa = datetime.now()

    # print('Preferential_attachment prediction starting...')

    out = open('./predictions/preferential_attachment.csv', 'w')
    outN = open('./predictions/preferential_attachment_with_name.csv', 'w')
    hop2s = dict()
    neighbors = dict()
    katz_sim = defaultdict(dict)
    sortDic = {}
    left_set = list(set(nx.bipartite.sets(G)[0]))
    right_set = list(set(nx.bipartite.sets(G)[1]))

    out.write('(left_element, right_element)')
    out.write(",")
    out.write('Probability')
    out.write("\n")

    outN.write('(left_element, right_element)')
    outN.write(",")
    outN.write('Probability')
    outN.write("\n")

    for left_element in left_set:
        hop2s[left_element] = get_adjacents(G, list(set(G[left_element])), 1)
        for right_element in right_set:
            neighbors[right_element] = list(set(G[right_element]))
            if not (left_element, right_element) in G.edges:
                katz_sim[left_element][right_element] = katz_similarity(int(left_element), int(right_element), G)
                if katz_sim[left_element][right_element] > 0:
                    out.write(str((left_element, right_element)))
                    out.write(",")
                    out.write(str(katz_sim[left_element][right_element]))
                    out.write("\n")

                    outN.write(str((df_nodes[left_element], df_nodes[right_element])))
                    outN.write(",")
                    outN.write(str(katz_sim[left_element][right_element]))
                    outN.write("\n")

    # print('Katz similarity prediction finished sucnessfully')
    _time = start_pa - datetime.now()
    print('Katz similarity Executed in {} seconds'.format(_time), "\n")
