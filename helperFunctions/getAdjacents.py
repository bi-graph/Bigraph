def getAdj2(graph, inListt, n):
    """

    :param graph:
    :param inListt:
    :param n:
    :return:
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
