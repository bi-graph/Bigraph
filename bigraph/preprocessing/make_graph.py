import networkx as nx


class MakeGraph:
    def make_graph(
        self,
        dataframe: dict,
        left_bipartite: str = "left_side",
        right_bipartite: str = "right_side",
    ):
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

        graph.add_edges_from(self._add_to_list(dataframe))
        isolates = nx.isolates(graph)
        # TODO: make following line a choice to be able to remove isolates or not

        # graph.remove_nodes_from(isolates)
        print("Graph made successfully", "\n")
        return graph

    def _add_to_list(self, dataframe: dict) -> list:
        """
        Generate link tuples and append them to a list

        :param dataframe: Dataframe containing links
        :return: Edge list
        """
        edge_list = []
        for edge_row in dataframe.iterrows():
            tuples = edge_row[1][0], edge_row[1][1]
            edge_list.append(tuples)
        return edge_list
