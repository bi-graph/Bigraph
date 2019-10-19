from _operator import itemgetter
from collections import defaultdict
from datetime import datetime

import networkx as nx

from helperFunctions.getAdjacents import getAdj2
from predictionMethods.algorithms import adamic_adar, common_neighbors, preferential_attachment, katz_similarity, \
    jaccard


def jc_predict(G, df_nodes):
    start_jc = datetime.now()

    # print('Jaccard prediction starting...')
    dictionary = {}
    out = open('./predictions/jaccard.csv', 'w')
    outN = open('./predictions/jaccard_with_name.csv', 'w')
    hop2s = dict()
    neighbors = dict()
    jaccard_sim = defaultdict(dict)
    pros = list(set(nx.bipartite.sets(G)[0]))
    icds = list(set(nx.bipartite.sets(G)[1]))

    out.write('(Probiotic, ICD)')
    out.write(",")
    out.write('Probability')
    out.write("\n")

    outN.write('(Probiotic, ICD)')
    outN.write(",")
    outN.write('Probability')
    outN.write("\n")

    for pro in pros:
        hop2s[pro] = getAdj2(G, list(set(G[pro])), 1)
        for icd in icds:
            neighbors[icd] = list(set(G[icd]))
            if not (pro, icd) in G.edges:
                jaccard_sim[pro][icd] = jaccard(hop2s[int(pro)], neighbors[int(icd)])
                if jaccard_sim[pro][icd] > 0:
                    dictionary.update({(pro, icd): jaccard_sim[pro][icd]})

    for k, v in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
        # print(k[0],v)
        out.write(str((k[0], k[1])))
        out.write(",")
        out.write(str(jaccard_sim[k[0]][k[1]]))
        out.write("\n")

        outN.write(str((df_nodes[k[0]], df_nodes[k[1]])))
        outN.write(",")
        outN.write(str(jaccard_sim[k[0]][k[1]]))
        outN.write("\n")
    # print('Jaccard prediction finished sucnessfully')
    end_jc = datetime.now()
    # print('Jaccard duration: {}'.format(end_jc - start_jc), "\n")
    return dictionary


def aa_predict(G, df_nodes):
    start_aa = datetime.now()

    # print('Adamic_adar prediction starting...')

    out = open('./predictions/adamic_adar.csv', 'w')
    outN = open('./predictions/adamic_adar_with_name.csv', 'w')
    hop2s = dict()
    neighbors = dict()
    aa_sim = defaultdict(dict)
    sortDic = {}
    pros = list(set(nx.bipartite.sets(G)[0]))
    icds = list(set(nx.bipartite.sets(G)[1]))
    dictionary = {}
    out.write('(Probiotic, ICD)')
    out.write(",")
    out.write('Probability')
    out.write("\n")

    outN.write('(Probiotic, ICD)')
    outN.write(",")
    outN.write('Probability')
    outN.write("\n")

    for pro in pros:
        hop2s[pro] = getAdj2(G, list(set(G[pro])), 1)
        for icd in icds:
            neighbors[icd] = list(set(G[icd]))
            if not (pro, icd) in G.edges:
                aa_sim[pro][icd] = adamic_adar(hop2s[int(pro)], neighbors[int(icd)], G)
                if aa_sim[pro][icd] > 0:
                    dictionary.update({(pro, icd): aa_sim[pro][icd]})

    for k, v in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
        # print(k[0],v)
        out.write(str((k[0], k[1])))
        out.write(",")
        out.write(str(aa_sim[k[0]][k[1]]))
        out.write("\n")

        outN.write(str((df_nodes[k[0]], df_nodes[k[1]])))
        outN.write(",")
        outN.write(str(aa_sim[k[0]][k[1]]))
        outN.write("\n")
    print('Adamic-adar prediction finished sucnessfully')
    end_aa = datetime.now()
    print('Adamic-adar duration: {}'.format(end_aa - start_aa), "\n")
    return dictionary


