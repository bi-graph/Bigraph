def getAdj2(graph, input_list, n):
    """

    :param graph: NetworkX graph object
    :param input_list: Input list
    :param n: Hop N
    :return: N hop neighbours of the input list's items
    """
    full_list = []
    while (n > 0):
        n -= 1
        outListt = []
        for nd in graph.nbunch_iter(input_list):
            for neigh in graph[nd]:
                if neigh not in full_list:
                    full_list.append(neigh)
                    outListt.append(neigh)
    return outListt
