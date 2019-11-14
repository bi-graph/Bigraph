
def adamic_adar(setone, settwo, G):
    """

    :param setone:
    :param settwo:
    :param G:
    :return:
    """
    intersection = (set(setone) & set(settwo))
    sum = 0
    for i in intersection:
        # Get neighbors count
        deg = set(G[i]).__len__()
        if (deg > 1):
            sum += (math.log(deg)) ** -1
        else:
            sum += 0
    return sum