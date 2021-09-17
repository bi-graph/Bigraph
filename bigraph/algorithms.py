import math


def _adamic_adar(set_one: list, set_two: list, graph) -> float:
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


def _common_neighbors(set_one: list, set_two: list) -> int:
    """
    Calculate Common neighbors score for input lists

    :param set_one: A list of graph nodes -> part one
    :param set_two: A list of graph nodes -> part two
    :return: Common neighbours score
    """
    return len(set(set_one) & set(set_two))


def _preferential_attachment(set_one: list, set_two: list) -> int:
    """
    Calculate Preferential attachment score for input lists

    :param set_one: A list of graph nodes -> part one
    :param set_two: A list of graph nodes -> part two
    :return: Preferential attachment score
    """
    return len(set(set_one)) * len(set(set_two))


def _jaccard(set_one: list, set_two: list) -> float:
    """
    Calculate Jaccard score for input lists

    :param set_one: A list of graph nodes -> part one
    :param set_two: A list of graph nodes -> part two
    :return: Jaccard score
    """
    intersection = len(set(set_one) & set(set_two))
    union = len(set(set_one) | set(set_two))
    return float(intersection) / float(union)


def _katz_similarity(node_i: int, node_j: int, graph) -> float:
    """
    Calculate Katz score for input nodes

    :param node_i: Starting node
    :param node_j: Destination node
    :param graph: NetworkX bipartite graph
    :return: Katz similarity score
    """
    length = 1
    neighbors = set(graph[node_i])
    score = 0
    max_length = 2
    beta = 0.1

    while length <= max_length:
        number_of_paths = neighbors.count(node_j)
        if number_of_paths > 0:
            score += (beta ** length) * number_of_paths

        neighbours_for_next_loop = []
        for k in neighbors:
            neighbours_for_next_loop += set(graph[k])
        neighbors = neighbours_for_next_loop
        length += 1
    return score
