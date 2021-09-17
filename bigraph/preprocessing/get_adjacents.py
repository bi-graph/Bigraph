def _get_hop_2_neighbours(graph, input_list: list, hop_n: int) -> list:
    """
    Find hop_n neighbours of each item in input_list

    :param graph: NetworkX graph object
    :param input_list: Input list
    :param hop_n: Hop hop_n
    :return: hop_n hop neighbours of the input list's items
    """
    full_list = []
    while hop_n > 0:
        hop_n -= 1
        output_list = []
        for node in graph.nbunch_iter(input_list):
            for neighbour in graph[node]:
                if neighbour not in full_list:
                    full_list.append(neighbour)
                    output_list.append(neighbour)
    return output_list
