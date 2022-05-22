import collections
import operator
import pathlib
import time

import networkx as nx
import tabulate

from bigraph.preprocessing import ImportFiles
from .algorithms import Algorithms
from .preprocessing import GetAdjacents
from .preprocessing import MakeGraph


class BiGraph(Algorithms, ImportFiles, MakeGraph, GetAdjacents):
    def __init__(self):
        df, df_nodes = self.import_files()
        self.graph = self.make_graph(df)

        print(self.graph.__dict__)
        snp = len({n for n, d in self.graph.nodes(data=True) if d["bipartite"] == 0})
        cancer = len({n for n, d in self.graph.nodes(data=True) if d["bipartite"] == 1})
        headers = ["Number of nodes", "Number of edges", "SNP", "Cancer"]
        table = [[self.graph.nodes.__len__(), self.graph.edges.__len__(), snp, cancer]]
        print(tabulate.tabulate(table, headers, tablefmt="fancy_grid"))
        print(nx.number_connected_components(self.graph))

    def jc_predict(self) -> dict:
        """
        Compute the Jaccard-Needham dissimilarity between two 1-D arrays.

        :return: A dictionary containing the Jaccard distance between vectors `left_element` and `right_element`.
        """
        start_jc = time.time()

        dictionary = {}
        pathlib.Path("./predictions").mkdir(parents=True, exist_ok=True)

        out = open("./predictions/jaccard.csv", "w")
        hop2s = dict()
        neighbors = dict()
        jaccard_sim = collections.defaultdict(dict)
        left_set = [n for n, d in self.graph.nodes(data=True) if d["bipartite"] == 0]
        right_set = [n for n, d in self.graph.nodes(data=True) if d["bipartite"] == 1]

        out.write("(left_element, right_element)")
        out.write(",")
        out.write("Score")
        out.write("\n")

        exception_count = 0
        for left_element in left_set:
            hop2s[left_element] = self._get_hop_2_neighbours(
                self.graph, list(set(self.graph[left_element])), 1
            )
            for right_element in right_set:
                neighbors[right_element] = list(set(self.graph[right_element]))
                if not (left_element, right_element) in self.graph.edges:
                    try:
                        jaccard_sim[left_element][right_element] = self.jaccard(
                            hop2s[(left_element)], neighbors[(right_element)]
                        )
                        if jaccard_sim[left_element][right_element] > 0:
                            dictionary.update(
                                {
                                    (left_element, right_element): jaccard_sim[
                                        left_element
                                    ][right_element]
                                }
                            )
                    except:
                        exception_count += 1
                        print(exception_count)
        for k, v in sorted(
            dictionary.items(), key=operator.itemgetter(1), reverse=True
        ):
            out.write(str((k[0], k[1])))
            out.write(",")
            out.write(str(jaccard_sim[k[0]][k[1]]))
            out.write("\n")

        _time = time.time() - start_jc
        print("Jaccard Executed in {} seconds".format(_time), "\n")

        return dictionary

    def aa_predict(self) -> dict:
        """
        Compute the Jaccard-Needham dissimilarity between two 1-D arrays.

        :return: A dictionary containing the Adamic-adar score for `left_element` and `right_element`.
        """
        start_aa = time.time()

        print("Adamic_adar prediction starting...")
        pathlib.Path("./predictions").mkdir(parents=True, exist_ok=True)

        out = open("./predictions/adamic_adar.csv", "w")
        outN = open("./predictions/adamic_adar_with_name.csv", "w")
        hop2s = dict()
        neighbors = dict()
        aa_sim = collections.defaultdict(dict)
        sortDic = {}
        left_set = [n for n, d in self.graph.nodes(data=True) if d["bipartite"] == 0]
        right_set = [n for n, d in self.graph.nodes(data=True) if d["bipartite"] == 1]
        dictionary = {}

        out.write("(left_element, right_element)")
        out.write(",")
        out.write("Score")
        out.write("\n")

        exception_count = 0
        for left_element in left_set:
            hop2s[left_element] = self._get_hop_2_neighbours(
                self.graph, list(set(self.graph[left_element])), 1
            )
            for right_element in right_set:
                neighbors[right_element] = list(set(self.graph[right_element]))
                if not (left_element, right_element) in self.graph.edges:
                    try:
                        aa_sim[left_element][right_element] = self.adamic_adar(
                            hop2s[(left_element)],
                            neighbors[(right_element)],
                            self.graph,
                        )
                        if aa_sim[left_element][right_element] > 0:
                            dictionary.update(
                                {
                                    (left_element, right_element): aa_sim[left_element][
                                        right_element
                                    ]
                                }
                            )
                    except:
                        exception_count += 1
                        print(exception_count)

        for k, v in sorted(
            dictionary.items(), key=operator.itemgetter(1), reverse=True
        ):
            out.write(str((k[0], k[1])))
            out.write(",")
            out.write(str(aa_sim[k[0]][k[1]]))
            out.write("\n")

        _time = time.time() - start_aa
        print("Adamic-adar Executed in {} seconds".format(_time), "\n")
        return dictionary

    def cn_predict(self) -> dict:
        """
        Return the common neighbors of two nodes in a graph.

        :return: A dictionary containing the Common neighbours score for `left_element` and `right_element`.
        """
        start_cn = time.time()

        pathlib.Path("./predictions").mkdir(parents=True, exist_ok=True)

        out = open("./predictions/common_neighbor.csv", "w")
        hop2s = dict()
        neighbors = dict()
        cn_sim = collections.defaultdict(dict)
        sortDic = {}

        left_set = [n for n, d in self.graph.nodes(data=True) if d["bipartite"] == 0]
        right_set = [n for n, d in self.graph.nodes(data=True) if d["bipartite"] == 1]

        dictionary = {}
        out.write("(left_element, right_element)")
        out.write(",")
        out.write("Score")
        out.write("\n")

        for left_element in left_set:
            hop2s[left_element] = self._get_hop_2_neighbours(
                self.graph, list(set(self.graph[left_element])), 1
            )
            for right_element in right_set:
                # print('cancer {} -- '.format(len(G[right_element])))
                neighbors[right_element] = list(set(self.graph[right_element]))
                if not (left_element, right_element) in self.graph.edges:
                    cn_sim[left_element][right_element] = self.common_neighbors(
                        hop2s[left_element], neighbors[right_element]
                    )

                    if cn_sim[left_element][right_element] > 0:
                        dictionary.update(
                            {
                                (left_element, right_element): cn_sim[left_element][
                                    right_element
                                ]
                            }
                        )

        for k, v in sorted(
            dictionary.items(), key=operator.itemgetter(1), reverse=True
        ):
            # print(k[0],v)
            out.write(str((k[0], k[1])))
            out.write(",")
            out.write(str(cn_sim[k[0]][k[1]]))
            out.write("\n")

        _time = time.time() - start_cn
        print("Common neighbours Executed in {} seconds".format(_time), "\n")

        return dictionary

    def pa_predict(self) -> dict:
        """
        Compute the preferential attachment score of all node pairs.

        :return: A dictionary containing the Preferential attachment score for `left_element` and `right_element`.
        """
        start_pa = time.time()
        # print('Preferential_attachment prediction starting...')
        dictionary = {}

        pathlib.Path("./predictions").mkdir(parents=True, exist_ok=True)
        out = open("./predictions/preferential_attachment.csv", "w")
        hop2s = dict()
        neighbors_right_element = dict()
        neighbors_left_element = dict()
        pa_sim = collections.defaultdict(dict)
        sortDic = {}
        left_set = [n for n, d in self.graph.nodes(data=True) if d["bipartite"] == 0]
        right_set = [n for n, d in self.graph.nodes(data=True) if d["bipartite"] == 1]

        out.write("(left_element, right_element)")
        out.write(",")
        out.write("Score")
        out.write("\n")

        for left_element in left_set:
            neighbors_left_element[left_element] = list(set(self.graph[left_element]))
            for right_element in right_set:
                neighbors_right_element[right_element] = list(
                    set(self.graph[right_element])
                )
                if not (left_element, right_element) in self.graph.edges:
                    pa_sim[left_element][right_element] = self.preferential_attachment(
                        neighbors_left_element[(left_element)],
                        neighbors_right_element[(right_element)],
                    )
                    if pa_sim[left_element][right_element] > 0:
                        dictionary.update(
                            {
                                (left_element, right_element): pa_sim[left_element][
                                    right_element
                                ]
                            }
                        )

        for k, v in sorted(
            dictionary.items(), key=operator.itemgetter(1), reverse=True
        ):
            out.write(str((k[0], k[1])))
            out.write(",")
            out.write(str(pa_sim[k[0]][k[1]]))
            out.write("\n")

        _time = time.time() - start_pa
        print("Preferential attachment Executed in {} seconds".format(_time), "\n")

        return dictionary

    def katz_predict(self, df_nodes: dict) -> dict:
        """
        Compute the Katz similarity score of all node pairs.

        :param df_nodes: Graph nodes
        :return: A dictionary containing the Preferential attachment score for `left_element` and `right_element`.
        """
        start_katz = time.time()

        pathlib.Path("./predictions").mkdir(parents=True, exist_ok=True)

        out = open("./predictions/preferential_attachment.csv", "w")
        outN = open("./predictions/preferential_attachment_with_name.csv", "w")
        hop2s = dict()
        neighbors = dict()
        katz_sim = collections.defaultdict(dict)
        sortDic = {}
        left_set = list(set(nx.bipartite.sets(self.graph)[0]))
        right_set = list(set(nx.bipartite.sets(self.graph)[1]))

        out.write("(left_element, right_element)")
        out.write(",")
        out.write("Score")
        out.write("\n")

        outN.write("(left_element, right_element)")
        outN.write(",")
        outN.write("Score")
        outN.write("\n")

        for left_element in left_set:
            hop2s[left_element] = self._get_hop_2_neighbours(
                self.graph, list(set(self.graph[left_element])), 1
            )
            for right_element in right_set:
                neighbors[right_element] = list(set(self.graph[right_element]))
                if not (left_element, right_element) in self.graph.edges:
                    katz_sim[left_element][right_element] = self.katz_similarity(
                        int(left_element), int(right_element), self.graph
                    )
                    if katz_sim[left_element][right_element] > 0:
                        out.write(str((left_element, right_element)))
                        out.write(",")
                        out.write(str(katz_sim[left_element][right_element]))
                        out.write("\n")

                        outN.write(
                            str((df_nodes[left_element], df_nodes[right_element]))
                        )
                        outN.write(",")
                        outN.write(str(katz_sim[left_element][right_element]))
                        outN.write("\n")

        _time = time.time() - start_katz
        print("Katz similarity Executed in {} seconds".format(_time), "\n")
