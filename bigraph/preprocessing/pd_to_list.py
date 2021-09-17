def _add_to_list(dataframe: dict) -> list:
    """
    Generate link tuples and append them to a list

    :param dataframe: Dataframe containing links
    :return: Edge list
    """
    edge_list = []
    for edge_row in dataframe.iterrows():
        # if not str(df_nodes[edge_row[1][1]]).__contains__('.'):
        tuples = edge_row[1][0], edge_row[1][1]
        edge_list.append(tuples)
    return edge_list
