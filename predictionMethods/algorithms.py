import math


def adamic_adar(setone, settwo, G):
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


def common_neighbors(setone, settwo):
    return len(set(setone) & set(settwo))


def preferential_attachment(setone, settwo):
    return len(set(setone)) * len(set(settwo))


def katz_similarity(i, j, G):
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
    return score


def jaccard(setone, settwo):
    intersection = len(set(setone) & set(settwo))
    union = len(set(setone) | set(settwo))
    return float(intersection) / float(union)
