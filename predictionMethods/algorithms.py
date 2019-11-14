
def adamic_adar(set_one, set_two, G):
    """
    
    :param set_one:
    :param set_two:
    :param G:
    :return:
    """
    intersection = (set(set_one) & set(set_two))
    sum = 0
    for node in intersection:
        # Get neighbors count
        deg = set(G[node]).__len__()
        if (deg > 1):
            sum += (math.log(deg)) ** -1
        else:
            sum += 0
    return sum