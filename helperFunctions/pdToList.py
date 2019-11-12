def add_to_list(df: dict) -> list:
    """
    Generate link tuples and append them to a list
    :param df: Dataframe containing links
    :return: Edge list
    """
    edgeList = []
    for i in df.iterrows():
        # if not str(df_nodes[i[1][1]]).__contains__('.'):
        tuples = i[1][0], i[1][1]
        edgeList.append(tuples)
    return edgeList
