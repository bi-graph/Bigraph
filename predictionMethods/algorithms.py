import math


def adamic_adar(set_one: list, set_two: list, graph) -> float:
    """
    Calculate Adamic Adar score for input lists
    :param set_one: A list of graph nodes -> part one
    :param set_two: A list of graph nodes -> part two
    :param graph: NetworkX bipartite graph
    :return: Adamic Adar score
    """
    intersection = (set(set_one) & set(set_two))
    sum = 0
    for node in intersection:
        # Get neighbors count
        degree = set(graph[node]).__len__()
        if degree > 1:
            sum += (math.log(degree)) ** -1
        else:
            sum += 0
    return sum


def common_neighbors(set_one: list, set_two: list) -> int:
    """
    Calculate Common neighbors score for input lists
    :param set_one: A list of graph nodes -> part one
    :param set_two: A list of graph nodes -> part two
    :return: Common neighbours score
    """
    return len(set(set_one) & set(set_two))


def preferential_attachment(set_one: list, set_two: list) -> int:
    """
    Calculate Preferential attachment score for input lists
    :param set_one: A list of graph nodes -> part one
    :param set_two: A list of graph nodes -> part two
    :return: Preferential attachment score
    """
    return len(set(set_one)) * len(set(set_two))


def jaccard(set_one: list, set_two: list) -> float:
    """
    Calculate Jaccard score for input lists
    :param set_one: A list of graph nodes -> part one
    :param set_two: A list of graph nodes -> part two
    :return: Jaccard score
    """
    intersection = len(set(set_one) & set(set_two))
    union = len(set(set_one) | set(set_two))
    return float(intersection) / float(union)

def katz_similarity(i, j, G):
    """

    :param i:
    :param j:
    :param G:
    :return:
    """
    l = 1
    neighbors = set(G[i])
    score = 0
    maxl = 2
    beta = 0.1

    while l <= maxl:
        numberOfPaths = neighbors.count(j)
        if numberOfPaths > 0:
            score += (beta ** l) * numberOfPaths

        neighborsForNextLoop = []
        for k in neighbors:
            neighborsForNextLoop += set(G[k])
        neighbors = neighborsForNextLoop
        l += 1