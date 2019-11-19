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

def jaccard(set_one, set_two):
    """

    :param set_one:
    :param set_two:
    :return:
    """
    intersection = len(set(set_one) & set(set_two))
    union = len(set(set_one) | set(set_two))
    return float(intersection) / float(union)
