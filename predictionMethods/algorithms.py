def adamic_adar(set_one: list, set_two: list, G) -> float:
    """
    Calculate Adamic Adar score for input lists
    :param set_one: A list of graph nodes -> part one
    :param set_two: A list of graph nodes -> part two
    :param G: NetworkX bipartite graph
    :return: Adamic Adar score
    """
    intersection = (set(set_one) & set(set_two))
    sum = 0
    for node in intersection:
        # Get neighbors count
        degree = set(G[node]).__len__()
        if degree > 1:
            sum += (math.log(degree)) ** -1
        else:
            sum += 0
    return sum

def common_neighbors(setone, settwo):
    """

    :param setone:
    :param settwo:
    :return:
    """
    return len(set(setone) & set(settwo))
