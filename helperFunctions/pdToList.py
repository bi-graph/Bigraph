def add_to_list(dataframe: dict) -> list:
    """
    Generate link tuples and append them to a list
    :param dataframe: Dataframe containing links
    :return: Edge list
    """
    edge_list = []
    for i in dataframe.iterrows():
        # if not str(df_nodes[i[1][1]]).__contains__('.'):
        tuples = i[1][0], i[1][1]
        edge_list.append(tuples)
    return edge_list