def cn_predict(G, df_nodes):
    start_cn = datetime.now()

    print('Common neighbor prediction starting...')

    out = open('./predictions/common_neighbor.csv', 'w')
    outN = open('./predictions/common_neighbor_with_name.csv', 'w')
    hop2s = dict()
    neighbors = dict()
    cn_sim = defaultdict(dict)
    sortDic = {}
    pros = list(set(nx.bipartite.sets(G)[0]))
    icds = list(set(nx.bipartite.sets(G)[1]))
    dictionary = {}
    out.write('(Probiotic, ICD)')
    out.write(",")
    out.write('Probability')
    out.write("\n")

    outN.write('(Probiotic, ICD)')
    outN.write(",")
    outN.write('Probability')
    outN.write("\n")

    for pro in pros:
        hop2s[pro] = getAdj2(G, list(set(G[pro])), 1)
        for icd in icds:
            neighbors[icd] = list(set(G[icd]))
            if not (pro, icd) in G.edges:
                cn_sim[pro][icd] = common_neighbors(hop2s[int(pro)], neighbors[int(icd)])
                if cn_sim[pro][icd] > 0:
                    dictionary.update({(pro, icd): cn_sim[pro][icd]})

    for k, v in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
        # print(k[0],v)
        out.write(str((k[0], k[1])))
        out.write(",")
        out.write(str(cn_sim[k[0]][k[1]]))
        out.write("\n")

        outN.write(str((df_nodes[k[0]], df_nodes[k[1]])))
        outN.write(",")
        outN.write(str(cn_sim[k[0]][k[1]]))
        outN.write("\n")
    # print('Common neghbor prediction finished sucnessfully')
    end_cn = datetime.now()
    # print('Common neghbor duration: {}'.format(end_cn - start_cn), "\n")
    return dictionary


def pa_predict(G, df_nodes):
    start_pa = datetime.now()
    print('Preferential_attachment prediction starting...')
    dictionary = {}
    out = open('./predictions/preferential_attachment.csv', 'w')
    outN = open('./predictions/preferential_attachment_with_name.csv', 'w')
    hop2s = dict()
    neighborsICD = dict()
    neighborsPro = dict()
    pa_sim = defaultdict(dict)
    sortDic = {}
    pros = list(set(nx.bipartite.sets(G)[0]))
    icds = list(set(nx.bipartite.sets(G)[1]))

    out.write('(Probiotic, ICD)')
    out.write(",")
    out.write('Probability')
    out.write("\n")

    outN.write('(Probiotic, ICD)')
    outN.write(",")
    outN.write('Probability')
    outN.write("\n")

    for pro in pros:
        # hop2s[pro] = getAdj2(G, list(set(G[pro])), 1)
        neighborsPro[pro] = list(set(G[pro]))
        for icd in icds:
            neighborsICD[icd] = list(set(G[icd]))
            if not (pro, icd) in G.edges:
                pa_sim[pro][icd] = preferential_attachment(neighborsPro[int(pro)], neighborsICD[int(icd)])
                if pa_sim[pro][icd] > 0:
                    dictionary.update({(pro, icd): pa_sim[pro][icd]})

    for k, v in sorted(dictionary.items(), key=itemgetter(1), reverse=True):
        # print(k[0],v)
        out.write(str((k[0], k[1])))
        out.write(",")
        out.write(str(pa_sim[k[0]][k[1]]))
        out.write("\n")

        outN.write(str((df_nodes[k[0]], df_nodes[k[1]])))
        outN.write(",")
        outN.write(str(pa_sim[k[0]][k[1]]))
        outN.write("\n")
    print('Preferential_attachment prediction finished sucnessfully')
    end_pa = datetime.now()
    # print('Common neghbor duration: {}'.format(end_pa - start_pa), "\n")
    return dictionary


def katz_predict(G, df_nodes):
    start_pa = datetime.now()

    print('Preferential_attachment prediction starting...')

    out = open('./predictions/preferential_attachment.csv', 'w')
    outN = open('./predictions/preferential_attachment_with_name.csv', 'w')
    hop2s = dict()
    neighbors = dict()
    pa_sim = defaultdict(dict)
    sortDic = {}
    pros = list(set(nx.bipartite.sets(G)[0]))
    icds = list(set(nx.bipartite.sets(G)[1]))

    out.write('(Probiotic, ICD)')
    out.write(",")
    out.write('Probability')
    out.write("\n")

    outN.write('(Probiotic, ICD)')
    outN.write(",")
    outN.write('Probability')
    outN.write("\n")

    for pro in pros:
        hop2s[pro] = getAdj2(G, list(set(G[pro])), 1)
        for icd in icds:
            neighbors[icd] = list(set(G[icd]))
            if not (pro, icd) in G.edges:
                pa_sim[pro][icd] = katz_similarity(int(pro), int(icd), G)
                if pa_sim[pro][icd] > 0:
                    out.write(str((pro, icd)))
                    out.write(",")
                    out.write(str(pa_sim[pro][icd]))
                    out.write("\n")

                    outN.write(str((df_nodes[pro], df_nodes[icd])))
                    outN.write(",")
                    outN.write(str(pa_sim[pro][icd]))
                    outN.write("\n")
    print('Preferential_attachment prediction finished sucnessfully')
    end_pa = datetime.now()
    print('Common neghbor duration: {}'.format(end_pa - start_pa), "\n")
