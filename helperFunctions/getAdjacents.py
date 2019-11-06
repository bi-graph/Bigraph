def getAdj2(G, inListt, n):
    """

    :param G:
    :param inListt:
    :param n:
    :return:
    """
    fullListt = []
    while (n > 0):
        n -= 1
        outListt = []
        for nd in G.nbunch_iter(inListt):
            for neigh in G[nd]:
                if neigh not in fullListt:
                    fullListt.append(neigh)
                    outListt.append(neigh)