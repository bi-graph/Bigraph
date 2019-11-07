def getAdj2(graph, inListt, n):
    """

    :param graph: NetworkX graph object
    :param inListt: Input list
    :param n: Hop N
    :return: N hop neighbours of the input list's items
    """
    fullListt = []
    while (n > 0):
        n -= 1
        outListt = []
        for nd in graph.nbunch_iter(inListt):
            for neigh in graph[nd]:
                if neigh not in fullListt:
                    fullListt.append(neigh)
                    outListt.append(neigh)
    return outListt
